# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:32:48 2017

@author: Ferriss
"""

from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
#from pynams import dlib
#import matplotlib.pyplot as plt
#import numpy as np
#from uncertainties import ufloat

#%%
wb_kiki = kiki.wb_Kiki_8hr
wb_SC = SC.wb_800C_7hr

for wb in [wb_kiki, wb_SC]:
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=kiki.peaks)
    wb.areas = [prof.areas for prof in wb.profiles]
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]
#    wb.style['color'] = 'darkmagenta'
#    wb.style['markeredgecolor'] = 'darkmagenta'

wb_kiki.style['color'] = 'darkmagenta'
wb_SC.style['color'] = '#2ca02c'
#%%
fig, ax3 = wb_kiki.plot_areas_3panels(wholeblock=True, 
                                      centered=True,
                                      styles3=[wb_kiki.style]*3)
wb_SC.plot_areas_3panels(wholeblock=True, axes3=ax3,
                         centered=True,
                         styles3=[wb_SC.style]*3)

ax3[1].set_title('Changes in [Ti] peak after heating at 800C, QFM-2')
ax3[0].set_ylabel('Peak height at 3525 cm-1/ initial')

ax3[2].legend(loc=4)