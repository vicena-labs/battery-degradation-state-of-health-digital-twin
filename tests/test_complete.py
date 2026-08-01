import numpy as np
import pandas as pd
from battery_twin import PackParameters,simulate_pack,load_calendar_ageing,fit_evaluate,conformal_evaluate,stress_sensitivity,pareto_policies,validate_csv

def test_pack_outputs_and_repeatability():
 t=np.arange(0,301); i=np.ones(len(t))*4; a,_=simulate_pack(t,i,seed=4,pack=PackParameters(4,2)); b,_=simulate_pack(t,i,seed=4,pack=PackParameters(4,2)); assert np.allclose(a.pack_voltage_v,b.pack_voltage_v); assert (a.soc_spread>=0).all()
def test_conformal_outputs():
 d=load_calendar_ageing(); m,_,_,_,_=fit_evaluate(d); _,q,o=conformal_evaluate(m,d); assert 0<q['interval_half_width']<.3; assert 0<=q['empirical_coverage']<=1; assert (o.lower_soh<=o.upper_soh).all()
def test_decision_outputs():
 s=stress_sensitivity(); p=pareto_policies(); assert len(s)==36; assert p.pareto.any(); assert s.soh.between(0,1).all()
def test_upload_validation(tmp_path):
 f=tmp_path/'ok.csv'; pd.DataFrame({'State-of-Charge':[50],'Temperature':[25],'Cell Identity Number':[1],'Days Passed':[0],'Discharge Capacity':[2.0],'Charge Capacity':[2.0]}).to_csv(f,index=False); assert validate_csv(f)['valid']
 bad=tmp_path/'bad.csv'; pd.DataFrame({'x':[1]}).to_csv(bad,index=False); assert not validate_csv(bad)['valid']
