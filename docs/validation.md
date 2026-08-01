# Validation guide

Part of the [Vicena Research Twins collection](https://vicena.ai).

Acceptance checks are dimensional ranges, monotonic SOC during discharge, positive heat response, monotonic synthetic fade, schema completeness, group-disjoint train and test trajectories, comparison against a mean-SOH baseline, and saved residuals. Current release metrics are MAE 0.0285, RMSE 0.0363, R2 0.644, versus baseline MAE 0.0444 on 27 held-out groups. Recompute metrics after any model, split, or dataset change. For Level 2, validate on independent experiments, sites, equipment, or later campaigns not used for calibration.
