"""Safe preparation helpers for Vicena Compute and Rowan remote workflows.

These functions create inspectable inputs only. They never submit paid jobs.
"""
from pathlib import Path
import hashlib,json

EC_SMILES='O=C1OCO1'

def battery_ecm_ngspice_netlist(r0_ohm=.032,r1_ohm=.018,c1_f=2400.0,pulse_a=3.0,duration_s=180.0):
    vals=[r0_ohm,r1_ohm,c1_f,pulse_a,duration_s]
    if any(float(x)<=0 for x in vals): raise ValueError('All ECM and pulse values must be positive')
    step=max(duration_s/600,1e-4); at=min(duration_s*.5,60.0)
    return f'''Battery 1RC Thevenin pulse response, illustrative parameters
V_OCV ocv 0 3.70
I_LOAD out 0 PULSE(0 {pulse_a} 1m 1u 1u {duration_s/2} {duration_s})
R0 ocv n1 {r0_ohm}
R1 n1 out {r1_ohm}
C1 n1 out {c1_f}
.tran {step} {duration_s}
.print tran time v(out) v(n1)
.measure tran v_terminal_mid FIND v(out) AT={at}
.measure tran v_terminal_min MIN v(out)
.end
'''

def vicena_compute_sidecar(title='Battery ECM transient',**kwargs):
    net=battery_ecm_ngspice_netlist(**kwargs)
    return [{'attempt':1,'title':title,'inputs':{'netlist':net},'limits':{'cpu_cores':1,'memory_mib':1024,'wall_seconds':120}}]

def rowan_electrolyte_request(smiles=EC_SMILES,workflow='descriptors',max_vicena_credits=100):
    if not smiles or not isinstance(smiles,str): raise ValueError('SMILES is required')
    if workflow not in {'descriptors','solubility','conformer_search','basic_calculation'}: raise ValueError('Unsupported documented example workflow')
    if max_vicena_credits<=0: raise ValueError('Budget cap must be positive')
    payload={'provider':'rowan','workflow':workflow,'initial_smiles':smiles,'name':'battery-electrolyte-screen','max_vicena_credits':int(max_vicena_credits),'submission':'requires explicit user authorization'}
    payload['task_key']=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
    return payload

def write_compute_examples(root='compute'):
    root=Path(root); (root/'vicena_compute').mkdir(parents=True,exist_ok=True); (root/'rowan').mkdir(parents=True,exist_ok=True)
    (root/'vicena_compute'/'vicena_compute_workflow_inputs.example.json').write_text(json.dumps(vicena_compute_sidecar(),indent=2)+'\n')
    (root/'vicena_compute'/'battery_ecm.cir').write_text(battery_ecm_ngspice_netlist())
    (root/'rowan'/'electrolyte_request.example.json').write_text(json.dumps(rowan_electrolyte_request(),indent=2)+'\n')
