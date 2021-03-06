[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1318324.svg)](https://doi.org/10.5281/zenodo.1318324)

# olivine

All of the raw data and code used in the 2018 Ferriss et al. submission to *Geochemica et Cosmochemica Acta* on H diffusivity in olivine except the code for the [interactive online Arrhenius diagram](https://arrheniusdiagram.herokuapp.com/arrheniusdiagram), which is [here](https://github.com/EFerriss/arrheniusdiagram/).

Details about the FTIR files can be found in [this table](https://github.com/EFerriss/olivine/blob/master/olivine/Ferriss_Supplement_astable.csv) as well as in the python scripts used to handle them: [Kiki_spectra.py](https://github.com/EFerriss/olivine/blob/master/olivine/KilaueaIki/Kiki_spectra.py) and [SanCarlos_spectra.py](https://github.com/EFerriss/olivine/blob/master/olivine/SanCarlos/SanCarlos_spectra.py). Baselines were created using the python library [pynams v2.1](https://zenodo.org/record/1319766) for [Kilauea Iki](https://github.com/EFerriss/olivine/blob/master/olivine/KilaueaIki/Kiki_baselines.py) and [San Carlos](https://github.com/EFerriss/olivine/blob/master/olivine/SanCarlos/SanCarlos_baselines.py). 

The Monte Carlo simulations were performed with [a MATLAB script](https://github.com/EFerriss/olivine/blob/master/olivine/monte_carlo/olivine_degassing_MCfit_script.m).

Please cite as:  
Elizabeth Ferriss, & Megan Newcombe. (2018, July 23). Data and code for H diffusion in olivine (Version v1.2). Zenodo. http://doi.org/10.5281/zenodo.1318324
