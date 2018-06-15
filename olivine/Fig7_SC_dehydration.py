# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing dehydration profiles in San Carlos olivines for total 
hydrogen and 2 major peaks.

Data details and peak heights are in SanCarlos_spectra.py. Baselines
were created in SanCarlos_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
import itertools
from pynams import dlib
import numpy as np
import matplotlib.pyplot as plt
import os
import olivine
import pandas as pd
import pynams
import string

file = os.path.join(olivine.__path__[0], 'Fig7_SC_dehydration.tif')
dfile = os.path.join(olivine.__path__[0], 'mydata.csv')

diffusivities = pd.read_csv(dfile)
SCdiffusivities = diffusivities[diffusivities.name == 'SC1-2']

times = [17.4, 7, 19, 68]

wbs = [SC.wb_800C_hyd,
       SC.wb_800C_7hr,
       SC.wb_800C_19hr,
       SC.wb_800C_68hr]

mechs = ['total', '[Ti]', '[Si]']

for wb, time in zip(wbs, times):
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=SC.peaks)
    wb.diffs = []
    Ddata = SCdiffusivities[SCdiffusivities.hours == time]
    for mech in mechs:
        Ddatamech = Ddata[Ddata.mechanism == mech]
        wb.diffs.append(list(Ddatamech.log10D))

conversion_factor_area2water = 0.6 # see Table1_concentrations.py
profidx = itertools.cycle([0, 1, 2])
for wb in wbs:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
        wb.areas[next(profidx)] = prof.areas

wb2 = SC.wb_800C_hyd
initial = np.mean(list(itertools.chain(*wb2.areas)))

#%% the figure
ytops = iter([1.2, 1.2, 1.2])

# set styles
style2 = wb2.style
style2['markersize'] = 4
styles = [style2.copy(), style2.copy(), style2.copy(), style2.copy()]
styles[1]['marker'] = 's'
styles[2]['marker'] = '^'
styles[3]['marker'] = 'x'
styles[1]['markerfacecolor'] = 'none'
styles[3]['label'] = '68hr'
styles[2]['label'] = '19hr'
styles[1]['label'] = '7hr'
styles[0]['label'] = 'metastable equilib.'
     
# make the axes
fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.13
ypstart = 0.07
wgap = 0.005
width = 0.27
height = 0.24
hgap = 0.04
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
axes[2][0].set_ylabel('total\nhydrogen / initial')
axes[0][0].set_ylabel('[Si-4H]\npeak height / initial')
axes[1][0].set_ylabel('[Ti-2H]\npeak height / initial')

# pp curves
pp = dlib.pp.whatIsD(800, printout=False)
styleD1 = {'color':'k', 'linestyle':'-', 'label':'redox 7hr'}
styleD2 = {'color':'k', 'linestyle':':', 'label':'redox 19hr'}
stylesD = [styleD1, styleD2]
for ax3 in axes:
    for wb, style in zip(wbs[1:3], stylesD):
        wb.plot_diffusion(axes3=ax3,
                          log10D_m2s=pp,
                          wholeblock_diffusion=True,
                          labelD=False, 
                          style_diffusion=style)
       
# initial lines
for ax3 in axes:
    for ax in ax3:
        ax.plot(ax.get_xlim(), [1., 1.], '--', color=style2['color'], 
                alpha=0.6, label='initial')
        
# total water data
idx = -1
for wb, style in zip(wbs, styles):
    wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                          centered=True, show_errorbars=False,
                          wholeblock=True)
for idx, ax in enumerate(axes[idx]):
    ax.set_title(''.join(('|| ', wb2.directions[idx],
                          ', R || ', wb2.raypaths[idx])))

# peak height data
for idx in [0, 1]:
    for wb, style in zip(wbs, styles):
        wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                              centered=True, show_errorbars=False,
                              wholeblock=True, heights_instead=True,
                              peak_idx=idx)

# set axes limits and labels
letters = iter(string.ascii_uppercase)
for idx in [2, 1, 0]:
    ytop = next(ytops)
    for ax in axes[idx]:
        ax.set_ylim(0, 1.2)
        letter = next(letters)
        x = ax.get_xlim()[0] - 0.1*ax.get_xlim()[0]
        ax.text(x, ytop-0.1*ytop, letter)


axes[1][1].set_title('')
axes[0][1].set_title('')

axes[0][2].plot([0, 0], [-10, -10], **styleD1)
axes[0][2].plot([0, 0], [-10, -10], **styleD2)

axes[2][2].legend(loc=1, ncol=4, bbox_to_anchor=(1., 1.5))

for D, ax in zip(pp, axes[-1]): 
    tstring = ''.join(('10$^{', '{:.1f}'.format(D), '}$ m$^2$/s'))
    ytxt = ax.get_ylim()[1] - ytxt_shifts[-1]*ax.get_ylim()[1]
    ax.text(0, 0.05, tstring, color='k', va='center', ha='center')

fig.savefig(file, dpi=300, format='tif')