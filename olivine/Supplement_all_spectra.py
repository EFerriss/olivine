# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:55:19 2017

@author: Elizabeth Ferriss

Show all FTIR spectra and baselines used for olivine dehydration project
"""
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
from matplotlib.backends.backend_pdf import PdfPages
import os
import pandas as pd
import pynams
import numpy as np
import olivine
import matplotlib.pyplot as plt
from pynams import styles

filetosave = os.path.join(olivine.__path__[0], 'Supplement_all_spectra.pdf')

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
SCcolors = ['#2ca02c'] * len(SC_whole_block_list)
Kcolors = ['darkmagenta'] * len(kiki_whole_block_list)
colors = SCcolors + Kcolors

# get baselines and areas
for wb, color, peaks in zip(wblist, colors, peaks_list):
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=peaks)
    wb.areas = [prof.areas for prof in wb.profiles]
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]
    wb.style = styles.style_points.copy()
    wb.style['color'] = color
    wb.style['markeredgecolor'] = color
    
for wb in SC_whole_block_list:
    wb.sample.name = 'SC1-2'

for wb in kiki_whole_block_list:
    wb.sample.name = 'kiki'
    
#%%# get diffusivity data from spreadsheet
# store log10 diffusivities in wholeblock attribute D3
datafile = os.path.join(pynams.__path__[0], 'diffusion', 'literaturevalues.csv')
diffs = pd.read_csv(datafile)
diffs = diffs.dropna(how='all') # ignore empty rows
diffs.fillna(0, inplace=True) # replace missing values with zero

diffs['hours'] = diffs['hours'].astype(float)

peak2mech = {None: 'bulk', 3600:'[Si]', 3525:'[Ti]', 3356:'[tri]', 3236:'[Mg]'}
peak2idx = {None: None, 3600: 0, 3525: 1, 3356: 2, 3236:3}
peak2fin = {None: 0.15, 3600: 0.4, 3525: 0, 3356: 0, 3236: 0.}

#% plot by peak and wholeblock group and save to pdf
pdf = PdfPages(filetosave)

### San Carlos
peaks = [None] + SCpeaks

for peak in peaks:
    idx = peak2idx[peak]
    mech = peak2mech[peak]
    
    if peak is None:
        height = False
    else:
        height = True
        
    for wb in SC_whole_block_list:
        # plot data        
        fig, ax3 = wb.plot_areas_3panels(styles3=[wb.style]*3, 
                                         centered=True, 
                                         peak_idx = idx,
                                         heights_instead=height,
                                         wholeblock=True, 
                                         scale=1, 
                                         ytop = 1.4,
                                         show_line_at_1=True)

        # get diffusivity data from spreadsheet and plot
        wb.hours = wb.time_seconds / 3600.
        df = diffs[diffs['name'] == wb.sample.name]
        df = df[df['celsius'] == wb.celsius]
        df = df[df['hours'] == wb.hours]
        df = df[df['mechanism'] == mech]
        D3 = list(df.log10D)
        hyd = list(df.Experiment)
        
        if (0 not in D3) and ('dehydration' in hyd):
            fin = peak2fin[peak]
            wb.plot_diffusion(axes3=ax3, show_data=False,
                              wholeblock_diffusion=True, 
                              fin = fin,
                              log10D_m2s=D3, labelD=True,
                              labelDy=1.275)
        ax3[1].set_title(' '.join((wb.name, ax3[1].get_title())))
        fig.subplots_adjust(bottom=0.3)
        pdf.savefig()
        plt.close()

# Kilauea Iki
pvlist = [0, 0, 97, 97, 97, 97, 95]
ytops = [2., 2.5, 1.5, 1.5, 1.5]
peaks = [None, 3600, 3525, 3356]
#peaks = [3356]
#ytops = [1.2]*6
temps = [800, 800] + [1000]*5

for peak, ytop in zip(peaks, ytops):
    idx = peak2idx[peak]
    mech = peak2mech[peak]
    
    if peak is None:
        height = False
    else:
        height = True
        
    for wb, pv, temp in zip(kiki_whole_block_list, pvlist, temps):
        # plot data        
        if wb.celsius == 1000:
            ytop = 1.25
        fig, ax3 = wb.plot_areas_3panels(styles3=[wb.style]*3, 
                                         centered=True, 
                                         peak_idx = idx,
                                         heights_instead=height,
                                         wholeblock=True, 
                                         scale=1, 
                                         ytop = ytop,
                                         show_line_at_1=True)

        # get diffusivity data from spreadsheet and plot
        wb.hours = wb.time_seconds / 3600.
        df = diffs[diffs['name'] == wb.sample.name]
        df = df[df['celsius'] == wb.celsius]
        df = df[df['hours'] == wb.hours]
        df = df[df['mechanism'] == mech]
        D3 = list(df.log10D)
        hyd = list(df.Experiment)
        if (0 not in D3) and ('dehydration' in hyd):
            wb.plot_diffusion(axes3=ax3, show_data=False,
                              wholeblock_diffusion=True, 
                              log10D_m2s=D3, labelD=True,
                              labelDy=ytop-ytop*0.08)
        ax3[1].set_title(' '.join((wb.name, ax3[1].get_title())))
        fig.subplots_adjust(bottom=0.3)
        pdf.savefig()
        plt.close()


## individual spectra and baselines
wblist = [SC.wb_1000C_SC1_7] + SC_whole_block_list + kiki_whole_block_list
           
ytops = np.ones_like(wblist) * 0.5
ytops[0] = 1.4
ytops[9:] = 1.
for ytop, wb in zip(ytops, wblist):
    for R, orient, prof in zip(wb.raypaths, wb.directions, wb.profiles):
        for loc, spec in zip(prof.positions_microns, prof.spectra):
            spec.get_baseline()
            fig, ax = spec.plot_showbaseline()
            ax.set_ylim(0, ytop)
            ax.set_title(''.join((wb.name, '\n',
                                  '{:.1f}'.format(loc), ' $\mu$m along ', 
                                  orient, ', R || ', str(R)
                                    )))
            pdf.savefig()
            plt.close()
#
pdf.close()
#%%
def spit(D3):
    for D in D3:
        print('{:.1f}'.format(D))