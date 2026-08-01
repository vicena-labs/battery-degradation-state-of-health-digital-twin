# Data sources and boundaries

## Bundled Level 1 calendar-aging data

Source: Experimental Calendar Ageing Data for Lithium-Ion Battery Chemistries, Zenodo DOI https://doi.org/10.5281/zenodo.6685365. Downloaded 2026-08-01. Archive SHA256: `327ab07a89b3eb68ef422817f4bd75f50ab6fed399d458381c3b9f1d984fe155`. The six CSV files are redistributed here to make the published validation reproducible. Users must review the Zenodo record and cite the dataset.

## Archived future-extension data

LiBforSecUse life-cycle and impedance data, Zenodo DOI https://doi.org/10.5281/zenodo.6418665. MAT archive SHA256: `1090f5fca4cd8d5d07a58c14b1ab6cd91449a5d7a4f1606b0a9218bb813d13df`. This release does not claim validation from that MAT file because its MATLAB table serialization is not consumed by the current Python loader. It is retained as a provenance-verified input for a future impedance-to-SOH extension.

## Li-S cycle-aging and early-cycle RUL benchmark

Source: Dataset for Experimental Study on Cycle Aging of 3.4 Ah Lithium-Sulfur Pouch Cells: Temperature and Current Investigation, Zenodo DOI https://doi.org/10.5281/zenodo.16527416. The dataset README states CC BY 4.0. Downloaded 2026-08-01 using official Zenodo content URLs. File-level checksums are stored in `datasets/measured/li_s_cycle_aging/SHA256SUMS`. The current parser uses file `VZ1_035_021_CVUT_D_0003_v1.txt`, containing condition-level mean normalized capacity, error bars, and cycle values. It does not provide physical cell identities for the summarized curves.
