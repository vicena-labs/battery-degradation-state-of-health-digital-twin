____________________Dataset for "Experimental Study on Cycle Aging of 3.4 Ah Lithium-Sulfur Pouch Cells: Temperature and Current Investigation"____________________

Last updated: 2025-07-22

______Contact______
* Dominika Capkova
* ORCID: 0000-0002-3614-5629
* Department of Electrical and Electronic Technology, Faculty of Electrical Engineering and Communication, Brno University of Technology + Department of Chemical Sciences and Bernal Institute, University of Limerick
* 616 00, Brno, Czech Republic + Limerick, V94 T9PX, Ireland

______Principal Investigator______
* Karel Bouzek
* ORCID: 0000-0002-0394-0634
* Dept. of Inorganic Technology, Faculty of Chemical Technology, University of Chemistry and Technology, Prague
* Technicka 5, 166 28, Prague 6, Czech Republic

______Data manager or custodian______
* Michal Carda
* ORCID: 0000-0002-3061-3751
* Dept. of Inorganic Technology. Faculty of Chemical Technology, University of chemistry and Technology, Prague
* Technicka 5, 166 28, Prague 6, Czech Republic

______License______
*Dataset for Experimental Study on Cycle Aging of 3.4 Ah Lithium-Sulfur Pouch Cells: Temperature and Current Investigation © 2025 by Dominika Capkova is licensed under CC BY
*license information: https://creativecommons.org/licenses/by/4.0/

------------------------------------------------------------------------------------------------

______About the dataset______
Underlying data supporting the figures, graphs, and pictures in the article.
Figure 1: Measured voltages and times during a cycling and reference performance test (RPT).
Figure 2: Experimentally measured and fitted real and imaginary impedances.
Figure 3: Total capacity, high voltage plateau capacity, low voltage plateau capacity and Coulombic efficiency values obtained directly or computed from the RPTs.
Figure 4: Measured voltage and capacity for the example charging curve, together with computed dV/dQ signal.
Figure 5: DV peak positions, heights, widths, and shuttle current data.
Figure 6: Obtained resistance values for 10% and 70% DOD.
Figure 7: Resistance values obtained from EIS analysis for 10% and 70% DOD for cases aged at different temperatures.
Figure 8: Resistance values obtained from EIS analysis for 10% and 70% DOD for cases aged at different charging/discharged currents.

______Methods of data collection______
Cycling and reference performance test (RPT) data were measured on the Digatron BTS 600 battery tester. Electrochemical impedance spectroscopy (EIS) data were measured on the Fuelcon Evaluator Battery test station. For processing the EIS data, MATLAB software with the ‘Zfit’ function was used to fit the electrical circuit parameters. Differential voltage (DV) peaks were obtained from the measured voltage and capacity measurement data, which were denoised by the Savitzky-Golay filter (3rd order and 21 sample window for voltage, 1st order and 101 sample window for capacity) and moving average (with windows of 3 samples and 2 samples for voltage and capacity, respectively), by applying ‘peakfit’ function in MATLAB.


______Methods of data processing______
The dataset contains only raw data, therefore no processing is described.

------------------------------------------------------------------------------------------------

______File name structure_____
* VZx_000_111_XXXXX_Y_0000_v1
     VZx – research proposal (3 characters)
     000 – order of the publication in the research proposal (3 char.)
     111 – last 3 numerals of the superior indicator (3 char.)
     XXXXX – institution abbreviation (max. 5 char.)
          VSCHT - University of chemistry and technology, Prague
          CVUT - Czech Technical University
          UFCH - Institute of Physical Chemistry, Czech Academy of Sciences
          UK - Charles University
          VUT - Brno University of Technology
     Y – file type (1 char.):
          M – manuscript
          D – data
          S – supplementary information
          P – published version of the article
     0000 – order of the files in the dataset (4 char.)
     v1 – versioning (v + version number)

* example: VZ1_001_023_VSCHT_D_0001_v1.csv
    

______File formats______
* Text documents 

______Date formats______
* YYYY-MM-DD
* HH-MM-SS 24hr format

______Units and abbreviations______
* Time [hours]	Voltage [V]	Time [hours]	Voltage [V]
* Voltage [V]	Capacity [-]	dQ/dV [V/Ah]


------------------------------------------------------------------------------------------------
______List of files______
* VZ1_035_021_CVUT_D_0001_v1.txt
* VZ1_035_021_CVUT_D_0002_v1.txt
* VZ1_035_021_CVUT_D_0003_v1.txt
* VZ1_035_021_CVUT_D_0004_v1.txt
* VZ1_035_021_CVUT_D_0005_v1.txt - peaks
* VZ1_035_021_CVUT_D_0006_v1.txt - shuttle
* VZ1_035_021_CVUT_D_0007_v1.txt
* VZ1_035_021_CVUT_D_0008_v1.txt - EIS_R_T_data
* VZ1_035_021_CVUT_D_0009_v1.txt - IS_R_T_data