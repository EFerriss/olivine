# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:04:00 2017

@author: Ferriss

Various calculations used throughout the text on hydrogen diffusion in olivine
"""
from __future__ import print_function, division
import numpy as np
import pynams.experiments as exper
import olivine
from olivine.SanCarlos import SanCarlos_spectra as SC

print()
print('Kohlstedt & Mackwell 1998 experiments at 1000C, 200MPa, NNO, 8hr')
print('"metastable equilibrium" concentration')
exper.convertH(7)
print('final concentration')
exper.convertH(50)

print()
print('At 1000C, according to Mosenfelder et al. 2006')
exper.solubility_of_H_in_olivine(Celsius=1000, pressure_GPa=1, 
                                 author='Mosenfelder')
print()

#%%
area2water = 0.6
wb2 = SC.wb_800C_hyd
wb2.get_baselines()
wb2.make_areas()
waters = np.array([prof.areas for prof in wb2.profiles]) * area2water
water = [w for w in waters]
mina = min([min(prof.areas) for prof in wb2.profiles]) * area2water
maxa = max([max(prof.areas) for prof in wb2.profiles]) * area2water

print()
print('range of water concentrations in hydrated SC1-2')
print(mina, 'to', maxa, 'ppm H2O')
print('average and stdev water')
