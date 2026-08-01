"""Built with Vicena. Reproduce the Level 1 group-held-out validation."""
from pathlib import Path
import json
from battery_twin import load_calendar_ageing,fit_evaluate
Path('outputs').mkdir(exist_ok=True)
model,metrics,pred,train,test=fit_evaluate(load_calendar_ageing())
pred.to_csv('outputs/level1_predictions.csv',index=False)
Path('outputs/level1_metrics.json').write_text(json.dumps(metrics,indent=2))
print(json.dumps(metrics,indent=2))
