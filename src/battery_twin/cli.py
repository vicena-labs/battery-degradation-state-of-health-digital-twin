import argparse,json
import numpy as np
from .core import simulate_profile
from .validation import load_calendar_ageing,fit_evaluate
def main():
 p=argparse.ArgumentParser(); p.add_argument('command',choices=['simulate','validate']); p.add_argument('--output',default='outputs/result.csv'); a=p.parse_args()
 if a.command=='simulate':
  t=np.arange(0,1801,1); i=np.where(t<900,3.0,np.where(t<1200,0,1.5)); d=simulate_profile(t,i); d.to_csv(a.output,index=False); print({'final_soc':round(d.soc.iloc[-1],4),'min_voltage_v':round(d.voltage_v.min(),4),'max_temperature_c':round(d.temperature_c.max(),3),'output':a.output})
 else:
  _,m,r,_,_=fit_evaluate(load_calendar_ageing()); r.to_csv(a.output,index=False); print(json.dumps(m,indent=2))
if __name__=='__main__': main()
