# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:04:00 2017

@author: Ferriss

Various calculations used throughout the text on hydrogen diffusion in olivine
"""
from __future__ import print_function, division
import numpy as np
import pynams.experiments as exper
from pynams import dlib
import itertools
from uncertainties import ufloat
from olivine.SanCarlos import SanCarlos_spectra as SC

#%%
D3 = dlib.KM98_slow.whatIsD(1000, printout=False) # pv mechanism diffusivities
trueC = exper.solubility_of_H_in_olivine(Celsius=1000, pressure_GPa=1, 
                                 author='Mosenfelder', printout=False)
peaks = SC.peaks
conversion_factor_area2water = 0.6 # see Table1_concentrations.py
wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
wb2.get_baselines()
wb7.get_baselines()
wb2.make_areas()
wb7.make_areas()

profidx = itertools.cycle([0, 1, 2])
for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
        wb.areas[next(profidx)] = prof.areas

wb2mean = np.mean(list(itertools.chain(*wb2.areas)))
wb2stdev = np.std(list(itertools.chain(*wb2.areas)))
wb7mean = np.mean(list(itertools.chain(*wb7.areas)))
wb7stdev = np.std(list(itertools.chain(*wb7.areas)))
wb2area = ufloat(wb2mean, wb2stdev)
wb7area = ufloat(wb7mean, wb7stdev)

metastable = wb2mean
wb7.D3, wb7.init, wb7.fin = wb7.fitD(peak_idx=None, init=metastable,
                                     fin=trueC, show_plot=False,
                                     wholeblock_data=False,
                                     log10Ds_m2s=D3, 
                                     vary_diffusivities=[False, False, True])
wb7.D3a, wb7.inita, wb7.fina = wb7.fitD(peak_idx=None, init=metastable,
                                     fin=trueC, show_plot=False,
                                     wholeblock_data=False,
                                     log10Ds_m2s=D3, 
                                     vary_diffusivities=[True, False, False])
maxarea = max([max(areas) for areas in wb7.areas])
scale_final = trueC / maxarea # to scale up final value to true solubility
wb7.peak_D3 = [[]]*4
wb7.peak_D3a = [[]]*4
for idx in range(4):
    peak_heights7 = [profile.peak_heights[idx] for profile in wb7.profiles]
    peak_heights2 = [profile.peak_heights[idx] for profile in wb2.profiles]
    maxy = max([max(heights) for heights in peak_heights7])
    meta = np.mean(list(itertools.chain(*peak_heights2)))
    wb7.peak_D3[idx], init, fin = wb7.fitD(peak_idx=idx, show_plot=False,
                                       heights_instead=True, 
                                       wholeblock_data=False,
                                       init=meta, 
                                       fin=maxy*scale_final,
                                       log10Ds_m2s=D3,
                                       vary_diffusivities=[False, False, True])
    wb7.peak_D3a[idx], init, fin = wb7.fitD(peak_idx=idx, show_plot=False,
                                       heights_instead=True, 
                                       wholeblock_data=False,
                                       init=meta, 
                                       fin=maxy*scale_final,
                                       log10Ds_m2s=D3,
                                       vary_diffusivities=[True, False, False])

#%%
fmt = '{:.1f}'

print('-'*50)
print('assuming quadratic baseline')
print('hydrated SC1-7 water:', fmt.format(wb7area), 'ppm H2O across profile')
print('hydrated SC1-2 water:', fmt.format(wb2area), 'ppm H2O across profile')
print()
print('Kohlstedt & Mackwell 1998 experiments at 1000C, 200MPa, NNO, 8hr')
print('"metastable equilibrium" concentration')
exper.convertH(7)
print('final concentration')
exper.convertH(50)
print()
print('Solubility at 1000C, according to Mosenfelder et al. 2006')
print(fmt.format(trueC), 'ppm H2O')
print()
print('If final concentration is really', fmt.format(trueC), 'ppm H2O')
print('Kohlstedt Mackwell metastable equilibrium is', fmt.format(trueC*(7/50)), 'ppm H2O')
print()
print('metastable equilibrium in SC1-2', fmt.format(metastable), 'ppm H2O')
print()
print('proton-vacancy mechanism D at 1000C')
print('log10', fmt.format(D3[0]), 'm2/s || a')
print('log10', fmt.format(D3[1]), 'm2/s || b')
print('log10', fmt.format(D3[2]), 'm2/s || c')
print('Least-squares best-fit diffusivities || c assuming:')
print('* initial "metastable equlibrium"', fmt.format(metastable), 'ppm H2O')
print('* final concentration:', fmt.format(trueC), 'ppm H2O')
print('* ratio of final to measured max peak height:', fmt.format(scale_final))
print('bulk H:            log10', fmt.format(wb7.D3[2]), '|| c in m2/s')
for idx in range(4):
    txt = ' '.join(('peak at', str(peaks[idx]), 'cm-1: log10', 
                    str(fmt.format(wb7.peak_D3[idx][2])), '|| c in m2/s'))
    print(txt)
print('Holding Dc constant but varying Da')
print('bulk H:            log10', fmt.format(wb7.D3a[2]), '|| a in m2/s')
for idx in range(4):
    txt = ' '.join(('peak at', str(peaks[idx]), 'cm-1: log10', 
                    str(fmt.format(wb7.peak_D3a[idx][0])), '|| a in m2/s'))
    print(txt)    