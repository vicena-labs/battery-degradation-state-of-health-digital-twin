"""Level 1 measured calendar-aging ingestion and held-out validation."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,PolynomialFeatures,StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge,LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

def load_calendar_ageing(path='datasets/measured/calendar_ageing'):
    frames=[]
    for f in sorted(Path(path).glob('*_Data.csv')):
        d=pd.read_csv(f); d.columns=[c.strip().lower().replace('-','_').replace(' ','_') for c in d.columns]
        d['chemistry']=f.stem.split('_')[0]
        d['cell_key']=d['chemistry']+'_'+d['cell_identity_number'].astype(str)+'_'+d['state_of_charge'].astype(str)+'_'+d['temperature'].astype(str)
        d['initial_capacity_ah']=d.groupby('cell_key')['discharge_capacity'].transform('first')
        d['soh']=d['discharge_capacity']/d['initial_capacity_ah']
        frames.append(d)
    if not frames: raise FileNotFoundError(path)
    out=pd.concat(frames,ignore_index=True)
    required=['state_of_charge','temperature','days_passed','discharge_capacity','chemistry','cell_key','soh']
    if out[required].isna().any().any(): raise ValueError('Measured data contain missing required values')
    return out

def group_holdout(df,seed=21,test_fraction=0.25):
    keys=np.array(sorted(df.cell_key.unique())); rng=np.random.default_rng(seed); rng.shuffle(keys)
    n=max(1,int(np.ceil(len(keys)*test_fraction))); test=set(keys[:n])
    return df[~df.cell_key.isin(test)].copy(),df[df.cell_key.isin(test)].copy()

def fit_evaluate(df):
    train,test=group_holdout(df)
    features=['days_passed','temperature','state_of_charge','chemistry']; cat=['chemistry']; num=features[:-1]
    pre=ColumnTransformer([('num',make_pipeline(PolynomialFeatures(2,include_bias=False),StandardScaler()),num),('cat',OneHotEncoder(handle_unknown='ignore'),cat)])
    model=make_pipeline(pre,Ridge(alpha=2.0)); model.fit(train[features],train.soh); pred=model.predict(test[features])
    base=np.full(len(test),train.soh.mean())
    metrics={'n_rows':len(df),'n_groups':df.cell_key.nunique(),'train_groups':train.cell_key.nunique(),'test_groups':test.cell_key.nunique(),'mae':mean_absolute_error(test.soh,pred),'rmse':mean_squared_error(test.soh,pred)**0.5,'r2':r2_score(test.soh,pred),'baseline_mae':mean_absolute_error(test.soh,base)}
    result=test[['chemistry','cell_key','days_passed','temperature','state_of_charge','soh']].copy(); result['predicted_soh']=pred; result['residual']=result.soh-result.predicted_soh
    return model,metrics,result,train,test
