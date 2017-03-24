# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:32:26 2017

@author: Ferriss

unpolarized profiles on hydrated SC1-2
"""
from __future__ import print_function, division
from pynams import Sample, Spectrum, Profile
import os
import numpy as np
from olivine import FTIR

SC1_2_sample = Sample(length_a_microns=[2310., 2292., 2319., 2309., 2318.], 
                          length_b_microns=[1981., 1960., 1982., 1968., 1989.], 
                          length_c_microns=[2200.])

FTIR_file_location = ''.join((os.path.dirname(FTIR.__file__), '\\'))

# unpolarized with two different ray paths
SC1_2_hyd_db_unpol = Spectrum(fname='SC1-2-hyd-dcross-unpol',
                                     folder=FTIR_file_location,
                            thickness_microns=np.mean(SC1_2_sample.length_b_microns))
SC1_2_hyd_da_unpol = Spectrum(fname='SC1-2-hyd-dline-unpol',
                                     folder=FTIR_file_location,
                            thickness_microns=np.mean(SC1_2_sample.length_a_microns))

SC1_2_hydrated_profileA = Profile(profile_name='SC1-2-hydrated initial || a',
                          sample=SC1_2_sample, direction='a', raypath='b', 
                          folder=FTIR_file_location,
                          fnames=['SC1-2-hyd-a01', 
                                      'SC1-2-hyd-a06',
                                      'SC1-2-hyd-dcross-unpol',
                                      'SC1-2-hyd-a12',
                                      'SC1-2-hyd-a15',
                                      'SC1-2-hyd-a18',
                                      'SC1-2-hyd-a21'],
                          positions_microns=[150., 650., 1000., 1250., 1550., 
                                             1850., 2150.])
                                             
SC1_2_hydrated_profileB = Profile(profile_name='SC1-2-hydrated initial || b',
                          sample=SC1_2_sample, direction='b', raypath='c',
                          folder=FTIR_file_location,
                          fnames=['SC1-2-hyd-b01',
                                      'SC1-2-hyd-b03', 
                                      'SC1-2-hyd-b06',
                                      'SC1-2-hyd-b10-unpol-400scans',
                                      'SC1-2-hyd-b13',
                                      'SC1-2-hyd-b16',
                                      'SC1-2-hyd-b21'], 
                          positions_microns=[125., 300., 600., 1000.,
                                             1300., 1600., 1850.])


SC1_2_hydrated_profileC = Profile(profile_name='SC1-2-hydrated initial || c',
                          sample=SC1_2_sample, direction='c', raypath='b', 
                          folder=FTIR_file_location,
                          fnames=[#'SC1-2-hyd-c01', # too noisy!
                                      'SC1-2-hyd-c03',
                                      'SC1-2-hyd-c06',
                                      'SC1-2-hyd-c09',
                                      'SC1-2-hyd-c12',
                                      'SC1-2-hyd-dcross-unpol',
                                      'SC1-2-hyd-c21',
                                      'SC1-2-hyd-c24',
                                      'SC1-2-hyd-c27',
                                      'SC1-2-hyd-c30'],
                          positions_microns=[#50., 
                                             200., 500., 800., 1100.,
                                             1600., 2000., 2300., 2600., 2900.]
                                             )
