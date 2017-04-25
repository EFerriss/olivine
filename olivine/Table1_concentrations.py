# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:13:13 2017

@author: Elizabeth
H diffusion in olivine

Estimate concentrations before and after hydration in San Carlos and 
Kilauea Iki olivine based on baselines created in Kiki_baseline.py and 
SanCarlos_baseline.py
"""
from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
from pynams import pynams
import numpy as np
from uncertainties import ufloat

SC1_untreated = [SC.SC_untreated_Ea, SC.SC_untreated_Eb, SC.SC_untreated_Ec]
SC7_hydrated = SC.spec7
SC2_hydrated = SC.spec2
SC2_dehydrated = SC.SC_final_averaged
SC_list = SC1_untreated + [SC7_hydrated, SC2_hydrated, SC2_dehydrated]
Kiki_list = [kiki.Kiki_init_Ea, kiki.Kiki_init_Eb, kiki.Kiki_init_Ec]

baselines = ['-high-baseline.CSV', '-baseline.CSV', '-low-baseline.CSV']
directions = ['E || [100]', 'E || [010]', 'E || [001]', ]
numf = '{:.0f}'

#%%
print()
print('Kilauea Iki olivine')
kiki_area = ufloat(0, 0)
kiki_Withers = ufloat(0, 0)
kiki_Bell = ufloat(0, 0)
kiki_SIMS = ufloat(14, 1.2)
for idx, spec in enumerate(Kiki_list):
    areas = []
    for baseline in baselines:
        spec.get_baseline(baseline_ending=baseline, print_confirmation=False)
        areas.append(spec.make_area(printout=False))
    spec.area = ufloat(np.mean(areas), np.std(areas))
    print(numf.format(spec.area), 'cm^-2 average area', directions[idx])
    spec.Withers = pynams.area2water(spec.area, phase='olivine',
                                   calibration='Withers')
    spec.Bell = pynams.area2water(spec.area, phase='olivine',
                                  calibration='Bell')
    kiki_area = kiki_area + spec.area
    kiki_Withers = kiki_Withers + spec.Withers
    kiki_Bell = kiki_Bell + spec.Bell
kiki_ave = np.mean([kiki_Withers, kiki_Bell, kiki_SIMS])
kiki_scale = kiki_ave/Kiki_list[0].area
print(numf.format(kiki_area), 'total cm^-2 FTIR area')
print(kiki_Bell, 'ppm H2O with Bell calibration')
print(kiki_Withers, 'ppm H2O with Withers calibration') 
print(kiki_SIMS, 'ppm H2O by nanoSIMS')
print(kiki_ave, 'ppm H2O average initial water concentration')
print(kiki_scale, 'ratio of water in ppm H2O to area in cm^-2 E || [100]')

print()
print('San Carlos olivine')
for spec in SC_list:
    areas = []
    for baseline in baselines:
        spec.get_baseline(baseline_ending=baseline, print_confirmation=False)
        areas.append(spec.make_area(printout=False))
    spec.area = ufloat(np.mean(areas), np.std(areas))
total_initial_area = sum([spec.area for spec in SC1_untreated])
Bell = pynams.area2water(total_initial_area, phase='olivine', 
                         calibration='Bell')
Withers = pynams.area2water(total_initial_area, phase='olivine', 
                            calibration='Withers')
SIMS = ufloat(5, 0.87)
ave_water = np.mean([Withers, Bell, SIMS])
SC_scale = ave_water/SC1_untreated[0].area
SC7_water = SC7_hydrated.area * SC_scale
SC2_water = SC2_hydrated.area * SC_scale
print(numf.format(SC1_untreated[0].area), 'cm^-2 E || [100] untreated SC1-1')
print(numf.format(SC7_hydrated.area), 'cm^-2 E || [100] part hydrated SC1-7')
print(numf.format(SC2_hydrated.area), 'cm^-2 E || [100] part hydrated SC1-2')
print(numf.format(SC2_dehydrated.area), 'cm^-2 E || [100] dehydrated SC1-2')
print(numf.format(SC1_untreated[1].area), 'cm^-2 E || [010] untreated SC1-1')
print(numf.format(SC1_untreated[2].area), 'cm^-2 E || [001] untreated SC1-1')
print(numf.format(total_initial_area), 'cm^-2 total area untreated SC1-1')
print(Bell, 'ppm H2O with Bell calibration SC-1')
print(Withers, 'ppm H2O with Withers calibration SC1-1') 
print(SIMS, 'ppm H2O in dehydrated SC1-2 by nanoSIMS')
print(ave_water, 'ppm H2O average initial water concentration SC1')
print(SC_scale, 'ratio of water in ppm H2O to area in cm^-2 E || [100]')
print(numf.format(SC7_water), 'ppm H2O in partially hydrated SC1-7')
print(numf.format(SC2_water), 'ppm H2O in partially hydrated SC1-2')

