"""Deterministic validation for uploaded calendar-aging CSV files."""
import json
from pathlib import Path
import pandas as pd
REQ={'State-of-Charge':'%','Temperature':'degC','Cell Identity Number':'identifier','Days Passed':'days','Discharge Capacity':'Ah','Charge Capacity':'Ah'}
def validate_csv(path):
    d=pd.read_csv(path); missing=[x for x in REQ if x not in d.columns]; errors=[]
    if missing: errors.append('Missing columns: '+', '.join(missing))
    if not missing:
        if d[list(REQ)].isna().any().any(): errors.append('Missing values in required columns')
        if (d['Days Passed']<0).any(): errors.append('Days Passed must be nonnegative')
        if not d['State-of-Charge'].between(0,100).all(): errors.append('State-of-Charge must be percent in [0,100]')
        if (d[['Discharge Capacity','Charge Capacity']]<=0).any().any(): errors.append('Capacities must be positive Ah')
        dup=d.duplicated(['State-of-Charge','Temperature','Cell Identity Number','Days Passed']).sum()
        if dup: errors.append(f'{dup} duplicate trajectory-time records')
    return {'valid':not errors,'path':str(path),'rows':len(d),'units':REQ,'errors':errors}
def write_report(path,output):
    r=validate_csv(path); Path(output).write_text(json.dumps(r,indent=2)); return r
