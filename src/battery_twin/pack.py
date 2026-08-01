"""Pack-level aggregation, imbalance, and passive cooling reference models."""
from dataclasses import dataclass
import numpy as np
import pandas as pd
from .core import CellParameters, simulate_profile

@dataclass(frozen=True)
class PackParameters:
    series_cells: int = 12
    parallel_cells: int = 2
    capacity_cv: float = 0.025
    resistance_cv: float = 0.08
    initial_soc_std: float = 0.012

def simulate_pack(time_s, pack_current_a, ambient_c=25.0, seed=7, cell=CellParameters(), pack=PackParameters()):
    if pack.series_cells < 1 or pack.parallel_cells < 1: raise ValueError('Pack topology must be positive')
    rng=np.random.default_rng(seed); n=pack.series_cells*pack.parallel_cells
    cap=np.clip(rng.normal(cell.capacity_ah,cell.capacity_ah*pack.capacity_cv,n),.5*cell.capacity_ah,1.5*cell.capacity_ah)
    r0=np.clip(rng.normal(cell.r0_ohm,cell.r0_ohm*pack.resistance_cv,n),.25*cell.r0_ohm,3*cell.r0_ohm)
    soc0=np.clip(rng.normal(.95,pack.initial_soc_std,n),0,1); cell_current=np.asarray(pack_current_a)/pack.parallel_cells
    traces=[]
    for k in range(n):
        cp=CellParameters(capacity_ah=cap[k],r0_ohm=r0[k],r1_ohm=cell.r1_ohm,c1_f=cell.c1_f,mass_kg=cell.mass_kg,heat_capacity_j_kgk=cell.heat_capacity_j_kgk,hA_w_k=cell.hA_w_k,coulombic_efficiency=cell.coulombic_efficiency)
        x=simulate_profile(time_s,cell_current,ambient_c,soc0[k],params=cp); x['cell']=k; traces.append(x)
    z=pd.concat(traces,ignore_index=True); g=z.groupby('time_s')
    summary=g.agg(cell_voltage_min_v=('voltage_v','min'),cell_voltage_mean_v=('voltage_v','mean'),cell_voltage_max_v=('voltage_v','max'),cell_temperature_max_c=('temperature_c','max'),soc_min=('soc','min'),soc_max=('soc','max')).reset_index()
    summary['pack_voltage_v']=summary.cell_voltage_mean_v*pack.series_cells
    summary['pack_power_w']=summary.pack_voltage_v*np.asarray(pack_current_a)
    summary['soc_spread']=summary.soc_max-summary.soc_min
    return summary,z
