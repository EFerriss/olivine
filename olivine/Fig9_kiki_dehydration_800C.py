# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Modified paper figure to emphasize absolute changes in peak heights
"""
from __future__ import print_function, division
from olivine.KilaueaIki import Kiki_spectra as kiki
import itertools
import matplotlib.pyplot as plt
import os
import olivine
import numpy as np
import string

file = os.path.join(olivine.__path__[0], 'Fig9_kiki_peakchanges_800.tif')

wbdata = kiki.wb_Kiki_8hr

wbs = [kiki.wb_Kiki_init,
       kiki.wb_Kiki_8hr
       ]

hours = wbdata.time_seconds/3600.

for wb in wbs:
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=kiki.peaks)
    wb.diffs = []

conversion_factor_area2water = 0.6 # see Table1_concentrations.py
profidx = itertools.cycle([0, 1, 2])
for wb in wbs:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
        wb.areas[next(profidx)] = prof.areas

for prof, iprof in zip(wbdata.profiles, kiki.wb_Kiki_init.profiles):
    prof.initial_profile = iprof

#%% the figure
mechs = ['total', '[tri]', '[Ti]', '[Si]']

# set styles
style = {'linestyle':'None'}
style['markeredgecolor'] = 'darkmagenta'
style['markersize'] = 4
styles = [style.copy(), style.copy()]
styles[0]['marker'] = 'o'
styles[1]['marker'] = 's'
styles[0]['markerfacecolor'] = 'darkmagenta'
styles[1]['markerfacecolor'] = 'none'
styles[1]['label'] = 'heated 8hr'
styles[0]['label'] = 'initial'
     
fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.13
ypstart = 0.1
wgap = 0.005
width = 0.27
height = 0.18
hgap = 0.02
ytxt_shifts = [0.2, 0.2, 0.2, 0.7, 0.2]
axes = []
for peak in range(len(mechs)):
    ax1 = fig.add_axes([xstart, ypstart, width, height])
    ax2 = fig.add_axes([xstart+width+wgap, ypstart, width, height])
    ax3 = fig.add_axes([xstart+2*width+2*wgap, ypstart, width, height])
    axes.append([ax1, ax2, ax3])
    ypstart = ypstart + hgap + height

# label the axes    
for idx, ax3 in enumerate(axes):
    for ax in ax3:
        if idx != 0:
            ax.axes.get_xaxis().set_ticks([])
    ax3[1].axes.get_yaxis().set_ticks([])
    ax3[2].axes.get_yaxis().set_ticks([])
axes[0][0].set_xlabel('x (mm)')
axes[0][1].set_xlabel('y (mm)')
axes[0][2].set_xlabel('z (mm)')
axes[3][0].set_ylabel('total\nhydrogen (cm$^{-2}$)')
axes[0][0].set_ylabel('[Si-4H]\nheight (cm$^{-1}$)')
axes[1][0].set_ylabel('[Ti-2H]\nheight (cm$^{-1}$)')
axes[2][0].set_ylabel('[Fe$^{3+}$-H]\nheight (cm$^{-1}$)')

# total water data
idx = -1
for wb, style in zip(wbs, styles):
    wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                          centered=True, show_errorbars=False,
                          wholeblock=False)
for idx, ax in enumerate(axes[idx]):
    ax.set_title(''.join(('|| ', wbdata.directions[idx],
                          ', R || ', wbdata.raypaths[idx])))

# peak height data
for idx in [0, 1, 2]:
    for wb, style in zip(wbs, styles):
        wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                              centered=True, show_errorbars=False,
                              wholeblock=False, heights_instead=True,
                              peak_idx=idx)   


# initial and final overall values        
totalH_initial = np.mean(list(itertools.chain(*kiki.wb_Kiki_init.areas)))
totalH_final = np.mean(list(itertools.chain(*kiki.wb_Kiki_8hr.areas)))

for wb in wbs:
    wb.peakpos = wb.profiles[0].peakpos
    wb.peakSi = [prof.peak_heights[0] for prof in wb.profiles]
    wb.peakTi = [prof.peak_heights[1] for prof in wb.profiles]
    wb.peakTri = [prof.peak_heights[2] for prof in wb.profiles]
    wb.peakSi_mean = np.mean(list(itertools.chain(*wb.peakSi)))
    wb.peakTi_mean = np.mean(list(itertools.chain(*wb.peakTi)))
    wb.peakTri_mean = np.mean(list(itertools.chain(*wb.peakTri)))

def plot_initial_line(init, ax3):
    for ax in ax3:
        ax.plot(ax.get_xlim(), [init, init], '--', color='darkmagenta',
                label='average initial')


def plot_final_line(final, ax3):
    for ax in ax3:
        ax.plot(ax.get_xlim(), [final, final], '-', color='k', alpha=0.5,
                label='average final')

plot_initial_line(totalH_initial, axes[-1])
plot_final_line(totalH_final, axes[-1])
plot_initial_line(wbs[0].peakSi_mean, axes[0])
plot_final_line(wbs[1].peakSi_mean, axes[0])
plot_initial_line(wbs[0].peakTi_mean, axes[1])
plot_final_line(wbs[1].peakTi_mean, axes[1])
plot_initial_line(wbs[0].peakTri_mean, axes[2])
plot_final_line(wbs[1].peakTri_mean, axes[2])
    
print()
print('[Si] peak')
print('initial:', kiki.wb_Kiki_init.peakSi_mean)
print('final:', kiki.wb_Kiki_8hr.peakSi_mean)
print('change:', kiki.wb_Kiki_8hr.peakSi_mean - kiki.wb_Kiki_init.peakSi_mean)
print()
print('[Tri] peak')
print('initial:', kiki.wb_Kiki_init.peakTri_mean)
print('final:', kiki.wb_Kiki_8hr.peakTri_mean)
print('change:', kiki.wb_Kiki_8hr.peakTri_mean - kiki.wb_Kiki_init.peakTri_mean)
print()
print('[Ti] peak')
print('initial:', kiki.wb_Kiki_init.peakTi_mean)
print('final:', kiki.wb_Kiki_8hr.peakTi_mean)
print('change:', kiki.wb_Kiki_8hr.peakTi_mean - kiki.wb_Kiki_init.peakTi_mean)
print()
print('total H')
print('initial:', totalH_initial)
print('final:', totalH_final)
print('change:', totalH_final - totalH_initial)
 
# set axes limits and labels
ytops = [60, 0.25, 0.6, 0.25]
letters = iter(string.ascii_uppercase)
for ytop, idx in zip(ytops, [3, 2, 1, 0]):
    for ax in axes[idx]:
        ax.set_ylim(0, ytop)
        letter = next(letters)
        x = ax.get_xlim()[0] - 0.15*ax.get_xlim()[0]
        ax.text(x, ytop-0.15*ytop, letter)

for idx in range(3):
    axes[idx][1].set_title('')

axes[-1][0].text(0, 80, '800$\degree$C', fontsize=20, ha='center')
axes[-1][2].legend(loc=1, ncol=2, bbox_to_anchor=(0.8, 1.6))

for ax in axes[0]:
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

fig.autofmt_xdate()
fig.savefig(file, dpi=300, format='tif')