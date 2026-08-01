"""Group-aware bootstrap and split-conformal uncertainty utilities."""
import numpy as np
import pandas as pd
from sklearn.base import clone
from .validation import group_holdout
FEATURES=['days_passed','temperature','state_of_charge','chemistry']

def conformal_evaluate(model,df,alpha=0.1,seed=31):
    fit,outer=group_holdout(df,seed=seed,test_fraction=.25); train,cal=group_holdout(fit,seed=seed+1,test_fraction=.25)
    m=clone(model).fit(train[FEATURES],train.soh); cal_err=np.abs(cal.soh-m.predict(cal[FEATURES])); q=float(np.quantile(cal_err,min(1,np.ceil((len(cal_err)+1)*(1-alpha))/len(cal_err)),method='higher'))
    pred=m.predict(outer[FEATURES]); lo=pred-q; hi=pred+q
    out=outer[['chemistry','cell_key','days_passed','temperature','state_of_charge','soh']].copy(); out['predicted_soh']=pred; out['lower_soh']=lo; out['upper_soh']=hi; out['covered']=(out.soh>=lo)&(out.soh<=hi)
    metrics={'alpha':alpha,'interval_half_width':q,'empirical_coverage':float(out.covered.mean()),'test_rows':len(out),'test_groups':out.cell_key.nunique()}
    return m,metrics,out

def grouped_bootstrap_metrics(model,df,n_boot=200,seed=44):
    rng=np.random.default_rng(seed); train,test=group_holdout(df); model=clone(model).fit(train[FEATURES],train.soh); pred=model.predict(test[FEATURES]); base=test.assign(error=np.abs(test.soh-pred)); keys=base.cell_key.unique(); vals=[]
    for _ in range(n_boot):
        sampled=rng.choice(keys,len(keys),replace=True); vals.append(np.mean(np.concatenate([base.loc[base.cell_key==k,'error'].to_numpy() for k in sampled])))
    return {'mae_point':float(base.error.mean()),'mae_ci95_low':float(np.quantile(vals,.025)),'mae_ci95_high':float(np.quantile(vals,.975)),'bootstrap_replicates':n_boot}
