"""Reproduce measured Li-S early-cycle EOL prediction benchmark."""
from pathlib import Path
import json
from battery_twin import load_lis_cycle_capacity,benchmark_rul
out=Path('outputs'); out.mkdir(exist_ok=True)
d=load_lis_cycle_capacity(); result,metrics=benchmark_rul(d,early_cycles=60,threshold=.8)
d.to_csv(out/'lis_cycle_capacity.csv',index=False); result.to_csv(out/'rul_benchmark.csv',index=False); (out/'rul_metrics.json').write_text(json.dumps(metrics,indent=2)); print(json.dumps(metrics,indent=2))
