# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:40:38 2017

@author: Ferriss

unoriented San Carlos olivines used to test experimental and analytical 
procedures
"""
from __future__ import print_function, division
from pynams import Sample, Spectrum
import os
import numpy as np
from olivine import FTIR

FTIR_file_location = ''.join((os.path.dirname(FTIR.__file__), '\\'))
thisfolder = ''.join((FTIR_file_location, '..\\San Carlos\\'))

#%% Test San Carlos olivine samples SCt*
# SCt5 given to Beth Goldoff for testing hole drilling at the museum
SCt1_sample = Sample(thickness_thinslab_microns=[2117., 2072., 2105., 2080., 
                                                 2115.])
SCt2_sample = Sample(thickness_thinslab_microns=[2110., 2072., 2105., 2080., 
                                                 2115.])
SCt3_sample = Sample(thickness_thinslab_microns=[2276., 2273., 2281., 2244., 
                                                 2253.])
SCt4_sample = Sample(thickness_thinslab_microns=[2278., 2267., 2318., 2272., 
                                                 2248.])
SCt5_sample = Sample(thickness_thinslab_microns=[2488., 2533., 2521., 2491., 
                                                 2479.])
SCt6_sample = Sample(thickness_thinslab_microns=[2421., 2482., 2410., 2442., 
                                                 2467.])

# initial spectra
SCt1i_100scans = Spectrum(fname='SCt1i-100scans', sample=SCt1_sample,
                          folder=FTIR_file_location)
SCt1i_200scans = Spectrum(fname='SCt1i-200scans', sample=SCt1_sample,
                          folder=FTIR_file_location)
SCt1i_300scans = Spectrum(fname='SCt1i-300scans', sample=SCt1_sample,
                          folder=FTIR_file_location)
SCt1i = Spectrum(fname='SCt1i', sample=SCt1_sample, folder=FTIR_file_location)
SCt2i = Spectrum(fname='SCt2i', sample=SCt2_sample, folder=FTIR_file_location)
SCt3i = Spectrum(fname='SCt3i', sample=SCt3_sample, folder=FTIR_file_location)
SCt4i = Spectrum(fname='SCt4i', sample=SCt4_sample, folder=FTIR_file_location)
SCt5i = Spectrum(fname='SCt5i', sample=SCt5_sample, folder=FTIR_file_location)
SCt6i = Spectrum(fname='SCt6i', sample=SCt6_sample, folder=FTIR_file_location)

#%% SCt2 
# 20 hours 3 minutes at 700 C 10 kbar; initial = SCt2i; broke into 3 pieces
SCt2_1_core = Spectrum(fname='SCt2-1-core', sample=SCt2_sample, folder=FTIR_file_location)
SCt2_1_rim = Spectrum(fname='SCt2-1-rim', sample=SCt2_sample, folder=FTIR_file_location)
SCt2_3 = Spectrum(fname='SCt2-3', sample=SCt2_sample, folder=FTIR_file_location)

#%% SCt2a
# 5 Nov 2015: , 93 hours at 800 C, 10 kbar; broke into four pieces
### THICKNESS VERY UNCERTAIN
SCt2a = Spectrum(fname='SCt2a-1', sample=SCt2_sample, folder=FTIR_file_location)

#%% SCt4 1 Dec 2015: thick Cu capsule; CHECK thick-microns!!
thick_slide_mm = np.mean([1.537, 1.538, 1.545])
thick_slide_plus_sample_mm = np.mean([3.780, 3.796, 3.738])
thick_SCt4_microns = (thick_slide_plus_sample_mm - thick_slide_mm) * 1000.
SCt4core = Spectrum(fname='SCt4core', thickness_microns=thick_SCt4_microns, 
                    folder=FTIR_file_location)
SCt4rim = Spectrum(fname='SCt4rim', thickness_microns=thick_SCt4_microns, 
                   folder=FTIR_file_location)


