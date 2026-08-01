# Model card

Part of the [Vicena Research Twins collection](https://vicena.ai).

## Level 0

The electrical model is a one-polarization-pair Thevenin equivalent circuit. SOC uses Coulomb counting. Terminal voltage combines a smooth illustrative OCV-SOC function, ohmic drop, and RC polarization. The thermal state uses irreversible electrical heat and a lumped convection loss. Aging uses empirical square-root calendar fade, Arrhenius acceleration, SOC stress, and a sublinear equivalent-full-cycle term. It is a scenario model, not a mechanistic electrochemical degradation model.

## Level 1

A regularized polynomial regression estimates SOH from days, temperature, storage SOC, and chemistry. One-hot chemistry encoding prevents ordinal assumptions. Whole cell-condition trajectories are assigned to either calibration or test. The fixed seed makes the split reproducible.

## Limitations

Parameters are not identified for a named commercial cell. The measured model represents calendar aging only. SOH above 1 can arise from measurement and formation variation and is retained. No pack imbalance, active thermal management, lithium plating, safety events, online filtering, or field telemetry is modeled.

## Pack and uncertainty extensions in v0.2.0

The pack layer applies seeded cell-to-cell capacity, resistance, and initial-SOC variation and aggregates parallel current and series voltage. It supports sensitivity and algorithm testing but is not calibrated. Split-conformal intervals use a separate group-disjoint calibration subset, and bootstrap resampling occurs at the cell-condition trajectory level rather than the row level. Coverage is empirical and conditional on the dataset scope.

The decision layer enumerates temperature, storage SOC, and daily throughput scenarios using the synthetic aging law. Pareto labels therefore support experimental prioritization only.
