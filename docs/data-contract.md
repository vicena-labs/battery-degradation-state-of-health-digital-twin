# Data contract

Part of the [Vicena Research Twins collection](https://vicena.ai).

Each measured record requires storage SOC in percent, temperature in degC, physical cell identity, elapsed days, discharge capacity in Ah, and charge capacity in Ah. The physical cell identity plus chemistry, SOC, and temperature defines a trajectory. A trajectory must belong to exactly one of training, calibration, or test. Missing units, cell IDs, or test conditions are blockers. Use `battery_twin.validate_csv` or the schema under `schemas/` before analysis.
