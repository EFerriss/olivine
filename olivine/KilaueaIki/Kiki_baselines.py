#-*- coding: utf-8 -*-
"""
Created on Fri Dec 09 14:24:39 2016

@author: Ferriss

Make and save Kilauea Iki olivine baselines
"""

from __future__ import division, print_function
from olivine.KilaueaIki import Kiki_spectra as kiki
from pynams import styles
import olivine

thisfolder = kiki.thisfolder
high_ending = olivine.high_ending
low_ending = olivine.low_ending

#%% Range of 3 baselines for initial concentration estimates
spec = kiki.Kiki_init_Ea
spec.make_baseline(curvature=0.05, abs_smear_high=10)
spec.save_baseline()
spec.make_baseline(abs_smear_high=10, wn_low=3300, force_through_wn=3400)
spec.save_baseline(baseline_ending=high_ending)
spec.make_baseline(curvature=0.1, abs_smear_high=10, wn_low=3100)
spec.save_baseline(baseline_ending=low_ending)

spec = kiki.Kiki_init_Eb
spec.make_baseline(curvature=0.07, abs_smear_high=10, wn_low=3150)
spec.save_baseline()
spec.make_baseline(force_through_wn=3400, wn_low=3150, abs_smear_high=10)
spec.save_baseline(baseline_ending=high_ending)
spec.make_baseline(curvature=0.11, abs_smear_high=10, wn_low=3100)
spec.save_baseline(baseline_ending=low_ending)

spec = kiki.Kiki_init_Ec
spec.make_baseline(curvature=0.05, abs_smear_high=10, wn_low=3150)
spec.save_baseline()
spec.make_baseline(force_through_wn=3450, wn_low=3150, abs_smear_high=10)
spec.save_baseline(baseline_ending=high_ending)
spec.make_baseline(curvature=0.08, abs_smear_high=10, wn_low=3100)
spec.save_baseline(baseline_ending=low_ending)

#%% three sets of baselines for each spectrum
baseline = {'curvature':0.05, 'abs_smear_high':10, 
            'wn_low':3150, 'abs_smear_low':10}
baselinelow = {'curvature':0.085, 'abs_smear_high':10, 
               'wn_low':3150, 'abs_smear_low':10}
baselinehigh = {'abs_smear_high':10, 'wn_low':3400, 'abs_smear_low':10}

wb_list = [
           kiki.wb_Kiki_init, 
           kiki.wb_Kiki_1hr, 
           kiki.wb_Kiki_8hr,
           kiki.wb_Kiki_1000C_3hr, 
           kiki.wb_Kiki_1000C_6hr, 
           kiki.wb_Kiki_1000C_7hr,
           kiki.wb_Kiki_ox
           ]

for wb in wb_list:
    wb.make_baselines(**baseline)
    wb.save_baselines()
    wb.make_baselines(**baselinehigh)
    wb.save_baselines(baseline_ending=high_ending)
    wb.make_baselines(**baselinelow)
    wb.save_baselines(baseline_ending=low_ending)

#%
#spec = kiki.wb_Kiki_1000C_7hr.profiles[0].spectra[8]
#spec.get_baseline(baseline_ending=low_ending)
#fig, ax = spec.plot_showbaseline()
#fig.savefig('test.jpg', format='jpg')

#%% Kiki weirdos that use the low ending baseline
specs = kiki.wb_Kiki_1hr.profiles[2].spectra + \
        kiki.wb_Kiki_8hr.profiles[0].spectra + \
        kiki.wb_Kiki_8hr.profiles[2].spectra + \
        kiki.wb_Kiki_1000C_3hr.profiles[0].spectra + \
        kiki.wb_Kiki_1000C_6hr.profiles[0].spectra + \
        kiki.wb_Kiki_1000C_7hr.profiles[0].spectra + \
        kiki.wb_Kiki_1000C_7hr.profiles[2].spectra + \
        kiki.wb_Kiki_1000C_8hr.profiles[0].spectra

for spec in specs:
    spec.get_baseline(baseline_ending=low_ending)
    spec.save_baseline()
