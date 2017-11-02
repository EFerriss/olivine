# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing dehydration profiles in Kilauea Iki olivine for bulk 
hydrogen and 3 major peaks.

Data details and peak heights are in Kiki_spectra.py. Baselines
were created in Kiki_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.KilaueaIki import Kiki_spectra as kiki
import itertools
from pynams import dlib
import numpy as np
import matplotlib.pyplot as plt
import os
import olivine
import pandas as pd
import pynams
import string

file = os.path.join(olivine.__path__[0], 'Fig8_kiki_reorganization_800.jpg')

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
mechs = ['bulk', '[tri]', '[Ti]', '[Si]']

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
     
# make the axes
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
axes[3][0].set_ylabel('bulk\nhydrogen / initial')
axes[0][0].set_ylabel('[Si-Fe$^{2+}$]\npeak height / initial')
axes[1][0].set_ylabel('[Ti-3525]\npeak height / initial')
axes[2][0].set_ylabel('[tri-Fe$^{3+}$]\npeak height / initial')

# bulk water data
idx = -1
for wb, style in zip(wbs, styles):
    wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                          centered=True, show_errorbars=False,
                          wholeblock=True)
for idx, ax in enumerate(axes[idx]):
    ax.set_title(''.join(('|| ', wbdata.directions[idx],
                          ', R || ', wbdata.raypaths[idx])))

# peak height data
for idx in [0, 1, 2]:
    for wb, style in zip(wbs, styles):
        wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                              centered=True, show_errorbars=False,
                              wholeblock=True, heights_instead=True,
                              peak_idx=idx)   
        
# initial lines
for ax3 in axes:
    for ax in ax3:
        ax.plot(ax.get_xlim(), [1., 1.], '--', color='darkmagenta', 
                alpha=0.6)
        
       
# diffusion
#pv = dlib.pv.whatIsD(800, printout=False)
#styleD1 = {'color':'darkmagenta', 'linestyle':'-', 'label':'6hr fit'}
#styleD2 = {'color':'k', 'linestyle':':', 'label':'6hr PV'}
#mechs.reverse()
#ytxts = [0.5, 0.1, 0.1, 0.1]
#for mech, ax3, ytxt in zip(mechs, axes, ytxts):
#    # PV
#    wbdata.plot_diffusion(axes3=ax3,
#                      log10D_m2s=pv,
#                      wholeblock_diffusion=True,
#                      labelD=False, 
#                      style_diffusion=styleD2)
    
##     best fit at 1000C
#    Ddata = Kdiffusivities[Kdiffusivities.mechanism == mech]
#    D3 = list(Ddata.log10D)
#    wbdata.plot_diffusion(axes3=ax3,
#                          log10D_m2s=D3,
#                          wholeblock_diffusion=True,
#                          labelD=False, 
#                          style_diffusion=styleD1)
#    
#    for D, ax in zip(D3, ax3): 
#        tstring = ''.join(('10$^{', '{:.1f}'.format(D), '}$ m$^2$/s'))
#        ax.text(0, ytxt, tstring, color='darkmagenta', va='center', ha='center')
    
# set axes limits and labels
ytops = [1.5, 1.5, 1.5, 3]
letters = iter(string.ascii_uppercase)
for ytop, idx in zip(ytops, [3, 2, 1, 0]):
    for ax in axes[idx]:
        ax.set_ylim(0, ytop)
        letter = next(letters)
        x = ax.get_xlim()[0] - 0.15*ax.get_xlim()[0]
        ax.text(x, ytop-0.15*ytop, letter)

for idx in range(3):
    axes[idx][1].set_title('')

axes[-1][0].text(0, 2.1, '800$\degree$C', fontsize=20, ha='center')

axes[-1][2].legend(loc=1, ncol=3, bbox_to_anchor=(0.8, 1.6))

for ax in axes[0]:
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

fig.autofmt_xdate()
fig.savefig(file, dpi=300, format='jpg')