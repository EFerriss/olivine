# -*- coding: utf-8 -*-
"""
@author: Elizabeth Ferriss

Figure showing dehydration profiles in San Carlos olivine SC1-2
for [Ti] peak at 3525 cm-1 changing diffusivity relative to pp mechanism
between 7 and 19 hours and comparison with Kilauea Iki behavior.
 
Data details and peak heights are in SanCarlos_spectra.py. Baselines
were created in SanCarlos_baselines.py and are stored in the same
folder as the original FTIR data.

"""
from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
import itertools
from pynams import dlib, styles
import numpy as np
import matplotlib.pyplot as plt
import os
import olivine

# output file
file = os.path.join(olivine.__path__[0], 'Fig7_Tipeak.jpg')

# set up peaks and areas
wbk = kiki.wb_Kiki_8hr
wb7 = SC.wb_800C_7hr
wb13 = SC.wb_800C_19hr

for wb in [wbk, wb7, wb13]:
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=[3525])
    for prof in wb.initial_profiles:
        prof.get_baselines()
        prof.make_areas()
        prof.make_peakheights(peaks=[3525])

style = styles.style_points.copy()
style['color'] = '#2ca02c'
styleK = style.copy()
styleK['color'] = 'darkmagenta'

#%% the figure
# make the axes
fig = plt.figure()
fig.set_size_inches(6.5, 5)
xstart = 0.13
ypstart = 0.13
wgap = 0.02
width = 0.25
height = 0.25
hgap = 0.05
ytxt_shifts = [0.2, 0.2, 0.2, 0.7, 0.2]

axes = []
for peak in range(3):
    ax1 = fig.add_axes([xstart, ypstart, width, height])
    ax2 = fig.add_axes([xstart+width+wgap, ypstart, width, height])
    ax3 = fig.add_axes([xstart+2*width+2*wgap, ypstart, width, height])
    axes.append([ax1, ax2, ax3])
    ypstart = ypstart + hgap + height

for idx, ax3 in enumerate(axes):
    for ax in ax3:
        ax.set_ylim(0, 1.2)
        if idx != 0:
            ax.axes.get_xaxis().set_ticks([])
    ax3[1].axes.get_yaxis().set_ticks([])
    ax3[2].axes.get_yaxis().set_ticks([])
axes[0][0].set_xlabel('x / length || [100]')
axes[0][1].set_xlabel('y / length || [010]')
axes[0][2].set_xlabel('z / length || [001]')
axes[2][0].set_ylabel('[Ti] H/H$_0$\nKilauea at 8 hours')
axes[1][0].set_ylabel('[Ti] H/H$_0$\nSC1-2 at 7 hours')
axes[0][0].set_ylabel('[Ti] H/H$_0$\nSC1-2 at 19 hours')

D3 = dlib.pp.whatIsD(800., printout=False)[0:3]

wbk.plot_areas_3panels(axes3=axes[2], 
                       heights_instead=True,
                       wholeblock=True, 
                       show_errorbars=False, 
                       peak_idx = 0,
                       centered = False,
                       show_line_at_1=True, 
                       styles3=[styleK]*3)
wbk.plot_diffusion(axes3=axes[2], 
                   log10D_m2s=D3,
                   centered=False,
                   wholeblock_diffusion=True,
                   labelD=False)

wb7.plot_areas_3panels(axes3=axes[1], 
                       heights_instead=True,
                       wholeblock=True, 
                       centered = False,
                       show_errorbars=False, 
                       peak_idx = 0, 
                       show_line_at_1=True, 
                       styles3=[style]*3)
wb7.plot_diffusion(axes3=axes[1], 
                   log10D_m2s=D3,
                   centered=False,
                   wholeblock_diffusion=True,
                   labelD=False)

wb13.plot_areas_3panels(axes3=axes[0], heights_instead=True,
                       wholeblock=True, show_errorbars=False, 
                       centered = False,
                       peak_idx = 0, show_line_at_1=True, 
                       styles3=[style]*3)

wb13.plot_diffusion(axes3=axes[0], 
                   log10D_m2s=D3,
                   centered=False,
                   wholeblock_diffusion=True,
                   labelD=False)


for length, ax in zip(wb7.sample.lengths_microns, axes[0]):
    x = [0, length/2., length]
    ax.set_xticks(x)
    ax.set_xticklabels(['0', 0.5, '1'])
#    plt.xticks(x, )
    
axes[1][1].plot([-100000], [-100000], '-k', label='pp mechanism')
axes[1][1].legend(loc=8)

tit1 ='[Ti] peak heated at 800$\degree$C'
#tit0 ='[Ti] peak at 3525 cm$^{-1}$ after 19 hours heating at 800$\degree$C'
axes[2][1].set_title('')
axes[0][1].set_title('')
axes[1][1].set_title('')

fig.savefig(file, dpi=300, format='jpg')