"""Executable Level 0 electro-thermal and aging reference models."""
from dataclasses import dataclass
import numpy as np
import pandas as pd

@dataclass(frozen=True)
class CellParameters:
    capacity_ah: float = 3.0
    r0_ohm: float = 0.032
    r1_ohm: float = 0.018
    c1_f: float = 2400.0
    mass_kg: float = 0.048
    heat_capacity_j_kgk: float = 900.0
    hA_w_k: float = 0.55
    coulombic_efficiency: float = 0.995

def ocv_from_soc(soc):
    z=np.clip(np.asarray(soc,float),0,1)
    return 3.0 + 1.05*z + 0.12*np.tanh((z-0.12)/0.05) + 0.05*np.tanh((z-0.88)/0.04)

def simulate_profile(time_s,current_a,ambient_c=25.0,soc0=0.95,temp0_c=None,params=CellParameters()):
    t=np.asarray(time_s,float); i=np.asarray(current_a,float)
    if t.ndim!=1 or len(t)!=len(i) or len(t)<2 or np.any(np.diff(t)<=0): raise ValueError('time_s must be strictly increasing and match current_a')
    n=len(t); dt=np.diff(t,prepend=t[0]); dt[0]=dt[1]
    soc=np.empty(n); vrc=np.empty(n); temp=np.empty(n); volt=np.empty(n); heat=np.empty(n)
    soc[0]=soc0; vrc[0]=0; temp[0]=ambient_c if temp0_c is None else temp0_c
    for k in range(n):
        if k:
            soc[k]=np.clip(soc[k-1]-params.coulombic_efficiency*i[k-1]*dt[k]/(3600*params.capacity_ah),0,1)
            tau=params.r1_ohm*params.c1_f
            a=np.exp(-dt[k]/tau); vrc[k]=a*vrc[k-1]+params.r1_ohm*(1-a)*i[k-1]
            q=i[k-1]**2*params.r0_ohm + abs(i[k-1]*vrc[k-1])
            temp[k]=temp[k-1]+dt[k]*(q-params.hA_w_k*(temp[k-1]-ambient_c))/(params.mass_kg*params.heat_capacity_j_kgk)
        volt[k]=ocv_from_soc(soc[k])-i[k]*params.r0_ohm-vrc[k]
        heat[k]=i[k]**2*params.r0_ohm+abs(i[k]*vrc[k])
    return pd.DataFrame({'time_s':t,'current_a':i,'soc':soc,'voltage_v':volt,'temperature_c':temp,'heat_w':heat})

def synthetic_aging(days,temperature_c=25,soc=0.5,efc_per_day=0.5):
    d=np.asarray(days,float); arr=np.exp(28000/8.314*(1/298.15-1/(temperature_c+273.15)))
    calendar=0.00075*arr*(0.45+soc)*np.sqrt(np.maximum(d,0)); cycling=0.000035*(efc_per_day*d)**0.72
    soh=np.clip(1-calendar-cycling,0,1)
    resistance_ratio=1+0.65*(1-soh)
    return pd.DataFrame({'days':d,'soh':soh,'capacity_fade':1-soh,'resistance_ratio':resistance_ratio})
