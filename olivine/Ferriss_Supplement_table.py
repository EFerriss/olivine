# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:55:19 2017

@author: Elizabeth Ferriss

Print to csv all data in Supplement for Ferriss et al. GCA H diffusion paper
"""
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
import os
import numpy as np
import olivine

filetosave = os.path.join(olivine.__path__[0], 
                          'Ferriss_Supplement_astable.csv')

try:
    os.remove(filetosave)
except OSError:
    pass

line = ','.join(('sample name', 'peak location (cm^-1)', 
                 'temperature (Celsius)', 'hours dehydrated', 
                 'traverse direction', 'raypath direction', 
                 'position (microns)', 'area/initial or height/initial',
                 'FTIR spectrum filename','\n'))
with open(filetosave, 'a') as csvfile:
    csvfile.write(line)

SC_whole_block_list = [SC.wb_800C_hyd] + SC.whole_block_list.copy()

kiki_whole_block_list = [kiki.wb_Kiki_init,
                         kiki.wb_Kiki_1hr, 
                         kiki.wb_Kiki_8hr,
                         kiki.wb_Kiki_1000C_3hr, 
                         kiki.wb_Kiki_1000C_6hr, 
                         kiki.wb_Kiki_1000C_7hr, 
                         kiki.wb_Kiki_1000C_8hr,
                         ]

wblist = SC_whole_block_list + kiki_whole_block_list

SCpeaks = [3600, 3525]
Kpeaks = kiki.peaks
init_peaks_list = [SCpeaks, SCpeaks, Kpeaks]
SCpeaks_list = [SCpeaks] * len(SC_whole_block_list)
Kpeaks_list = [Kpeaks] * len(kiki_whole_block_list)
peaks_list = SCpeaks_list + Kpeaks_list

# get baselines and areas
for wb, peaks in zip(wblist, peaks_list):
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=peaks)
    
for wb in SC_whole_block_list:
    wb.sample.name = 'SC1-2'

for wb in kiki_whole_block_list:
    wb.sample.name = 'kiki'

peak2idx = {'total H': None, 3600: 0, 3525: 1, 3356: 2, 3236:3}


######## San Carlos ########
peaks = ['total H'] + SCpeaks

for peak in peaks:
    idx = peak2idx[peak]
    
    if peak is None:
        height = False
    else:
        height = True
        
    for wb in SC_whole_block_list:
        if np.isclose(wb.time_seconds/3600, 17.4):
            time = 'hydrated'
        else:
            time = str(wb.time_seconds/3600)
            
        if peak == 'total H':
            height = False
        else:
            height = True
            
        xlist, ylist = wb.xy_picker(peak_idx=peak2idx[peak], wholeblock=True, 
                                    heights_instead=height)
                
        for i, prof in enumerate(wb.profiles):
            for x, y, spectrum in zip(xlist[i], ylist[i], prof.spectra):
                specfile = ''.join((spectrum.fname, '.csv'))
                line = ','.join((wb.sample.name, str(peak), str(wb.celsius), 
                                 time, prof.direction, prof.raypath, 
                                 '{:.1f}'.format(x), '{:.3f}'.format(y), 
                                 specfile, '\n'))
                with open(filetosave, 'a') as csvfile:
                    csvfile.write(line)
                

####### Kilauea Iki ##########
peaks = ['total H', 3600, 3525, 3356]
temps = [800, 800] + [1000]*5

for peak in peaks:
    if peak is None:
        height = False
    else:
        height = True

    for wb, temp in zip(kiki_whole_block_list, temps):
        xlist, ylist = wb.xy_picker(peak_idx=peak2idx[peak], wholeblock=True, 
                                    heights_instead=height)
                
        for i, prof in enumerate(wb.profiles):
            for x, y, spectrum in zip(xlist[i], ylist[i], prof.spectra):
                specfile = ''.join((spectrum.fname, '.csv'))
                line = ','.join((wb.sample.name, str(peak), str(wb.celsius), 
                                 time, prof.direction, prof.raypath, 
                                 '{:.1f}'.format(x), '{:.3f}'.format(y), specfile, '\n'))
                with open(filetosave, 'a') as csvfile:
                    csvfile.write(line)
