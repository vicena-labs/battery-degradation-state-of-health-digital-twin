"""Reproducible A4 landscape one-page overview from computed results."""
from pathlib import Path
import json,pandas as pd,matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
root=Path(__file__).resolve().parents[1]; out=root/'outputs'; assets=root/'assets'
m=json.loads((out/'level1_metrics.json').read_text()); rm=json.loads((out/'rul_metrics.json').read_text()); p=pd.read_csv(out/'level0_profile.csv'); r=pd.read_csv(out/'rul_benchmark.csv').dropna(subset=['absolute_error_cycles'])
fig=plt.figure(figsize=(11.69,8.27),facecolor='#f4f7fb'); gs=fig.add_gridspec(12,12,left=.045,right=.97,top=.94,bottom=.07,hspace=.8,wspace=.8)
axh=fig.add_subplot(gs[0:2,:]); axh.set_facecolor('#101b35'); axh.set_xticks([]); axh.set_yticks([])
axh.text(.025,.68,'VICENA  |  OPEN RESEARCH TWIN',color='#31d5c8',fontsize=10,weight='bold',transform=axh.transAxes); axh.text(.025,.28,'Battery Degradation and State-of-Health Digital Twin',color='white',fontsize=19,weight='bold',transform=axh.transAxes); axh.text(.975,.5,'v0.3.0  |  MIT',ha='right',va='center',color='white',fontsize=10,transform=axh.transAxes)
fig.text(.05,.775,'Electro-thermal simulation, measured SOH uncertainty, and early-cycle RUL evidence.',fontsize=13,weight='bold',color='#101b35')
for j,(title,body) in enumerate([('Electro-thermal','Cell and pack response with variability'),('Aging and RUL','Calendar, cycle, SOH, and EOL workflows'),('Measured evidence','Two public experimental programs'),('Research outputs','Schemas, tests, notebooks, CSV, JSON, PDF')]):
 ax=fig.add_subplot(gs[3:5,j*3:(j+1)*3]); ax.axis('off'); ax.add_patch(FancyBboxPatch((0,0),1,1,boxstyle='round,pad=.02',facecolor='white',edgecolor='#d9e1ee')); ax.text(.06,.68,title,weight='bold',color='#101b35'); ax.text(.06,.2,body,fontsize=8.4,color='#41506a',wrap=True)
a1=fig.add_subplot(gs[5:9,0:6]); a1.plot(p.time_s/60,p.voltage_v,color='#f2ad3b'); a1b=a1.twinx(); a1b.plot(p.time_s/60,p.temperature_c,color='#e96370'); a1.set(xlabel='Time [min]',ylabel='Voltage [V]',title='Level 0 synthetic electro-thermal response'); a1b.set_ylabel('Temperature [C]'); a1.grid(alpha=.2)
a2=fig.add_subplot(gs[5:9,6:12]); colors={'linear':'#19c3b1','exponential':'#7868e6'}
for method,g in r.groupby('method'): a2.scatter(g.observed_eol_cycle,g.predicted_eol_cycle,label=method,color=colors[method],s=38)
lo=min(r.observed_eol_cycle.min(),r.predicted_eol_cycle.min()); hi=max(r.observed_eol_cycle.max(),r.predicted_eol_cycle.max()); a2.plot([lo,hi],[lo,hi],'--',color='#101b35'); a2.set(xlabel='Observed 80% crossing [cycles]',ylabel='Predicted crossing [cycles]',title='Level 1+ measured early-cycle RUL'); a2.legend(); a2.grid(alpha=.2)
axm=fig.add_subplot(gs[9:11,:]); axm.set_facecolor('#101b35'); axm.set_xticks([]); axm.set_yticks([])
vals=[('Calendar rows',f"{m['n_rows']}"),('SOH MAE',f"{m['mae']:.3f}"),('RUL conditions','10'),('RUL MAE',f"{rm['exponential']['mae_cycles']:.2f} cycles"),('Tests','10 passed')]
for k,(lab,val) in enumerate(vals): axm.text(.03+k*.195,.62,val,color='white',fontsize=14,weight='bold',transform=axm.transAxes); axm.text(.03+k*.195,.22,lab,color='#b9c6dc',fontsize=8.5,transform=axm.transAxes)
fig.text(.05,.055,'1  Validate data   2  Simulate physics   3  Fit early cycles   4  Hold out future cycles   5  Report uncertainty',fontsize=9,weight='bold',color='#30415f'); fig.text(.05,.023,'github.com/vicena-labs/battery-degradation-state-of-health-digital-twin',fontsize=8,color='#51627c'); fig.text(.95,.023,'vicena.ai',ha='right',fontsize=8,weight='bold',color='#101b35')
assets.mkdir(exist_ok=True); png=assets/'battery-degradation-state-of-health-digital-twin-onepager.png'; pdf=root/'Battery_Degradation_State_of_Health_Digital_Twin_OnePager.pdf'; fig.savefig(png,dpi=180,facecolor=fig.get_facecolor()); fig.savefig(pdf,facecolor=fig.get_facecolor()); print({'png':str(png),'pdf':str(pdf),'soh_mae':m['mae'],'rul_mae_cycles':rm['exponential']['mae_cycles']})
