#-*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:20:20 2015

@author: Ferriss

FTIR spectra and profiles measured during hydration dehyration experiments 
on San Carlos olivine oriented by Laue Camera at Cornell
"""

from __future__ import print_function, division
from pynams import Sample, Spectrum, Profile, Block
import os
import numpy as np
from olivine import FTIR

FTIR_file_location = ''.join((os.path.dirname(FTIR.__file__), '\\'))
thisfolder = ''.join((FTIR_file_location, '..\\San Carlos\\'))
        
#%% untreated San Carlos olivine: SC1-1
# These spectra are assumed to represent the initial water content of SC1-2,
# which was cut from the same crystal, hydrated and then dehyrated.

sample_SC1_1 = Sample(length_a_microns=[2241., 2239., 2240., 2221., 2230., 
                                        2237., 2242., 2233., 2242., 2227.,
                                        2240.], 
                      length_b_microns=[1950., 1957., 1955., 1953., 1955.], 
                      length_c_microns=[3000.],
                      IGSN='IEFERJAI3')

### polarized measurements on untreated sample 
# E || a average of 3 spectra saved as SC-untreated-Ea.CSV
SC1_1_dcut_Eshort_1 = Spectrum(fname='SC1-1-dcut-Eshort-1',
                               folder=FTIR_file_location,
                               raypath='b', sample=sample_SC1_1)
SC1_1_dcut_Eshort_2 = Spectrum(fname='SC1-1-dcut-Eshort-2',
                               folder=FTIR_file_location,
                               raypath='b', sample=sample_SC1_1)
SC1_1_dcut_Eshort_3 = Spectrum(fname='SC1-1-dcut-Eshort-3',
                               folder=FTIR_file_location,
                               raypath='b', sample=sample_SC1_1)
SC_untreated_Ea = Spectrum(folder=None, fname=None)
SC_untreated_Ea.make_average_spectra(spectra_list=[SC1_1_dcut_Eshort_1, 
                                                   SC1_1_dcut_Eshort_2, 
                                                   SC1_1_dcut_Eshort_3], 
                                                   folder=FTIR_file_location)
SC_untreated_Ea.fname = 'SC-untreated-Ea'
SC_untreated_Ea.save_spectrum(folder=FTIR_file_location, file_ending='.CSV', 
                              delim=',', raw_data=True, printout=False)
SC_untreated_Ea = Spectrum(fname='SC-untreated-Ea', folder=FTIR_file_location,
                           raypath='b', polar='a', sample=sample_SC1_1)


# E || b average of 3 spectra saved as SC-untreated-Eb.CSV
SC1_1_dsmooth_Eshort_1 = Spectrum(fname='SC1-1-dsmooth-Eshort-1',
                                  folder=FTIR_file_location,
                                  raypath='a', sample=sample_SC1_1)
SC1_1_dsmooth_Eshort_2 = Spectrum(fname='SC1-1-dsmooth-Eshort-2',
                                  folder=FTIR_file_location,
                                  raypath='a', sample=sample_SC1_1)
SC1_1_dsmooth_Eshort_3 = Spectrum(fname='SC1-1-dsmooth-Eshort-3',
                                  folder=FTIR_file_location,
                                  raypath='a', sample=sample_SC1_1)
SC_untreated_Eb = Spectrum(folder=None, fname=None)
SC_untreated_Eb.make_average_spectra([SC1_1_dsmooth_Eshort_1, 
                                      SC1_1_dsmooth_Eshort_2, 
                                      SC1_1_dsmooth_Eshort_3],
                                      folder=FTIR_file_location)
SC_untreated_Eb.fname = 'SC-untreated-Eb'
SC_untreated_Eb.save_spectrum(folder=FTIR_file_location, file_ending='.CSV', 
                              delim=',', raw_data=True, printout=False)
SC_untreated_Eb = Spectrum(fname='SC-untreated-Eb', folder=FTIR_file_location,
                           raypath='a', polar='b', sample=sample_SC1_1)

# E || c average of 3 spectra saved as SC-untreated-Ec.CSV
SC1_1_dcut_Elong_1 = Spectrum(fname='SC1-1-dcut-Elong-1',
                                     folder=FTIR_file_location,
                                     raypath='b', sample=sample_SC1_1)
SC1_1_dcut_Elong_2 = Spectrum(fname='SC1-1-dcut-Elong-2',
                                     folder=FTIR_file_location,
                                     raypath='b', sample=sample_SC1_1)
SC1_1_dcut_Elong_3 = Spectrum(fname='SC1-1-dcut-Elong-3',
                                     folder=FTIR_file_location,
                                     raypath='b', sample=sample_SC1_1)
SC_untreated_Ec = Spectrum(folder=None, fname=None)
SC_untreated_Ec.make_average_spectra([SC1_1_dcut_Elong_1, 
                                      SC1_1_dcut_Elong_2, 
                                      SC1_1_dcut_Elong_3],
                                      folder=FTIR_file_location)
SC_untreated_Ec.fname = 'SC-untreated-Ec'
SC_untreated_Ec.save_spectrum(folder=FTIR_file_location, file_ending='.CSV', 
                              delim=',', raw_data=True, printout=False)
SC_untreated_Ec = Spectrum(fname='SC-untreated-Ec', folder=FTIR_file_location,
                           raypath='b', polar='c', sample=sample_SC1_1)

                               
#%% wb_800C_hyd
### San Carlos olivine treated at 10 kbar, 800 C, Ni-NiO, 17hr 24min: SC1-2

# This sample was repolished later, so the dimensions changed
# unpolarized FTIR profiles were made on this larger sample, but all 
# subsequent work was conducted using infrared radiation polarized || [100]
sample_SC1_2_big = Sample(length_a_microns=[2310., 2292., 2319., 2309., 2318.], 
                          length_b_microns=[1981., 1960., 1982., 1968., 1989.], 
                          length_c_microns=[2200.])

# polarized spectra with E in 3 orthogonal directions
SC1_2_hyd_Ea = Spectrum(fname='SC1-2-hyd-dcross-Eperp-polback', 
                        folder=FTIR_file_location,
                        raypath='b', sample=sample_SC1_2_big)
SC1_2_hyd_Eb = Spectrum(fname='SC1-2-hyd-dline-Eperp-polback', 
                        folder=FTIR_file_location,
                        raypath='a', sample=sample_SC1_2_big)
SC1_2_hyd_Ec = Spectrum(fname='SC1-2-hyd-dcross-Eline', 
                        folder=FTIR_file_location,
                        raypath='b', sample=sample_SC1_2_big)

# repolished sample
sample_SC1_2 = Sample(length_a_microns=[2200.],
                      length_b_microns=[1963., 1987., 1976., 1987., 1980.],
                      length_c_microns=[2858., 2864., 2858., 2863., 2864.])

# hydrated profiles measured with E || a along three directions
SC1_2_hyd_Ea_profileA = Profile(name='SC1-2-hyd || a',
                                       sample=sample_SC1_2, 
                                       direction='a', raypath='b',
                                       folder=FTIR_file_location,
                                       fnames=['SC1-2-hyd-Ea-a01',
                                       # too noisy 'SC1-2-hyd-Ea-a03',
                                                   'SC1-2-hyd-Ea-a05',
                                                   'SC1-2-hyd-Ea-a09',
                                                   'SC1-2-hyd-Ea-a13',
                                                   'SC1-2-hyd-Ea-a17',
                                                   'SC1-2-hyd-Ea-a21',], 
                                       positions_microns=[100., 500., 900.,
                                                          1300., 1700., 2100.])

SC1_2_hyd_Ea_profileB = Profile(name='SC1-2-hyd || b',
                                       sample=sample_SC1_2, 
                                       folder=FTIR_file_location,
                                       direction='b', raypath='c',
                                       fnames=['SC1-2-hyd-Ea-b01',
                                               'SC1-2-hyd-Ea-b05',
                                               'SC1-2-hyd-Ea-b09',
                                               'SC1-2-hyd-Ea-b14',
                                               'SC1-2-hyd-Ea-b18'], 
                                       positions_microns=[100., 500., 900.,
                                                          1400., 1800.])

SC1_2_hyd_Ea_profileC = Profile(name='SC1-2-hyd || c',
                                       sample=sample_SC1_2, 
                                       folder=FTIR_file_location,
                                       direction='c', raypath='b',
                                       fnames=['SC1-2-hyd-Ea-c01',
                                               'SC1-2-hyd-Ea-c04',
                                               # too noisy 'SC1-2-hyd-Ea-c06', 
                                               'SC1-2-hyd-Ea-c09',
                                               'SC1-2-hyd-Ea-a09', # -c12
                                               'SC1-2-hyd-Ea-c16',
                                               'SC1-2-hyd-Ea-c19',
                                               'SC1-2-hyd-Ea-c23',
                                               'SC1-2-hyd-Ea-c26',], 
                                       positions_microns=[125., 425., 
                                                          #660., 
                                                          925.,
                                                          1225., 1625., 1925.,
                                                          2325., 2625.])

wb_800C_hyd = Block(name='hydrated San Carlos olivine',
                          profiles=[SC1_2_hyd_Ea_profileA,
                                    SC1_2_hyd_Ea_profileB,
                                    SC1_2_hyd_Ea_profileC],
                          time_seconds=0.00000001,
                          folder=FTIR_file_location)

spec2 = wb_800C_hyd.average_spectra()
spec2.fname = 'SC1-2-hyd-average'
spec2.folder = FTIR_file_location
wb_800C_hyd_averagespec = spec2

#%% SC1-2-800C-1hr
# San Carlos oriented sample SC1-2 dehydrated for 1 hour at 800 C
SC1_2_800C_1hr_profileA = Profile(name='SC1-2-1hr || a',
                                  sample=sample_SC1_2, 
                                  direction='a', raypath='b',
                                  folder=FTIR_file_location,
                                  initial_profile=SC1_2_hyd_Ea_profileA,
                                  fnames=['SC1-2-800C-1hr-a01',
                                          'SC1-2-800C-1hr-a02',
                                          'SC1-2-800C-1hr-a03',
                                          'SC1-2-800C-1hr-a05',
                                          'SC1-2-800C-1hr-a07',
                                          'SC1-2-800C-1hr-a09',
                                          'SC1-2-800C-1hr-a11',
                                          'SC1-2-800C-1hr-a13',
                                          'SC1-2-800C-1hr-a15',
                                          'SC1-2-800C-1hr-a17',
                                          'SC1-2-800C-1hr-a19',
                                          'SC1-2-800C-1hr-a20',
                                          'SC1-2-800C-1hr-a21',], 
                                  positions_microns=[100., 200., 300., 500., 
                                                     700., 900., 1100., 1300., 
                                                     1500., 1700., 1900.,
                                                     2000., 2100.])
                                       
SC1_2_800C_1hr_profileB = Profile(name='SC1-2-1hr || b',
                                  sample=sample_SC1_2,  direction='b', 
                                  raypath='c', folder=FTIR_file_location,
                                  initial_profile=SC1_2_hyd_Ea_profileB,
                                  fnames=['SC1-2-800C-1hr-b01',
                                          'SC1-2-800C-1hr-b02',
                                          'SC1-2-800C-1hr-b03',
                                          'SC1-2-800C-1hr-b05',
                                          'SC1-2-800C-1hr-b07',
                                          'SC1-2-800C-1hr-b09',
                                          'SC1-2-800C-1hr-b12',
                                          'SC1-2-800C-1hr-b14',
                                          'SC1-2-800C-1hr-b16',
                                          'SC1-2-800C-1hr-b17',
                                          'SC1-2-800C-1hr-b18'], 
                                   positions_microns=[100., 200., 300., 500., 
                                                      700., 900., 1200., 1400., 1600.,
                                                      1700., 1800.])

SC1_2_800C_1hr_profileC = Profile(name='SC1-2-1hr || c',
                                  sample=sample_SC1_2, direction='c', 
                                  raypath='b', folder=FTIR_file_location,
                                  initial_profile=SC1_2_hyd_Ea_profileC,
                                  fnames=['SC1-2-800C-1hr-c00',
                                          'SC1-2-800C-1hr-c01',
                                          'SC1-2-800C-1hr-c02',
                                          'SC1-2-800C-1hr-c04',
                                          'SC1-2-800C-1hr-c06',
                                          'SC1-2-800C-1hr-c09',
                                          'SC1-2-800C-1hr-a09', # c12
                                          'SC1-2-800C-1hr-c16',
                                          'SC1-2-800C-1hr-c19',
                                          'SC1-2-800C-1hr-c21',
                                          'SC1-2-800C-1hr-c23',
                                          'SC1-2-800C-1hr-c25',
                                          'SC1-2-800C-1hr-c26',], 
                                  positions_microns=[50., 125., 225., 425., 
                                                     625., 925., 1225., 1625., 
                                                     1925., 2125., 2325., 
                                                     2525., 2625.])

wb_800C_1hr = Block(name='SC1-2 800C 1hr',
                         profiles=[SC1_2_800C_1hr_profileA,
                                   SC1_2_800C_1hr_profileB,
                                   SC1_2_800C_1hr_profileC,],
                         time_seconds=1.*3600.)

#wb_800_1hr_averagespec = wb_800C_hyd.average_spectra()
#.fname = 'SC1-2-hyd-average'
#spec2.folder = FTIR_file_location
 
#%% SC1-2-800C-3hr
# San Carlos oriented sample SC1-2 dehydrated for 3 hours at 800 C
SC1_2_800C_3hr_profileA = Profile(name='SC1-2-3hr || a',
                                       sample=sample_SC1_2, 
                                       direction='a', raypath='b',
                                       folder=FTIR_file_location,
                                       initial_profile=SC1_2_hyd_Ea_profileA,
                                       fnames=['SC1-2-800C-3hr-a01',
                                                   'SC1-2-800C-3hr-a02',
                                                   'SC1-2-800C-3hr-a03',
                                                   'SC1-2-800C-3hr-a05',
                                                   'SC1-2-800C-3hr-a07',
                                                   'SC1-2-800C-3hr-a09',
                                                   'SC1-2-800C-3hr-a11',
                                                   'SC1-2-800C-3hr-a13',
#                                                   'SC1-2-800C-3hr-a15',
                                                   'SC1-2-800C-3hr-a17',
                                                   'SC1-2-800C-3hr-a19',
                                                   'SC1-2-800C-3hr-a20',
                                                   'SC1-2-800C-3hr-a21',], 
                                      positions_microns=[100., 200., 300., 
                                                          500., 700., 900., 
                                                          1100., 1300., #1500.,
                                                          1700., 1900., 2000.,
                                                          2100.])

SC1_2_800C_3hr_profileB = Profile(name='SC1-2-3hr || b',
                                         sample=sample_SC1_2, 
                                         direction='b', raypath='c',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileB,
                                         fnames=['SC1-2-800C-3hr-b01',
                                                     'SC1-2-800C-3hr-b02',
#                                                     'SC1-2-800C-3hr-b03',
                                                     'SC1-2-800C-3hr-b05',
                                                     'SC1-2-800C-3hr-b07',
                                                     'SC1-2-800C-3hr-b09',
                                                     'SC1-2-800C-3hr-b12',
                                                     'SC1-2-800C-3hr-b14',
                                                     'SC1-2-800C-3hr-b16',
                                                     'SC1-2-800C-3hr-b17',
                                                     'SC1-2-800C-3hr-b18'], 
                                       positions_microns=[75., 200., #300., 
                                                          500., 700., 900., 
                                                          1200., 1400., 1600.,
                                                          1700., 1800.])

SC1_2_800C_3hr_profileC = Profile(name='SC1-2-3hr || c',
                                       sample=sample_SC1_2, 
                                       direction='c', raypath='b',
                                       folder=FTIR_file_location,
                                       initial_profile=SC1_2_hyd_Ea_profileC,
                                       fnames=['SC1-2-800C-3hr-c01',
                                                   'SC1-2-800C-3hr-c02',
                                                   'SC1-2-800C-3hr-c04',
                                                   'SC1-2-800C-3hr-c06',
#                                                   'SC1-2-800C-3hr-c09',
                                                   'SC1-2-800C-3hr-a09', # c12
                                                   'SC1-2-800C-3hr-c16',
                                                   'SC1-2-800C-3hr-c19',
                                                   'SC1-2-800C-3hr-c21',
                                                   'SC1-2-800C-3hr-c23',
                                                   'SC1-2-800C-3hr-c25',
                                                   'SC1-2-800C-3hr-c26',], 
                                      positions_microns=[75., 225., 
                                                         425., 625., #960.,
                                                         1225., 1625., 1925.,
                                                         2125., 2325., 2525.,
                                                         2625.])

wb_800C_3hr = Block(name='SC1-2 800C 3hr',
                                profiles=[SC1_2_800C_3hr_profileA,
                                          SC1_2_800C_3hr_profileB,
                                          SC1_2_800C_3hr_profileC,],
                                time_seconds=3.*3600.)

                                                                
#%% San Carlos oriented sample SC1-6
# SC1-6 treated at 10 kbar, 1000 C, Ni-NiO, 3 hr 51 minutes
SC1_6_sample = Sample(length_a_microns=[3491., 3514., 3511., 3516., 3488.], 
                      length_b_microns=[2344., 2340., 2346., 2341., 2351.], 
                      length_c_microns=[2794., 2792., 2795., 2795., 2792.]) 

# polarized spectra with E in 3 orthogonal directions
SC1_6_hyd_Ea = Spectrum(fname='SC1-6-thin-parlong', 
                               folder=FTIR_file_location,
                               thickness_microns=np.mean(sample_SC1_2.length_b_microns))
SC1_6_hyd_Eb = Spectrum(fname='SC1-6-mid-parshort', 
                               folder=FTIR_file_location,
                               thickness_microns=np.mean(sample_SC1_2.length_c_microns))
SC1_6_hyd_Ec = Spectrum(fname='SC1-6-thin-parshort', 
                               folder=FTIR_file_location,
                               thickness_microns=np.mean(sample_SC1_2.length_b_microns))

#%% SC1-2-800C-7hr
# San Carlos oriented sample SC1-2 dehydrated for 7 hours at 800 C
SC1_2_800C_7hr_profileA = Profile(name='SC1-2-7hr || a',
                                       sample=sample_SC1_2, 
                                       direction='a', raypath='b',
                                       folder=FTIR_file_location,
                                       initial_profile=SC1_2_hyd_Ea_profileA,
                                       fnames=['SC1-2-800C-7hr-a01',
                                                   'SC1-2-800C-7hr-a03',
                                                   'SC1-2-800C-7hr-a05',
                                                   'SC1-2-800C-7hr-a07',
                                                   'SC1-2-800C-7hr-a09',
                                                   'SC1-2-800C-7hr-a11',
                                                   'SC1-2-800C-7hr-a13',
                                                   'SC1-2-800C-7hr-a15',
                                                   'SC1-2-800C-7hr-a17',
                                                   'SC1-2-800C-7hr-a19',
                                                   'SC1-2-800C-7hr-a21',], 
                                      positions_microns=[100., 300., 
                                                          500., 700., 900., 
                                                          1100., 1300., 1500.,
                                                          1700., 1900., 2100.])

SC1_2_800C_7hr_profileB = Profile(name='SC1-2-7hr || b',
                                         sample=sample_SC1_2, 
                                         direction='b', raypath='c',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileB,
                                         fnames=['SC1-2-800C-7hr-b01',
                                                     'SC1-2-800C-7hr-b03',
                                                     'SC1-2-800C-7hr-b05',
                                                     'SC1-2-800C-7hr-b07',
                                                     'SC1-2-800C-7hr-b09',
                                                     'SC1-2-800C-7hr-b11',
                                                     'SC1-2-800C-7hr-b13',
                                                     'SC1-2-800C-7hr-b15',
                                                     'SC1-2-800C-7hr-b18'], 
                                       positions_microns=[100., 300., 
                                                          500., 700., 900., 
                                                          1100., 1300., 1500.,
                                                          1800.])

SC1_2_800C_7hr_profileC = Profile(name='SC1-2-7hr || c',
                                         sample=sample_SC1_2, 
                                         direction='c', raypath='b',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileC,
                                         fnames=['SC1-2-800C-7hr-c00-copper',
                                                     'SC1-2-800C-7hr-c02-copper',
                                                     'SC1-2-800C-7hr-c04-copper',
                                                     'SC1-2-800C-7hr-c06-copper',
                                                     'SC1-2-800C-7hr-c08-copper',
                                                     'SC1-2-800C-7hr-c10',
                                                     'SC1-2-800C-7hr-c12', 
#                                                     'SC1-2-800C-7hr-c14',
                                                     'SC1-2-800C-7hr-c16',
                                                     'SC1-2-800C-7hr-c18',
                                                     'SC1-2-800C-7hr-c20',
                                                     'SC1-2-800C-7hr-c22',
                                                     'SC1-2-800C-7hr-c24',
                                                     'SC1-2-800C-7hr-c2526',
                                                     'SC1-2-800C-7hr-c27',], 
                                      positions_microns=[75., 225., 425., 
                                                         625., 825., 1025.,
                                                         1225.,     1625.,
                                                         1825., 2025., 2225.,
                                                         2425., 2575., 2786.])

wb_800C_7hr = Block(name='SC1-2 800C 7hr',
                                profiles=[SC1_2_800C_7hr_profileA,
                                          SC1_2_800C_7hr_profileB,
                                          SC1_2_800C_7hr_profileC,],
                                time_seconds=7.*3600.)

#%% hydrated SC1-6 initial profiles, IR polarized || a
SC1_6_hyd_profileA = Profile(name='SC1-6-hyd || a',
                                    sample=SC1_6_sample, 
                                    folder=FTIR_file_location,
                                    direction='a', raypath='b',
                                    fnames=['SC1-6-hyd-a01',
                                                'SC1-6-hyd-a05',
                                                'SC1-6-hyd-a10',
                                                'SC1-6-hyd-a15',
                                                'SC1-6-hyd-a20',
                                                'SC1-6-hyd-a25',
                                                'SC1-6-hyd-a30',
                                                'SC1-6-hyd-a33',
                                                'SC1-6-hyd-a34',
                                                ], 
                                       positions_microns=[75., 450., 950.,
                                                          1450., 1950., 2450.,
                                                          2950., 3250., 3429.])
#
SC1_6_hyd_profileB = Profile(name='SC1-6-hyd || b',
                                    sample=SC1_6_sample, 
                                    folder=FTIR_file_location,
                                    direction='b', raypath='c',
                                    fnames=['SC1-6-hyd-b01',
                                                'SC1-6-hyd-b04',
                                                'SC1-6-hyd-b08',
                                                'SC1-6-hyd-b12',
                                                'SC1-6-hyd-b16',
                                                'SC1-6-hyd-b20',
                                                'SC1-6-hyd-b23',
                                                ], 
                                       positions_microns=[75., 350., 750.,
                                                          1150., 1550., 1950.,
                                                          2269.])

SC1_6_hyd_profileC = Profile(name='SC1-6-hyd || c',
                                       sample=SC1_6_sample, 
                                       folder=FTIR_file_location,
                                       direction='c', raypath='b',
                                       fnames=['SC1-6-hyd-c01',
#                                                   'SC1-6-hyd-c04',
                                                   'SC1-6-hyd-c08',
                                                   'SC1-6-hyd-c12',
                                                   'SC1-6-hyd-c16',
                                                   'SC1-6-hyd-c20',
                                                   'SC1-6-hyd-c24',
                                                   'SC1-6-hyd-c28',], 
                                       positions_microns=[75., #350., 
                                                          750.,
                                                          1150., 1550., 1950.,
                                                          2350., 2719.])

wb_1000C_SC1_6 = Block(profiles=[SC1_6_hyd_profileA,
                                             SC1_6_hyd_profileB,
                                             SC1_6_hyd_profileC],
                                   time_seconds=4.*3600.,
                                   name=''.join(('SC1-6 hydrated 10 kbar,',
                                                 ' 1000 C, Ni-NiO,',
                                                 ' 3 hr 51 minutes')))

#%% SC1-2-800C-13hr
# San Carlos oriented sample SC1-2 dehydrated for 13 hours at 800 C, NNO
SC1_2_800C_13hr_profileA = Profile(name='SC1-2-13hr || a',
                                       sample=sample_SC1_2, 
                                       direction='a', raypath='b',
                                       folder=FTIR_file_location,
                                       initial_profile=SC1_2_hyd_Ea_profileA,
                                       fnames=['SC1-2-800C-13hr-a01',
                                                   'SC1-2-800C-13hr-a03',
                                                   'SC1-2-800C-13hr-a05',
                                                   'SC1-2-800C-13hr-a07',
                                                   'SC1-2-800C-13hr-a09',
                                                   'SC1-2-800C-13hr-a11',
                                                   'SC1-2-800C-13hr-a13',
                                                   'SC1-2-800C-13hr-a15',
                                                   'SC1-2-800C-13hr-a17',
                                                   'SC1-2-800C-13hr-a19',
                                                   'SC1-2-800C-13hr-a21',], 
                                      positions_microns=[100., 300., 
                                                         500., 700., 900., 
                                                         1100., 1300., 1500.,
                                                         1700., 1900., 2100.])

SC1_2_800C_13hr_profileB = Profile(name='SC1-2-13hr || b',
                                         sample=sample_SC1_2, 
                                         direction='b', raypath='c',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileB,
                                         fnames=['SC1-2-800C-13hr-b01',
                                                     'SC1-2-800C-13hr-b03',
                                                     'SC1-2-800C-13hr-b05',
                                                     'SC1-2-800C-13hr-b07',
                                                     'SC1-2-800C-13hr-b09',
                                                     'SC1-2-800C-13hr-b11',
                                                     'SC1-2-800C-13hr-b13',
                                                     'SC1-2-800C-13hr-b15',
                                                     'SC1-2-800C-13hr-b18'], 
                                       positions_microns=[100., 300., 
                                                          500., 700., 900., 
                                                          1100., 1300., 1500.,
                                                          1800.])

SC1_2_800C_13hr_profileC = Profile(name='SC1-2-13hr || c',
                                         sample=sample_SC1_2, 
                                         direction='c', raypath='b',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileC,
                                         fnames=['SC1-2-800C-13hr-c00',
                                                     'SC1-2-800C-13hr-c02',
                                                     'SC1-2-800C-13hr-c04',
                                                     'SC1-2-800C-13hr-c06',
                                                     'SC1-2-800C-13hr-c08',
                                                     'SC1-2-800C-13hr-c10',
                                                     'SC1-2-800C-13hr-c12', 
#                                                     'SC1-2-800C-13hr-c14',
                                                     'SC1-2-800C-13hr-c16',
                                                     'SC1-2-800C-13hr-c18',
                                                     'SC1-2-800C-13hr-c20',
                                                     'SC1-2-800C-13hr-c22',
                                                     'SC1-2-800C-13hr-c24',
                                                     'SC1-2-800C-13hr-c2526',
                                                     'SC1-2-800C-13hr-c27',], 
                                      positions_microns=[75., 225., 425., 
                                                         625., 825., 1025.,
                                                         1225.,     1625.,
                                                         1825., 2025., 2225.,
                                                         2425., 2575., 2786.])

wb_800C_13hr = Block(name='SC1-2 800C 13hr',
                                profiles=[SC1_2_800C_13hr_profileA,
                                          SC1_2_800C_13hr_profileB,
                                          SC1_2_800C_13hr_profileC,],
                                time_seconds=13.*3600.)

#%% oriented San Carlos olivine piece SC1-7
SC1_7_sample = Sample(length_a_microns=[2788., 2791., 2793., 2789., 2791.],
                      length_b_microns=[1092., 1092., 1086., 1094., 1089.],
                      length_c_microns=[3048., 3084., 2980., 3065., 3036.])

#%% hydrated SC1-7 
SC1_7_hyd_profileA = Profile(name='SC1-7-hyd || a',
                                    sample=SC1_7_sample, 
                                    folder=FTIR_file_location,
                                    direction='a', raypath='b',
                                    fnames=['SC1-7-hyd-a01', 
                                                'SC1-7-hyd-a03',
                                                'SC1-7-hyd-a05',
                                                'SC1-7-hyd-a08',
                                                'SC1-7-hyd-a11',
                                                'SC1-7-hyd-a14',
                                                'SC1-7-hyd-a17',
                                                'SC1-7-hyd-a21',
                                                'SC1-7-hyd-a23',
                                                'SC1-7-hyd-a25',
                                                'SC1-7-hyd-a27',
                                                ], 
                                       positions_microns=[75., 275., 475.,
                                                          775., 1075., 1375.,
                                                          1675., 2075., 2275.,
                                                          2475., 2715.])

SC1_7_hyd_profileB = Profile(name='SC1-7-hyd || b',
                                       sample=SC1_7_sample, 
                                       folder=FTIR_file_location,
                                       direction='b', raypath='c',
                                       fnames=[
                                                   'SC1-7-hyd-b03',
                                                   'SC1-7-hyd-b05',
                                                   'SC1-7-hyd-b09',
                                                   ], 
                                       positions_microns=[300., 500., 900.,])

SC1_7_hyd_profileC = Profile(name='SC1-7-hyd || c',
                                       sample=SC1_7_sample, 
                                       folder=FTIR_file_location,
                                       direction='c', raypath='b',
                                       fnames=['SC1-7-hyd-c01',
                                                   'SC1-7-hyd-c03',
                                                   'SC1-7-hyd-c05',
                                                   'SC1-7-hyd-c08',
                                                   'SC1-7-hyd-c11',
                                                   'SC1-7-hyd-c14',
                                                   'SC1-7-hyd-c17',
                                                   'SC1-7-hyd-c21',
                                                   'SC1-7-hyd-c23',
                                                   'SC1-7-hyd-c25',
                                                   'SC1-7-hyd-c27',
                                                   'SC1-7-hyd-c29',
                                                   ], 
                                       positions_microns=[75., 275., 475.,
                                                          775., 1075., 1375., 
                                                          1675., 2075., 2275.,
                                                          2475., 2675., 2968.])

wb_1000C_SC1_7 = Block(profiles=[SC1_7_hyd_profileA,
                                             SC1_7_hyd_profileB,
                                             SC1_7_hyd_profileC],
                                   time_seconds=7.*3600.,
                                   name=''.join(('SC1-7 hydrated 10 kbar,',
                                                 ' 1000 C, Ni-NiO,',
                                                 ' 7 hours'))) # confirm in notes

spec7 = wb_1000C_SC1_7.average_spectra()
spec7.fname = 'SC1-7-average'
spec7.folder = FTIR_file_location
#%% SC1-2-800C-19hr
# San Carlos oriented sample SC1-2 dehydrated for 19 hours at 800 C, NNO
SC1_2_800C_19hr_profileA = Profile(name='SC1-2-19hr || a',
                                       sample=sample_SC1_2, 
                                       direction='a', raypath='b',
                                       folder=FTIR_file_location,
                                       initial_profile=SC1_2_hyd_Ea_profileA,
                                       fnames=['SC1-2-800C-19hr-a01',
                                                   'SC1-2-800C-19hr-a03',
                                                   'SC1-2-800C-19hr-a05',
                                                   'SC1-2-800C-19hr-a07',
                                                   'SC1-2-800C-19hr-a09',
                                                   'SC1-2-800C-19hr-a11',
                                                   'SC1-2-800C-19hr-a13',
                                                   'SC1-2-800C-19hr-a15',
                                                   'SC1-2-800C-19hr-a17',
                                                   'SC1-2-800C-19hr-a19',
                                                   'SC1-2-800C-19hr-a21',], 
                                      positions_microns=[100., 300., 
                                                         500., 700., 900., 
                                                         1100., 1300., 1500.,
                                                         1700., 1900., 2100.])

SC1_2_800C_19hr_profileB = Profile(name='SC1-2-19hr || b',
                                         sample=sample_SC1_2, 
                                         direction='b', raypath='c',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileB,
                                         fnames=['SC1-2-800C-19hr-b01',
                                                     'SC1-2-800C-19hr-b03',
                                                     'SC1-2-800C-19hr-b05',
                                                     'SC1-2-800C-19hr-b07',
#                                                     'SC1-2-800C-19hr-b09',
                                                     'SC1-2-800C-19hr-b11',
                                                     'SC1-2-800C-19hr-b13',
                                                     'SC1-2-800C-19hr-b15',
                                                     'SC1-2-800C-19hr-b18'], 
                                       positions_microns=[100., 300., 
                                                          500., 700., #900., 
                                                          1100., 1300., 1500.,
                                                          1800.])

SC1_2_800C_19hr_profileC = Profile(name='SC1-2-19hr || c',
                                         sample=sample_SC1_2, 
                                         direction='c', raypath='b',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileC,
                                         fnames=['SC1-2-800C-19hr-c00',
                                                     'SC1-2-800C-19hr-c02',
                                                     'SC1-2-800C-19hr-c04',
                                                     'SC1-2-800C-19hr-c06',
                                                     'SC1-2-800C-19hr-c08',
                                                     'SC1-2-800C-19hr-c10',
                                                     'SC1-2-800C-19hr-c12', 
#                                                     'SC1-2-800C-19hr-c14',
                                                     'SC1-2-800C-19hr-c16',
                                                     'SC1-2-800C-19hr-c18',
                                                     'SC1-2-800C-19hr-c20',
                                                     'SC1-2-800C-19hr-c22',
                                                     'SC1-2-800C-19hr-c24',
                                                     'SC1-2-800C-19hr-c2526',
                                                     'SC1-2-800C-19hr-c27',], 
                                      positions_microns=[75., 225., 425., 
                                                         625., 825., 1025.,
                                                         1225.,     1625.,
                                                         1825., 2025., 2225.,
                                                         2425., 2575., 2786.])

wb_800C_19hr = Block(name='SC1-2 800C 19hr',
                                profiles=[SC1_2_800C_19hr_profileA,
                                          SC1_2_800C_19hr_profileB,
                                          SC1_2_800C_19hr_profileC,],
                                time_seconds=19.*3600.)

#%% SC1-2-800C-43hr
# San Carlos oriented sample SC1-2 dehydrated for 43 hours at 800 C, NNO
SC1_2_800C_43hr_profileA = Profile(name='SC1-2-43hr || a',
                                       sample=sample_SC1_2, 
                                       direction='a', raypath='b',
                                       folder=FTIR_file_location,
                                       initial_profile=SC1_2_hyd_Ea_profileA,
                                       fnames=['SC1-2-800C-43hr-a01',
                                                   'SC1-2-800C-43hr-a03',
                                                   'SC1-2-800C-43hr-a05',
                                                   'SC1-2-800C-43hr-a07',
                                                   'SC1-2-800C-43hr-a09',
                                                   'SC1-2-800C-43hr-a11',
                                                   'SC1-2-800C-43hr-a13',
                                                   'SC1-2-800C-43hr-a15',
                                                   'SC1-2-800C-43hr-a17',
                                                   'SC1-2-800C-43hr-a19',
                                                   'SC1-2-800C-43hr-a21',], 
                                      positions_microns=[100., 300., 
                                                         500., 700., 900., 
                                                         1100., 1300., 1500.,
                                                         1700., 1900., 2100.])

SC1_2_800C_43hr_profileB = Profile(name='SC1-2-43hr || b',
                                         sample=sample_SC1_2, 
                                         direction='b', raypath='c',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileB,
                                         fnames=['SC1-2-800C-43hr-b01',
                                                     'SC1-2-800C-43hr-b03',
                                                     'SC1-2-800C-43hr-b05',
                                                     'SC1-2-800C-43hr-b07',
                                                     'SC1-2-800C-43hr-b09',
                                                     'SC1-2-800C-43hr-b11',
                                                     'SC1-2-800C-43hr-b13',
                                                     'SC1-2-800C-43hr-b15',
                                                     'SC1-2-800C-43hr-b18'], 
                                       positions_microns=[100., 300., 
                                                          500., 700., 900., 
                                                          1100., 1300., 
                                                          1500., 1800.])

SC1_2_800C_43hr_profileC = Profile(name='SC1-2-43hr || c',
                                         sample=sample_SC1_2, 
                                         direction='c', raypath='b',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileC,
                                         fnames=['SC1-2-800C-43hr-c00',
                                                     'SC1-2-800C-43hr-c02',
                                                     'SC1-2-800C-43hr-c04',
                                                     'SC1-2-800C-43hr-c06',
                                                     'SC1-2-800C-43hr-c08',
                                                     'SC1-2-800C-43hr-c10',
                                                     'SC1-2-800C-43hr-c12', 
#                                                     'SC1-2-800C-43hr-c14',
                                                     'SC1-2-800C-43hr-c16',
                                                     'SC1-2-800C-43hr-c18',
                                                     'SC1-2-800C-43hr-c20',
                                                     'SC1-2-800C-43hr-c22',
                                                     'SC1-2-800C-43hr-c24',
                                                     'SC1-2-800C-43hr-c2526',
                                                     'SC1-2-800C-43hr-c27',], 
                                      positions_microns=[75., 225., 425., 
                                                         625., 825., 1025.,
                                                         1225.,     1625.,
                                                         1825., 2025., 2225.,
                                                         2425., 2575., 2786.])

wb_800C_43hr = Block(name='SC1-2 800C 43hr',
                                profiles=[SC1_2_800C_43hr_profileA,
                                          SC1_2_800C_43hr_profileB,
                                          SC1_2_800C_43hr_profileC,],
                                time_seconds=43.*3600.)

#%% SC1-2-800C-68hr
# San Carlos oriented sample SC1-2 dehydrated for 68 hours at 800 C, NNO
SC1_2_800C_68hr_profileA = Profile(name='SC1-2-68hr || a',
                                       sample=sample_SC1_2, 
                                       direction='a', raypath='b',
                                       folder=FTIR_file_location,
                                       initial_profile=SC1_2_hyd_Ea_profileA,
                                       fnames=['SC1-2-800C-68hr-a01',
                                                   'SC1-2-800C-68hr-a03',
                                                   'SC1-2-800C-68hr-a05',
                                                   'SC1-2-800C-68hr-a07',
                                                   'SC1-2-800C-68hr-a09',
                                                   'SC1-2-800C-68hr-a11',
                                                   'SC1-2-800C-68hr-a13',
                                                   'SC1-2-800C-68hr-a15',
                                                   'SC1-2-800C-68hr-a17',
                                                   'SC1-2-800C-68hr-a19',
                                                   'SC1-2-800C-68hr-a21',], 
                                      positions_microns=[100., 300., 
                                                         500., 700., 900., 
                                                         1100., 1300., 1500.,
                                                         1700., 1900., 2100.])

SC1_2_800C_68hr_profileB = Profile(name='SC1-2-68hr || b',
                                         sample=sample_SC1_2, 
                                         direction='b', raypath='c',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileB,
                                         fnames=['SC1-2-800C-68hr-b01',
                                                     'SC1-2-800C-68hr-b03',
                                                     'SC1-2-800C-68hr-b05',
                                                     'SC1-2-800C-68hr-b07',
                                                     'SC1-2-800C-68hr-b09',
                                                     'SC1-2-800C-68hr-b11',
#                                                     'SC1-2-800C-68hr-b13',
                                                     'SC1-2-800C-68hr-b15',
                                                     'SC1-2-800C-68hr-b18'], 
                                       positions_microns=[100., 300., 
                                                          500., 700., 900., 
                                                          1100., #1300., 
                                                          1500., 1800.])

SC1_2_800C_68hr_profileC = Profile(name='SC1-2-68hr || c',
                                         sample=sample_SC1_2, 
                                         direction='c', raypath='b',
                                         folder=FTIR_file_location,
                                         initial_profile=SC1_2_hyd_Ea_profileC,
                                         fnames=['SC1-2-800C-68hr-c00',
                                                     'SC1-2-800C-68hr-c02',
                                                     'SC1-2-800C-68hr-c04',
                                                     'SC1-2-800C-68hr-c06',
                                                     'SC1-2-800C-68hr-c08',
                                                     'SC1-2-800C-68hr-c10',
                                                     'SC1-2-800C-68hr-c12', 
#                                                     'SC1-2-800C-68hr-c14',
                                                     'SC1-2-800C-68hr-c16',
                                                     'SC1-2-800C-68hr-c18',
                                                     'SC1-2-800C-68hr-c20',
                                                     'SC1-2-800C-68hr-c22',
                                                     'SC1-2-800C-68hr-c24',
                                                     'SC1-2-800C-68hr-c2526',
                                                     'SC1-2-800C-68hr-c27',], 
                                      positions_microns=[75., 225., 425., 
                                                         625., 825., 1025.,
                                                         1225.,     1625.,
                                                         1825., 2025., 2225.,
                                                         2425., 2575., 2786.])

wb_800C_68hr = Block(name='SC1-2 800C 68hr',
                                profiles=[SC1_2_800C_68hr_profileA,
                                          SC1_2_800C_68hr_profileB,
                                          SC1_2_800C_68hr_profileC,],
                                time_seconds=68.*3600.
                                )
      

SC_final_averaged = wb_800C_68hr.profiles[0].average_spectra()
SC_final_averaged.thickness_microns = wb_800C_68hr.profiles[0].thicknesses_microns
SC_final_averaged.fname = 'SC_final_averaged'
SC_final_averaged.folder = wb_800C_68hr.profiles[0].folder
SC_final_averaged.save_spectrum(printout=False)
SC_final_averaged.start_at_zero()
#%% lists for plotting elsewhere
whole_block_list = [wb_800C_1hr, wb_800C_3hr, wb_800C_7hr, wb_800C_13hr, 
                    wb_800C_19hr, wb_800C_43hr, wb_800C_68hr]
whole_block_label_list = ['hydrated', '1hr', '3hr', '7hr', '13hr', '19hr', 
                          '43hr', '68hr']

#%% Set up peak_heights and positions
peaks = [3600, 3525, 3356, 3236]
for wb in [wb_1000C_SC1_7, wb_800C_hyd, wb_800C_1hr, wb_800C_3hr,
           wb_800C_7hr, wb_800C_13hr, wb_800C_19hr, wb_800C_43hr,
           wb_800C_68hr]:
    wb.get_baselines()
    for prof in wb.profiles:
        prof.peakpos = peaks
        prof.peak_heights = [[]]*len(peaks)    
        for pidx, peak in enumerate(peaks): 
            prof.peak_heights[pidx] = []
            for spec in prof.spectra:
                idx = np.abs(peak - spec.base_wn).argmin()
                height = spec.abs_nobase_cm[idx]
                prof.peak_heights[pidx].append(height)
