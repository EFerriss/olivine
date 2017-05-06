# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 14:24:39 2016

@author: Ferriss

Profile information for Kilauea Iki olivine used in dehydration experiments
"""
from __future__ import print_function, division
from pynams import Sample, Spectrum, Profile, Block
import os
import numpy as np
from olivine import FTIR

FTIR_file_location = ''.join((os.path.dirname(FTIR.__file__), '\\'))
thisfolder = ''.join((FTIR_file_location, '..\\KilaueaIki\\'))

#%%

### Scoping measurements on doubly polished grain
Kiki_thickness_microns = np.mean(np.array([2035., 2038., 2036., 2037., 2037.]))
Kiki_scope_unpol = Spectrum(fname='Kiki1_scope_unpol', 
                                    folder=FTIR_file_location,
                                    thickness_microns=Kiki_thickness_microns)
Kiki_scope_45deg = Spectrum(fname='Kiki1_scope_45deg',
                                    folder=FTIR_file_location,
                                    thickness_microns=Kiki_thickness_microns)
Kiki_scope_90deg = Spectrum(fname='Kiki1_scope_90deg',
                                    folder=FTIR_file_location,
                                    thickness_microns=Kiki_thickness_microns)
Kiki_scope_135deg = Spectrum(fname='Kiki1_scope_135deg',
                                     folder=FTIR_file_location,
                                     thickness_microns=Kiki_thickness_microns)
Kiki_scope_140deg = Spectrum(fname='Kiki1_scope_140deg',
                                     folder=FTIR_file_location,
                                     thickness_microns=Kiki_thickness_microns)
Kiki_scope_150deg = Spectrum(fname='Kiki1_scope_150deg',
                                     folder=FTIR_file_location,
                                     thickness_microns=Kiki_thickness_microns)

### Final sample dimensions
Kiki_sample = Sample(length_a_microns=[2063., 2062., 2064., 2063., 2064.],
                     length_c_microns=[1294., 1294., 1293., 1294., 1294.],
                     length_b_microns=[1073., 1073., 1073., 1073., 1073,])

### Polarized measurements on untreated sample to estimate orientation
### NOTE: the estimated orientations based on polarized IR got [100] correct,
### but [010] and [001] were switched! All code has been updated to 
### account for that mistake, but the original filenames retain the
### incorrect labels.
Kiki_init_Ea_1 = Spectrum(fname='Kiki1_dthin_Estraight', 
                          folder=FTIR_file_location,
                          raypath='b', polar='a',
                          sample=Kiki_sample)
Kiki_init_Ea_2 = Spectrum(fname='Kiki1_dstraight_Elong', 
                          folder=FTIR_file_location,
                          raypath='b', polar='a', sample=Kiki_sample)
Kiki_init_Ea = Spectrum(folder=None, fname=None)
Kiki_init_Ea.make_average_spectra([Kiki_init_Ea_1, Kiki_init_Ea_2])
Kiki_init_Ea.fname='Kiki_init_Ea'
Kiki_init_Ea.save_spectrum(folder=FTIR_file_location, delim=',', 
                           file_ending='.CSV', raw_data=True, printout=False)
Kiki_init_Ea = Spectrum(fname='Kiki_init_Ea', 
                        folder=FTIR_file_location,
                        raypath='b', polar='a', sample=Kiki_sample)

Kiki_init_Ec_1 = Spectrum(fname='Kiki1_dthin_Eslant', 
                                  folder=FTIR_file_location,
                                  raypath='b', polar='c', sample=Kiki_sample)
Kiki_init_Ec_2 = Spectrum(fname='Kiki1_dcrack_Elong', 
                                  folder=FTIR_file_location,
                                  raypath='a', polar='c', sample=Kiki_sample)
Kiki_init_Ec = Spectrum(folder=None, fname=None)
Kiki_init_Ec.make_average_spectra([Kiki_init_Ec_1, Kiki_init_Ec_2])
Kiki_init_Ec.fname='Kiki_init_Ec'
Kiki_init_Ec.save_spectrum(folder=FTIR_file_location, delim=',',
                           file_ending='.CSV', raw_data=True, printout=False)
Kiki_init_Ec = Spectrum(fname='Kiki_init_Ec', 
                        folder=FTIR_file_location,
                        raypath='b', polar='c', sample=Kiki_sample)

Kiki_init_Eb = Spectrum(fname='Kiki1_dcrack_Ethin', 
                                folder=FTIR_file_location,
                                raypath='a', polar='b', sample=Kiki_sample)

### initial profile measurements on untreated sample
Kiki_init_profileA = Profile(name='Kilauea Iki untreated olivine || a', 
                             time_seconds=0.0001,
                             fnames=['Kiki1_init_a1', 'Kiki1_init_a2',
                                      'Kiki1_init_a3', 'Kiki1_init_a4',
                                      'Kiki1_init_a5', 'Kiki1_init_a6',
                                      'Kiki1_init_a7',],
                              positions_microns=np.linspace(200., 
                              np.mean(Kiki_sample.length_a_microns)-200, 7), 
                              folder=FTIR_file_location,
                              sample=Kiki_sample, direction='a', raypath='b')

Kiki_init_profileC = Profile(name='Kilauea Iki untreated olivine || c',
                             time_seconds=0.0001,
                                     folder=FTIR_file_location,
                              fnames=['Kiki1_init_b3', 'Kiki1_init_b4',
                                      'Kiki1_init_b5', 'Kiki1_init_b6',],
                              positions_microns=np.linspace(400.,
                              np.mean(Kiki_sample.length_b_microns)-200, 4), 
                              sample=Kiki_sample, direction='c', raypath='b')

Kiki_init_profileB = Profile(name='Kilauea Iki untreated olivine || b',
                              time_seconds=0.0001, folder=FTIR_file_location,
                              fnames=['Kiki1_init_c1', 'Kiki1_init_c2',
                                      'Kiki1_init_c3', 'Kiki1_init_c4',
                                      'Kiki1_init_c5', 'Kiki1_init_c6',
                                      'Kiki1_init_c7', 'Kiki1_init_c8',],
                              positions_microns=np.linspace(200., 
                              np.mean(Kiki_sample.length_c_microns)-200, 8), 
                              sample=Kiki_sample, direction='b', raypath='c')

wb_Kiki_init = Block(profiles=[Kiki_init_profileA, Kiki_init_profileB, 
                                     Kiki_init_profileC],
                           name='Kilauea Iki untreated olivine', 
                           time_seconds=0.0001,
                           sample=Kiki_sample, celsius=800.)

wb_Kiki_init_ave = wb_Kiki_init.average_spectra()
wb_Kiki_init_ave.fname = 'wb_Kiki_init_ave'
wb_Kiki_init_ave.folder = FTIR_file_location

### Profiles after 1 hour of heating at 800 C
length = Kiki_sample.thickness_microns[0]
Kiki_1hr_profileA = Profile(name='Kilauea Iki olivine heated 1hr || a',
                             time_seconds=3600.,
                             fnames=['Kiki_1hr_a01', 'Kiki_1hr_a02', 
                                    'Kiki_1hr_a03', 'Kiki_1hr_a05',
                                    'Kiki_1hr_a07', 'Kiki_1hr_a09',
                                    'Kiki_1hr_a1011', 'Kiki_1hr_a13',
                                    'Kiki_1hr_a15', 'Kiki_1hr_a17',
                                    'Kiki_1hr_a18', 'Kiki_1hr_a19',
                                    'Kiki_1hr_a20'],
                           positions_microns=[50., 150., 350., 550., 750., 
                                              950., 1100., 1350., 1550., 1750.,
                                              1850., 1950., length-50.], 
                           folder=FTIR_file_location, sample=Kiki_sample, 
                           direction='a', raypath='b', 
                           initial_profile=Kiki_init_profileA)

Kiki_1hr_profileC = Profile(name='Kilauea Iki olivine heated 1hr || c',
                                   time_seconds=3600.,
                                   fnames=['Kiki_1hr_b01', 'Kiki_1hr_b02',
                                           'Kiki_1hr_b03', 'Kiki_1hr_b04',
                                           'Kiki_1hr_b05', 'Kiki_1hr_b06',
                                           'Kiki_1hr_b07', 
                                           'Kiki_1hr_b08', 'Kiki_1hr_b09',
                                           'Kiki_1hr_b10', 'Kiki_1hr_b11',
                                           'Kiki_1hr_b12'],
                                   positions_microns= np.linspace(50., 1150., 12.),
                                   folder=FTIR_file_location,
                                   sample=Kiki_sample, 
                                   direction='c', raypath='b',
                                   initial_profile=Kiki_init_profileC)

Kiki_1hr_profileB = Profile(name='Kilauea Iki olivine heated 1hr || b', 
                                   time_seconds=3600.,
                                   fnames=['Kiki_1hr_c01', 'Kiki_1hr_c02',
                                           'Kiki_1hr_c03', 'Kiki_1hr_c04',
                                           'Kiki_1hr_c05', 'Kiki_1hr_c06',
                                           'Kiki_1hr_c07', 
                                           'Kiki_1hr_c08', 'Kiki_1hr_c09',
                                           'Kiki_1hr_c10', 'Kiki_1hr_c11',
                                           'Kiki_1hr_c12'],
                                   positions_microns = np.linspace(50.,1150., 
                                                                   12.),
                                   folder=FTIR_file_location,
                                   sample=Kiki_sample, 
                                   direction='b', raypath='c',
                                   initial_profile=Kiki_init_profileB)

wb_Kiki_1hr = Block(profiles=[Kiki_1hr_profileA, Kiki_1hr_profileB, 
                                     Kiki_1hr_profileC],
                         name='Kilauea Iki olivine heated 800C 1hr', 
                         time_seconds=3600., celsius=800.,
                         sample=Kiki_sample)

### Profiles after 8 hours of heating at 800 C 
### This is the initial for 1000C experiments
name = 'Kilauea Iki olivine heated 8hr at 800$\degree$C || a'
length = Kiki_sample.thickness_microns[0]
Kiki_8hr_profileA = Profile(name=name, time_seconds=3600.,
                           fnames=['Kiki_8hr_a01', 'Kiki_8hr_a02', 
                                   'Kiki_8hr_a03', 'Kiki_8hr_a05',
                                   'Kiki_8hr_a07', 'Kiki_8hr_a09',
                                   'Kiki_8hr_a1011', 'Kiki_8hr_a13',
                                   'Kiki_8hr_a15', 'Kiki_8hr_a17',
                                   'Kiki_8hr_a18', 'Kiki_8hr_a19',
                                   'Kiki_8hr_a20'],
                           positions_microns=[50., 150., 350., 550., 750., 
                                              950., 1100., 1350., 1550., 1750.,
                                              1850., 1950., length-50.], 
                           folder=FTIR_file_location, sample=Kiki_sample, 
                           direction='a', raypath='b', 
                           initial_profile=Kiki_init_profileA)

name = 'Kilauea Iki olivine heated 8hr at 800$\degree$C || c'
Kiki_8hr_profileC = Profile(name=name, time_seconds=3600.,
                            fnames=['Kiki_8hr_b01', 'Kiki_8hr_b02',
                                    'Kiki_8hr_b03', 'Kiki_8hr_b04',
                                    'Kiki_8hr_b05', 'Kiki_8hr_b06',
                                    'Kiki_8hr_b07', 'Kiki_8hr_b08', 
                                    'Kiki_8hr_b09', 'Kiki_8hr_b10', 
                                    'Kiki_8hr_b11','Kiki_8hr_b12'],
                           positions_microns= np.linspace(50., 1150., 12.),
                           folder=FTIR_file_location,
                           sample=Kiki_sample, 
                           direction='c', raypath='b',
                           initial_profile=Kiki_init_profileC)

name = 'Kilauea Iki olivine heated 8hr at 800$\degree$C || b'
Kiki_8hr_profileB = Profile(name=name, time_seconds=3600.,
                            fnames=['Kiki_8hr_c01', 'Kiki_8hr_c02',
                                    'Kiki_8hr_c03', 'Kiki_8hr_c04',
                                    'Kiki_8hr_c05', 'Kiki_8hr_c06',
                                    'Kiki_8hr_c07', 'Kiki_8hr_c08', 
                                    'Kiki_8hr_c09', 'Kiki_8hr_c10', 
                                    'Kiki_8hr_c11', 'Kiki_8hr_c12'],
                           positions_microns = np.linspace(50.,1150., 12.),
                           folder=FTIR_file_location,
                           sample=Kiki_sample, 
                           direction='b', raypath='c',
                           initial_profile=Kiki_init_profileB)

wb_Kiki_8hr = Block(profiles=[Kiki_8hr_profileA, Kiki_8hr_profileB, 
                                     Kiki_8hr_profileC],
                         name='Kilauea Iki olivine heated 800C 8hrs', 
                         time_seconds=3600., celsius=800.,
                         sample=Kiki_sample)

### Profiles after 8 hours of heating at 800 C + 3 hours heating at 1000 C
name = 'Kilauea Iki olivine heated 3hr at 1000$\degree$C || a'
length = Kiki_sample.thickness_microns[0]
Kiki_1000C_3hr_profileA = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_3hr_a01', 
                                          'Kiki_1000C_3hr_a02', 
                                          'Kiki_1000C_3hr_a03', 
                                          'Kiki_1000C_3hr_a05',
                                          'Kiki_1000C_3hr_a07', 
                                          'Kiki_1000C_3hr_a09',
                                          'Kiki_1000C_3hr_a1011', 
                                          'Kiki_1000C_3hr_a13',
                                          'Kiki_1000C_3hr_a15', 
                                          'Kiki_1000C_3hr_a17',
                                          'Kiki_1000C_3hr_a18', 
                                          'Kiki_1000C_3hr_a19',
                                          'Kiki_1000C_3hr_a20'],
                                  positions_microns=[50., 150., 350., 550., 
                                                     750., 950., 1100., 1350., 
                                                     1550., 1750., 1850., 
                                                     1950., length-50.], 
                                 folder=FTIR_file_location, sample=Kiki_sample, 
                                 direction='a', raypath='b', 
                                 initial_profile=Kiki_8hr_profileA)

name = 'Kilauea Iki olivine heated 3hr at 1000$\degree$C || c'
length = Kiki_sample.thickness_microns[2]
Kiki_1000C_3hr_profileC = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_3hr_b01', 
                                          'Kiki_1000C_3hr_b02',
                                          'Kiki_1000C_3hr_b03', 
                                          'Kiki_1000C_3hr_b04',
                                          'Kiki_1000C_3hr_b05', 
                                          'Kiki_1000C_3hr_b06',
                                          'Kiki_1000C_3hr_b07', 
                                          'Kiki_1000C_3hr_b08', 
                                          'Kiki_1000C_3hr_b09',
                                          'Kiki_1000C_3hr_b10', 
                                          'Kiki_1000C_3hr_b11',
                                          'Kiki_1000C_3hr_b12'],
                               positions_microns= np.linspace(50., 1150., 12.),
                               folder=FTIR_file_location, sample=Kiki_sample, 
                               direction='c', raypath='b',
                               initial_profile=Kiki_8hr_profileB)

name = 'Kilauea Iki olivine heated 3hr at 1000$\degree$C || b'
length = Kiki_sample.thickness_microns[1]
Kiki_1000C_3hr_profileB = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_3hr_c01', 
                                          'Kiki_1000C_3hr_c02',
                                          'Kiki_1000C_3hr_c03', 
                                          'Kiki_1000C_3hr_c04',
                                          'Kiki_1000C_3hr_c05', 
                                          'Kiki_1000C_3hr_c06',
                                          'Kiki_1000C_3hr_c07', 
                                          'Kiki_1000C_3hr_c08', 
                                          'Kiki_1000C_3hr_c09',
                                          'Kiki_1000C_3hr_c10', 
                                          'Kiki_1000C_3hr_c11',
                                          'Kiki_1000C_3hr_c12'],
                            positions_microns = np.linspace(50.,1150., 12.),
                            folder=FTIR_file_location, sample=Kiki_sample, 
                            direction='b', raypath='c',
                            initial_profile=Kiki_8hr_profileC)

name='Kilauea Iki olivine heated 800C 8hrs + 1000C 3hrs'
wb_Kiki_1000C_3hr = Block(profiles=[Kiki_1000C_3hr_profileA, 
                                        Kiki_1000C_3hr_profileB, 
                                        Kiki_1000C_3hr_profileC],
                              name=name, time_seconds=3600.*3., 
                              sample=Kiki_sample, celsius=1000.)

### Profiles after 8 hours of heating at 800 C + 6 hours heating at 1000 C
name = 'Kilauea Iki olivine heated 6hr at 1000$\degree$C || a'
length = Kiki_sample.thickness_microns[0]
Kiki_1000C_6hr_profileA = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_6hr_a01', 
                                          'Kiki_1000C_6hr_a02', 
                                          'Kiki_1000C_6hr_a03', 
                                          'Kiki_1000C_6hr_a05',
                                          'Kiki_1000C_6hr_a07', 
                                          'Kiki_1000C_6hr_a09',
                                          'Kiki_1000C_6hr_a1011', 
                                          'Kiki_1000C_6hr_a13',
                                          'Kiki_1000C_6hr_a15', 
                                          'Kiki_1000C_6hr_a17',
                                          'Kiki_1000C_6hr_a18', 
                                          'Kiki_1000C_6hr_a19',
                                          'Kiki_1000C_6hr_a20'],
                                  positions_microns=[50., 150., 350., 550., 
                                                     750., 950., 1100., 1350., 
                                                     1550., 1750., 1850., 
                                                     1950., length-50.], 
                                 folder=FTIR_file_location, sample=Kiki_sample, 
                                 direction='a', raypath='b', 
                                 initial_profile=Kiki_8hr_profileA)

name = 'Kilauea Iki olivine heated 6hr at 1000$\degree$C || c'
length = Kiki_sample.thickness_microns[2]
Kiki_1000C_6hr_profileC = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_6hr_b01', 
                                          'Kiki_1000C_6hr_b02',
                                          'Kiki_1000C_6hr_b03', 
                                          'Kiki_1000C_6hr_b04',
                                          'Kiki_1000C_6hr_b05', 
                                          'Kiki_1000C_6hr_b06',
                                          'Kiki_1000C_6hr_b07', 
                                          'Kiki_1000C_6hr_b08', 
                                          'Kiki_1000C_6hr_b09',
                                          'Kiki_1000C_6hr_b10', 
                                          'Kiki_1000C_6hr_b11',
                                          'Kiki_1000C_6hr_b12'],
                               positions_microns= np.linspace(50., 1150., 12.),
                               folder=FTIR_file_location, sample=Kiki_sample, 
                               direction='c', raypath='b',
                               initial_profile=Kiki_8hr_profileB)

name = 'Kilauea Iki olivine heated 6hr at 1000$\degree$C || b'
length = Kiki_sample.thickness_microns[1]
Kiki_1000C_6hr_profileB = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_6hr_c01', 
                                          'Kiki_1000C_6hr_c02',
                                          'Kiki_1000C_6hr_c03', 
                                          'Kiki_1000C_6hr_c04',
                                          'Kiki_1000C_6hr_c05', 
                                          'Kiki_1000C_6hr_c06',
                                          'Kiki_1000C_6hr_c07', 
                                          'Kiki_1000C_6hr_c08', 
                                          'Kiki_1000C_6hr_c09',
                                          'Kiki_1000C_6hr_c10', 
                                          'Kiki_1000C_6hr_c11',
                                          'Kiki_1000C_6hr_c12'],
                            positions_microns = np.linspace(50.,1150., 12.),
                            folder=FTIR_file_location, sample=Kiki_sample, 
                            direction='b', raypath='c',
                            initial_profile=Kiki_8hr_profileC)

name='Kilauea Iki olivine heated 800C 8hrs + 1000C 6hrs'
wb_Kiki_1000C_6hr = Block(profiles=[Kiki_1000C_6hr_profileA, 
                                        Kiki_1000C_6hr_profileB, 
                                        Kiki_1000C_6hr_profileC],
                              name=name, time_seconds=3600.*6., 
                              sample=Kiki_sample, celsius=1000.)

### Profiles after 8 hours of heating at 800 C + 7 hours heating at 1000 C
name = 'Kilauea Iki olivine heated 7hr at 1000$\degree$C || a'
length = Kiki_sample.thickness_microns[0]
Kiki_1000C_7hr_profileA = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_7hr_a01', 
                                          'Kiki_1000C_7hr_a02', 
                                          'Kiki_1000C_7hr_a03', 
                                          'Kiki_1000C_7hr_a05',
                                          'Kiki_1000C_7hr_a07', 
                                          'Kiki_1000C_7hr_a09',
                                          'Kiki_1000C_7hr_a1011', 
                                          'Kiki_1000C_7hr_a13',
                                          'Kiki_1000C_7hr_a15', 
                                          'Kiki_1000C_7hr_a17',
                                          'Kiki_1000C_7hr_a18', 
                                          'Kiki_1000C_7hr_a19',
                                          'Kiki_1000C_7hr_a20'],
                                  positions_microns=[50., 150., 350., 550., 
                                                     750., 950., 1100., 1350., 
                                                     1550., 1750., 1850., 
                                                     1950., length-50.], 
                                 folder=FTIR_file_location, sample=Kiki_sample, 
                                 direction='a', raypath='b', 
                                 initial_profile=Kiki_8hr_profileA)

name = 'Kilauea Iki olivine heated 7hr at 1000$\degree$C || c'
length = Kiki_sample.thickness_microns[2]
Kiki_1000C_7hr_profileC = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_7hr_b01', 
                                          'Kiki_1000C_7hr_b02',
                                          'Kiki_1000C_7hr_b03', 
                                          'Kiki_1000C_7hr_b04',
                                          'Kiki_1000C_7hr_b05', 
                                          'Kiki_1000C_7hr_b06',
                                          'Kiki_1000C_7hr_b07', 
                                          'Kiki_1000C_7hr_b08', 
                                          'Kiki_1000C_7hr_b09',
                                          'Kiki_1000C_7hr_b10', 
                                          'Kiki_1000C_7hr_b11',
                                          'Kiki_1000C_7hr_b12'],
                               positions_microns= np.linspace(50., 1150., 12.),
                               folder=FTIR_file_location, sample=Kiki_sample, 
                               direction='c', raypath='b',
                               initial_profile=Kiki_8hr_profileB)

name = 'Kilauea Iki olivine heated 6hr at 1000$\degree$C || b'
length = Kiki_sample.thickness_microns[1]
Kiki_1000C_7hr_profileB = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_1000C_7hr_c01', 
                                          'Kiki_1000C_7hr_c02',
                                          'Kiki_1000C_7hr_c03', 
                                          'Kiki_1000C_7hr_c04',
                                          'Kiki_1000C_7hr_c05', 
                                          'Kiki_1000C_7hr_c06',
                                          'Kiki_1000C_7hr_c07', 
                                          'Kiki_1000C_7hr_c08', 
                                          'Kiki_1000C_7hr_c09',
                                          'Kiki_1000C_7hr_c10', 
                                          'Kiki_1000C_7hr_c11',
                                          'Kiki_1000C_7hr_c12'],
                            positions_microns = np.linspace(50.,1150., 12.),
                            folder=FTIR_file_location, sample=Kiki_sample, 
                            direction='b', raypath='c',
                            initial_profile=Kiki_8hr_profileC)

name='Kilauea Iki olivine heated 800C 8hrs + 1000C 7hrs'
wb_Kiki_1000C_7hr = Block(profiles=[Kiki_1000C_7hr_profileA, 
                                        Kiki_1000C_7hr_profileB, 
                                        Kiki_1000C_7hr_profileC],
                              name=name, time_seconds=3600.*7., 
                              sample=Kiki_sample, celsius=1000.)

### highly oxidized final heating step 
### 8 hours of heating at 800 C + 7 hours heating at 1000 C ~QFM-2; NNO-2.6
### + 1 hour 1000C ~NNO + 2; QFM + 2.7
name = 'Kilauea Iki olivine oxidized heating step || a'
length = Kiki_sample.thickness_microns[0]
Kiki_ox_1000C_1hr_profileA = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_ox_1000C_1hr_a01', 
                                          'Kiki_ox_1000C_1hr_a02', 
                                          'Kiki_ox_1000C_1hr_a03', 
                                          'Kiki_ox_1000C_1hr_a05',
                                          'Kiki_ox_1000C_1hr_a07', 
                                          'Kiki_ox_1000C_1hr_a09',
                                          'Kiki_ox_1000C_1hr_a1011', 
                                          'Kiki_ox_1000C_1hr_a13',
                                          'Kiki_ox_1000C_1hr_a15', 
                                          'Kiki_ox_1000C_1hr_a17',
                                          'Kiki_ox_1000C_1hr_a18', 
                                          'Kiki_ox_1000C_1hr_a19',
                                          'Kiki_ox_1000C_1hr_a20'],
                                  positions_microns=[50., 150., 350., 550., 
                                                     750., 950., 1100., 1350., 
                                                     1550., 1750., 1850., 
                                                     1950., length-50.], 
                                 folder=FTIR_file_location, sample=Kiki_sample, 
                                 direction='a', raypath='b', 
                                 initial_profile=Kiki_8hr_profileA)

name = 'Kilauea Iki olivine oxidized heating step || b'
length = Kiki_sample.thickness_microns[2]
Kiki_ox_1000C_1hr_profileC = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_ox_1000C_1hr_b01', 
                                          'Kiki_ox_1000C_1hr_b02',
                                          'Kiki_ox_1000C_1hr_b03', 
                                          'Kiki_ox_1000C_1hr_b04',
                                          'Kiki_ox_1000C_1hr_b05', 
                                          'Kiki_ox_1000C_1hr_b06',
                                          'Kiki_ox_1000C_1hr_b07', 
                                          'Kiki_ox_1000C_1hr_b08', 
                                          'Kiki_ox_1000C_1hr_b09',
                                          'Kiki_ox_1000C_1hr_b10', 
                                          'Kiki_ox_1000C_1hr_b11',
                                          'Kiki_ox_1000C_1hr_b12'],
                               positions_microns= np.linspace(50., 1150., 12.),
                               folder=FTIR_file_location, sample=Kiki_sample, 
                               direction='c', raypath='b',
                               initial_profile=Kiki_8hr_profileB)

name = 'Kilauea Iki olivine oxidized heating step || c'
length = Kiki_sample.thickness_microns[1]
Kiki_ox_1000C_1hr_profileB = Profile(name=name, time_seconds=3600.,
                                  fnames=['Kiki_ox_1000C_1hr_c01', 
                                          'Kiki_ox_1000C_1hr_c02',
                                          'Kiki_ox_1000C_1hr_c03', 
                                          'Kiki_ox_1000C_1hr_c04',
                                          'Kiki_ox_1000C_1hr_c05', 
                                          'Kiki_ox_1000C_1hr_c06',
                                          'Kiki_ox_1000C_1hr_c07', 
                                          'Kiki_ox_1000C_1hr_c08', 
                                          'Kiki_ox_1000C_1hr_c09',
                                          'Kiki_ox_1000C_1hr_c10', 
                                          'Kiki_ox_1000C_1hr_c11',
                                          'Kiki_ox_1000C_1hr_c12'],
                            positions_microns = np.linspace(50.,1150., 12.),
                            folder=FTIR_file_location, sample=Kiki_sample, 
                            direction='b', raypath='c',
                            initial_profile=Kiki_8hr_profileC)

name = 'Kilauea Iki olivine oxidized heating step'
wb_Kiki_ox = Block(profiles=[Kiki_ox_1000C_1hr_profileA, 
                             Kiki_ox_1000C_1hr_profileB, 
                             Kiki_ox_1000C_1hr_profileC],
                    name=name, time_seconds=3600.*8., 
                    sample=Kiki_sample, celsius=1000.)

wb_Kiki_ox_ave = wb_Kiki_ox.average_spectra()
wb_Kiki_ox_ave.fname = 'wb_Kiki_ox_ave'
wb_Kiki_ox_ave.folder = FTIR_file_location
