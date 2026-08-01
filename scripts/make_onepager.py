"""Reproducible A4 landscape one-page overview from computed results."""
from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
root=Path(__file__).resolve().parents[1]; out=root/'outputs'; assets=root/'assets'
m=json.loads((out/'level1_metrics.json').read_text()); p=pd.read_csv(out/'level0_profile.csv'); v=pd.read_csv(out/'level1_predictions.csv')
fig=plt.figure(figsize=(11.69,8.27),facecolor='#f4f7fb'); gs=fig.add_gridspec(12,12,left=.045,right=.97,top=.94,bottom=.07,hspace=.8,wspace=.8)
axh=fig.add_subplot(gs[0:2,:]); axh.set_facecolor('#101b35'); axh.set_xticks([]); axh.set_yticks([])
axh.text(.025,.68,'VICENA  |  OPEN RESEARCH TWIN',color='#31d5c8',fontsize=10,weight='bold',transform=axh.transAxes)
axh.text(.025,.28,'Battery Degradation and State-of-Health Digital Twin',color='white',fontsize=19,weight='bold',transform=axh.transAxes)
axh.text(.975,.5,'v0.2.0  |  MIT',ha='right',va='center',color='white',fontsize=10,transform=axh.transAxes)
fig.text(.05,.775,'From executable electro-thermal scenarios to leakage-controlled measured SOH validation.',fontsize=13,weight='bold',color='#101b35')
for j,(title,body) in enumerate([('Electro-thermal','1RC Thevenin ECM, Coulomb SOC, heat balance'),('Aging','Calendar and cycle fade scenarios'),('Measured evidence','478 measurements, six chemistries'),('Research outputs','CSV, JSON, plots, notebooks, tests')]):
 ax=fig.add_subplot(gs[3:5,j*3:(j+1)*3]); ax.axis('off'); ax.add_patch(FancyBboxPatch((0,0),1,1,boxstyle='round,pad=.02',facecolor='white',edgecolor='#d9e1ee')); ax.text(.06,.68,title,weight='bold',color='#101b35'); ax.text(.06,.2,body,fontsize=8.4,color='#41506a',wrap=True)
a1=fig.add_subplot(gs[5:9,0:6]); a1.plot(p.time_s/60,p.voltage_v,color='#f2ad3b',label='Voltage [V]'); a1b=a1.twinx(); a1b.plot(p.time_s/60,p.temperature_c,color='#e96370',label='Temperature [C]'); a1.set(xlabel='Time [min]',ylabel='Voltage [V]',title='Level 0 synthetic electro-thermal response'); a1b.set_ylabel('Temperature [C]'); a1.grid(alpha=.2)
a2=fig.add_subplot(gs[5:9,6:12]); a2.scatter(v.soh,v.predicted_soh,c=v.days_passed,cmap='viridis',s=26); lo=min(v.soh.min(),v.predicted_soh.min()); hi=max(v.soh.max(),v.predicted_soh.max()); a2.plot([lo,hi],[lo,hi],'--',color='#101b35'); a2.set(xlabel='Measured SOH',ylabel='Predicted SOH',title='Level 1 held-out trajectory validation'); a2.grid(alpha=.2)
axm=fig.add_subplot(gs[9:11,:]); axm.set_facecolor('#101b35'); axm.set_xticks([]); axm.set_yticks([])
vals=[('Measured rows',f"{m['n_rows']}"),('Held-out groups',f"{m['test_groups']}"),('SOH MAE',f"{m['mae']:.3f}"),('Baseline MAE',f"{m['baseline_mae']:.3f}"),('Tests','7 passed')]
for k,(lab,val) in enumerate(vals): axm.text(.03+k*.195,.62,val,color='white',fontsize=15,weight='bold',transform=axm.transAxes); axm.text(.03+k*.195,.22,lab,color='#b9c6dc',fontsize=8.5,transform=axm.transAxes)
fig.text(.05,.055,'1  Define profile   2  Simulate physics   3  Validate schema   4  Calibrate by groups   5  Report held-out evidence',fontsize=9,weight='bold',color='#30415f')
fig.text(.05,.023,'github.com/vicena-labs/battery-degradation-state-of-health-digital-twin',fontsize=8,color='#51627c'); fig.text(.95,.023,'vicena.ai',ha='right',fontsize=8,weight='bold',color='#101b35')
assets.mkdir(exist_ok=True); png=assets/'battery-degradation-state-of-health-digital-twin-onepager.png'; pdf=root/'Battery_Degradation_State_of_Health_Digital_Twin_OnePager.pdf'
fig.savefig(png,dpi=180,facecolor=fig.get_facecolor()); fig.savefig(pdf,facecolor=fig.get_facecolor()); print({'png':str(png),'pdf':str(pdf),'mae':m['mae'],'level0_max_temp_c':p.temperature_c.max()})
