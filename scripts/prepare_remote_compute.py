"""Prepare, validate, and hash remote-compute inputs without submitting jobs."""
import json,os,importlib.metadata
from pathlib import Path
from battery_twin import write_compute_examples
write_compute_examples()
try: vc=__import__('vicena_compute'); vc_version=getattr(vc,'__version__','unknown')
except Exception: vc_version='unavailable'
try: rowan_version=importlib.metadata.version('rowan-python')
except Exception: rowan_version='unavailable'
report={'vicena_compute':{'sdk_version':vc_version,'gateway_configured':bool(os.getenv('VICENA_COMPUTE_API_KEY') or os.getenv('VICENA_EXTERNAL_API_KEY')),'workflow':'managed ngspice self-contained simulation','submitted':False},'rowan':{'sdk_version':rowan_version,'gateway_configured':bool(os.getenv('VICENA_EXTERNAL_API_KEY')),'example_workflow':'descriptors for ethylene carbonate','submitted':False},'reason_not_submitted':'Remote jobs can consume credits and require an explicit budget authorization.'}
Path('outputs/remote_compute_preflight.json').write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report,indent=2))
