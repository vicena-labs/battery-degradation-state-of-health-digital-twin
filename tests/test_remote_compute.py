import json
import pytest
from battery_twin import battery_ecm_ngspice_netlist,vicena_compute_sidecar,rowan_electrolyte_request

def test_ngspice_input_has_batch_evidence():
 n=battery_ecm_ngspice_netlist(); assert '.tran' in n and '.print' in n and '.measure' in n and 'R0' in n and 'C1' in n

def test_vicena_sidecar_limits():
 x=vicena_compute_sidecar()[0]; assert x['limits']=={'cpu_cores':1,'memory_mib':1024,'wall_seconds':120}; assert x['attempt']==1

def test_rowan_request_is_bounded_and_idempotent():
 a=rowan_electrolyte_request(); b=rowan_electrolyte_request(); assert a['task_key']==b['task_key']; assert a['max_vicena_credits']==100; assert a['submission'].startswith('requires')

def test_remote_inputs_reject_invalid():
 with pytest.raises(ValueError): battery_ecm_ngspice_netlist(r0_ohm=0)
 with pytest.raises(ValueError): rowan_electrolyte_request(workflow='docking')
