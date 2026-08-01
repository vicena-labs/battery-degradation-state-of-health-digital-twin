import numpy as np
from battery_twin import load_lis_cycle_capacity,observed_eol,forecast_eol,benchmark_rul

def test_lis_parser_and_conditions():
 d=load_lis_cycle_capacity(); assert d.condition.nunique()==10; assert len(d)>=100; assert d.soh.between(0,1.2).all()
def test_eol_interpolation_and_forecast():
 d=load_lis_cycle_capacity(); g=d[d.condition=='10oC']; assert 60<observed_eol(g,.8)<100; assert np.isfinite(forecast_eol(g,60,.8))
def test_rul_benchmark_has_observed_conditions():
 d=load_lis_cycle_capacity(); r,m=benchmark_rul(d); assert r.observed.sum()>=8; assert {'linear','exponential'}==set(m); assert m['linear']['mae_cycles']>0
