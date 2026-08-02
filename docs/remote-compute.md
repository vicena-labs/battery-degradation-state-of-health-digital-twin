# Vicena Compute and Rowan

Part of the [Vicena Research Twins collection](https://vicena.ai).

Vicena Compute runs registered engineering simulation workflows. This repository prepares a self-contained 1RC battery equivalent-circuit transient for managed ngspice. Rowan is the molecular-modeling route. This repository prepares an ethylene-carbonate descriptor request and documents upgrade paths to solubility, conformer search, or bounded quantum calculations.

These surfaces answer different questions. Ngspice evaluates circuit behavior. Rowan evaluates molecular structures and properties. Neither alone validates a battery cell, pack, electrolyte formulation, degradation mechanism, or safe operating envelope.

Run `python scripts/prepare_remote_compute.py` to verify SDK imports and gateway presence and write inspectable examples under `compute/`. It never submits a paid job.

For Vicena Compute, use the managed self-contained ngspice workflow. The generated netlist contains `.tran`, `.print`, and `.measure`, with one CPU, 1024 MiB, and 120 seconds. Submit only through Vicena's trusted runner and save the Vicena job ID and Workspace output folder.

For Rowan, review the molecule, workflow, and credit cap in `compute/rowan/electrolyte_request.example.json`. Use Vicena's trusted Rowan runner and persist the workflow UUID in `rowan_workflows.json`. The example cap is 100 Vicena computation credits, but no submission was made in this release.

For every remote result record provider, SDK and engine version, normalized input, budget cap, job ID, status, timestamps, units, artifact checksums, warnings, validation comparison, and claim boundary.
