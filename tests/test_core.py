import numpy as np
from battery_twin import simulate_profile,synthetic_aging,load_calendar_ageing,group_holdout

def test_electrothermal_bounds():
 t=np.arange(0,601); d=simulate_profile(t,np.ones_like(t)*3)
 assert d.soc.iloc[-1] < d.soc.iloc[0]
 assert d.temperature_c.max() > 25
 assert d.voltage_v.between(2.5,4.5).all()
def test_aging_monotonic():
 d=synthetic_aging(np.arange(0,366)); assert (d.soh.diff().dropna()<=1e-12).all()
def test_measured_group_split():
 d=load_calendar_ageing(); tr,te=group_holdout(d); assert set(tr.cell_key).isdisjoint(set(te.cell_key)); assert len(te)>0
