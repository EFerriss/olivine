# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:04:00 2017

@author: Ferriss

Various calculations used throughout the text on hydrogen diffusion in olivine
"""
from __future__ import print_function, division
import numpy as np
import pynams.experiments as exper
import itertools
from olivine.SanCarlos import SanCarlos_spectra as SC

print()
print('Kohlstedt & Mackwell 1998 experiments at 1000C, 200MPa, NNO, 8hr')
print('"metastable equilibrium" concentration')
exper.convertH(7)
print('final concentration')
exper.convertH(50)

print()
print('At 1000C, according to Mosenfelder et al. 2006')
trueC = exper.solubility_of_H_in_olivine(Celsius=1000, pressure_GPa=1, 
                                 author='Mosenfelder')

print()
print('If final concentration is really', trueC, 'ppm H2O')
print('KM98 metastable equilibrium is', trueC*(7/50), 'ppm H2O')

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

print('range of water concentrations in hydrated SC1-2')
print(mina, 'to', maxa, 'ppm H2O')

wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
wb2.get_baselines()
wb7.get_baselines()
wb2.make_areas()
wb7.make_areas()

areas = []
profidx = itertools.cycle([0, 1, 2])
for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * area2water)
        wb.areas[next(profidx)] = prof.areas
        areas.append(max(prof.areas))
metastable = np.mean([ar for ar in wb2.areas][0])
print('metastable equilibrium in SC1-2', metastable, 'ppm H2O')