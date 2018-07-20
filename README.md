# olivine

All of the raw data and code used in Ferriss et al. submission to *Gechemica et Cosmochemica Acta* on H diffusivity in olivine except the code for the [interactive online Arrhenius diagram](https://arrheniusdiagram.herokuapp.com/arrheniusdiagram), which is [here](https://github.com/EFerriss/arrheniusdiagram/).

Details about the FTIR files can be found in [this table](https://github.com/EFerriss/olivine/blob/master/olivine/Ferriss_Supplement_astable.csv) as well as in the python scripts Kiki_spectra.py in the KilaueaIki folder and SanCarlos_spectra.py in the SanCarlos folder. 

All of the python code written was in Python 3 and in most cases requires [pynams v0.2.0](https://zenodo.org/record/1172001#.WoG_rudOlPY). The Monte Carlo simulations were performed in MATLAB, and relevant files are available in the monte_carlo folder.

The main MATLAB script for running the Monte Carlo simulations is olivine_degassing_MCfit_script.m in the monte_carlo folder.
