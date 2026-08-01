# Model card

Part of the [Vicena Research Twins collection](https://vicena.ai).

## Level 0

The electrical model is a one-polarization-pair Thevenin equivalent circuit. SOC uses Coulomb counting. Terminal voltage combines a smooth illustrative OCV-SOC function, ohmic drop, and RC polarization. The thermal state uses irreversible electrical heat and a lumped convection loss. Aging uses empirical square-root calendar fade, Arrhenius acceleration, SOC stress, and a sublinear equivalent-full-cycle term. It is a scenario model, not a mechanistic electrochemical degradation model.

## Level 1

A regularized polynomial regression estimates SOH from days, temperature, storage SOC, and chemistry. One-hot chemistry encoding prevents ordinal assumptions. Whole cell-condition trajectories are assigned to either calibration or test. The fixed seed makes the split reproducible.

## Limitations

Parameters are not identified for a named commercial cell. The measured model represents calendar aging only. SOH above 1 can arise from measurement and formation variation and is retained. No pack imbalance, active thermal management, lithium plating, safety events, online filtering, or field telemetry is modeled.
