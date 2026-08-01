"""Sensitivity and constrained operating-policy screening."""
import itertools
import numpy as np
import pandas as pd
from .core import synthetic_aging

def stress_sensitivity(days=365):
    rows=[]
    for temp,soc,efc in itertools.product([15,25,35,45],[.3,.6,.9],[.2,.7,1.2]):
        end=synthetic_aging([0,days],temp,soc,efc).iloc[-1]
        rows.append({'temperature_c':temp,'storage_soc':soc,'efc_per_day':efc,'soh':end.soh,'resistance_ratio':end.resistance_ratio})
    return pd.DataFrame(rows)
def pareto_policies(days=365,min_daily_efc=.2):
    d=stress_sensitivity(days); d=d[d.efc_per_day>=min_daily_efc].copy(); d['throughput_efc']=d.efc_per_day*days
    efficient=[]
    for i,r in d.iterrows():
        dominated=((d.throughput_efc>=r.throughput_efc)&(d.soh>=r.soh)&((d.throughput_efc>r.throughput_efc)|(d.soh>r.soh))).any(); efficient.append(not dominated)
    d['pareto']=efficient
    return d.sort_values(['pareto','soh'],ascending=False)
