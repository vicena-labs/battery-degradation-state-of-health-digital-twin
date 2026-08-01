"""Built with Vicena. Minimal Level 0 battery twin example."""
import numpy as np
from battery_twin import simulate_profile
t=np.arange(0,1801); current=np.where(t<900,3.0,np.where(t<1200,0.0,1.5))
r=simulate_profile(t,current)
print(f"Final SOC: {r.soc.iloc[-1]:.3f}")
print(f"Minimum voltage: {r.voltage_v.min():.3f} V")
print(f"Maximum temperature: {r.temperature_c.max():.2f} C")
