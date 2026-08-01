# Cycle-aging and RUL validation

Part of the [Vicena Research Twins collection](https://vicena.ai).

The v0.3.0 benchmark reads ten published Li-S condition trajectories containing normalized mean capacity versus cycle. EOL is defined as the interpolated crossing of 0.80 normalized capacity. Linear and exponential models use only points through cycle 60. Their predictions are compared with crossings observed later in the same condition trajectory.

Exponential MAE is 9.26 cycles and median absolute error is 7.70 cycles across ten conditions. Linear MAE is 10.28 cycles and median absolute error is 8.28 cycles. These values are calculated from condition-level means. They do not quantify individual-cell RUL error, conventional lithium-ion performance, or cross-campaign generalization.

This lane is temporally held out and based on a second public experimental program. It is described as Level 1+ evidence, not Level 2, because the early-cycle fit and future evaluation belong to the same condition trajectory and the files lack separate physical-cell identifiers.
