# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:09:31 2017

@author: Ferriss
"""
from __future__ import division, print_function
from olivine.KilaueaIki import Kiki_spectra as kiki

thisfolder = kiki.thisfolder

wb = kiki.wb_Kiki_init

prof = wb.profiles[0]
x, y = prof.diffusion1D(-12, 3600)
print(x)
print(y)

#spec = wb.profiles[0].spectra[1]
#spec.get_baseline(folder=kiki.FTIR_file_location)

#spec2 = wb.profiles[0].spectra[1]
#spec2.get_baseline(folder=kiki.FTIR_file_location)

#%%
#spec.get_baseline(folder=kiki.FTIR_file_location)
#spec.get_peakfit(folder=kiki.FTIR_file_location)
#spec2.get_peakfit()
#spec.plot_peakfit()

#%%
#spec.fname
#%%
#print(x)
#x = x.sort_values(by=[0])
#print(x)