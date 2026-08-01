"""Measured Li-S cycle-aging trajectories and early-cycle RUL benchmarks."""
from pathlib import Path
import numpy as np
import pandas as pd

def load_lis_cycle_capacity(path='datasets/measured/li_s_cycle_aging/VZ1_035_021_CVUT_D_0003_v1.txt'):
    lines=Path(path).read_text(encoding='utf-8-sig').splitlines(); rows=[]; i=0
    while i<len(lines):
        label=lines[i].strip()
        if label and ('oC' in label or 'C/' in label):
            i+=2
            while i<len(lines) and lines[i].strip():
                parts=lines[i].split('\t')
                try: rows.append({'condition':label,'cycle':float(parts[0]),'soh':float(parts[1]),'soh_errorbar':abs(float(parts[2]))})
                except (ValueError,IndexError): break
                i+=1
        i+=1
    d=pd.DataFrame(rows)
    if d.empty or d.condition.nunique()<2: raise ValueError('No cycle-aging condition blocks found')
    if not d.soh.between(0,1.2).all(): raise ValueError('SOH outside accepted parsing range')
    return d

def observed_eol(group,threshold=.8):
    g=group.sort_values('cycle'); below=g[g.soh<=threshold]
    if below.empty:return np.nan
    b=below.iloc[0]; before=g[g.cycle<b.cycle].tail(1)
    if before.empty:return float(b.cycle)
    a=before.iloc[0]; return float(a.cycle+(threshold-a.soh)*(b.cycle-a.cycle)/(b.soh-a.soh))

def forecast_eol(group,early_cycles=60,threshold=.8,method='linear'):
    g=group.sort_values('cycle'); fit=g[g.cycle<=early_cycles]
    if len(fit)<3:return np.nan
    x=fit.cycle.to_numpy(); y=fit.soh.to_numpy()
    if method=='linear':
        slope,intercept=np.polyfit(x,y,1); return float((threshold-intercept)/slope) if slope<0 else np.inf
    if method=='exponential':
        slope,intercept=np.polyfit(x,np.log(np.clip(y,1e-6,None)),1); return float((np.log(threshold)-intercept)/slope) if slope<0 else np.inf
    raise ValueError('method must be linear or exponential')

def benchmark_rul(df,early_cycles=60,threshold=.8):
    rows=[]
    for name,g in df.groupby('condition',sort=False):
        actual=observed_eol(g,threshold)
        for method in ['linear','exponential']:
            pred=forecast_eol(g,early_cycles,threshold,method); rows.append({'condition':name,'method':method,'early_cycles':early_cycles,'threshold_soh':threshold,'observed_eol_cycle':actual,'predicted_eol_cycle':pred,'absolute_error_cycles':abs(pred-actual) if np.isfinite(actual) and np.isfinite(pred) else np.nan,'observed':np.isfinite(actual)})
    r=pd.DataFrame(rows); observed=r.dropna(subset=['absolute_error_cycles'])
    metrics={m:{'n_conditions':int(len(g)),'mae_cycles':float(g.absolute_error_cycles.mean()),'median_ae_cycles':float(g.absolute_error_cycles.median())} for m,g in observed.groupby('method')}
    return r,metrics
