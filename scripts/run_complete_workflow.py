"""Run Level 0, Level 1, uncertainty, sensitivity, and decision screening."""
from pathlib import Path
import json
import numpy as np
from battery_twin import simulate_pack,PackParameters,load_calendar_ageing,fit_evaluate,conformal_evaluate,grouped_bootstrap_metrics,stress_sensitivity,pareto_policies
out=Path('outputs'); out.mkdir(exist_ok=True)
t=np.arange(0,1801,2.0); current=np.where(t<600,8,np.where(t<900,0,5))
pack,_=simulate_pack(t,current,pack=PackParameters(series_cells=12,parallel_cells=2)); pack.to_csv(out/'pack_profile.csv',index=False)
df=load_calendar_ageing(); model,metrics,pred,_,_=fit_evaluate(df); _,conf,intervals=conformal_evaluate(model,df); boot=grouped_bootstrap_metrics(model,df)
intervals.to_csv(out/'conformal_intervals.csv',index=False); stress_sensitivity().to_csv(out/'stress_sensitivity.csv',index=False); pareto_policies().to_csv(out/'pareto_policies.csv',index=False)
report={'level1':metrics,'conformal':conf,'bootstrap':boot,'pack':{'series_cells':12,'parallel_cells':2,'max_temperature_c':float(pack.cell_temperature_max_c.max()),'max_soc_spread':float(pack.soc_spread.max()),'min_cell_voltage_v':float(pack.cell_voltage_min_v.min())}}
(out/'complete_metrics.json').write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
