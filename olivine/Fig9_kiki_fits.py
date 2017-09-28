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

file = os.path.join(olivine.__path__[0], 'Fig9_kiki_fits.jpg')

dfile = os.path.join(pynams.__path__[0], 'diffusion', 'literaturevalues.csv')
diffusivities = pd.read_csv(dfile)
Kdiffusivities = diffusivities[diffusivities.name == 'kiki']

times = [8, 3, 6, 7]

wbs = [kiki.wb_Kiki_8hr,
       kiki.wb_Kiki_1000C_3hr,
       kiki.wb_Kiki_1000C_6hr,
       kiki.wb_Kiki_1000C_8hr]

for prof in kiki.wb_Kiki_8hr.profiles:
    prof.initial_profile = prof

mechs = ['bulk', '[tri]', '[Ti]', '[Si]']

for wb, time in zip(wbs, times):
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=kiki.peaks)
    wb.diffs = []
    Ddata = Kdiffusivities[Kdiffusivities.hours == time]
    for mech in mechs:
        Ddatamech = Ddata[Ddata.mechanism == mech]
        wb.diffs.append(list(Ddatamech.log10D))

conversion_factor_area2water = 0.6 # see Table1_concentrations.py
profidx = itertools.cycle([0, 1, 2])
for wb in wbs:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
        wb.areas[next(profidx)] = prof.areas

wb2 = kiki.wb_Kiki_8hr
initial = np.mean(list(itertools.chain(*wb2.areas)))

pp = dlib.pv.whatIsD(celsius=800., printout=False)

#%% the figure

# set styles
style2 = wb2.style
style2['markeredgecolor'] = 'darkmagenta'
style2['markersize'] = 4
styles = [style2.copy(), style2.copy(), style2.copy(), style2.copy()]
styles[0]['marker'] = 'o'
styles[1]['marker'] = 's'
styles[2]['marker'] = '^'
styles[3]['marker'] = 'x'
styles[0]['markerfacecolor'] = 'darkmagenta'
styles[1]['markerfacecolor'] = 'none'
styles[3]['label'] = '8hr'
styles[2]['label'] = '6hr'
styles[1]['label'] = '3hr'
styles[0]['label'] = 'after reorganization'
     
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

        
# pp curves
pp = dlib.pp.whatIsD(1000, printout=False)
pv = dlib.pv.whatIsD(1000, printout=False)
styleD1 = {'color':'k', 'linestyle':'-', 'label':'pp 1hr'}
styleD2 = {'color':'k', 'linestyle':':', 'label':'pv 8hr'}
for ax3 in axes:
        wb.plot_diffusion(axes3=ax3,
                          time_seconds = 1*3600,
                          log10D_m2s=pp,
                          wholeblock_diffusion=True,
                          labelD=False, 
                          style_diffusion=styleD1)
        wb.plot_diffusion(axes3=ax3,
                          time_seconds = 8*3600,
                          log10D_m2s=pv,
                          wholeblock_diffusion=True,
                          labelD=False, 
                          style_diffusion=styleD2)
       

# initial lines
for ax3 in axes:
    for ax in ax3:
        ax.plot(ax.get_xlim(), [1., 1.], '--', color='darkmagenta', 
                alpha=0.6, label='initial')
        
# bulk water data
idx = -1
for wb, style in zip(wbs, styles):
    wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                          centered=True, show_errorbars=False,
                          wholeblock=True)
for idx, ax in enumerate(axes[idx]):
    ax.set_title(''.join(('|| ', wb2.directions[idx],
                          ', R || ', wb2.raypaths[idx])))

# peak height data
for idx in [0, 1, 2]:
    for wb, style in zip(wbs, styles):
        wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                              centered=True, show_errorbars=False,
                              wholeblock=True, heights_instead=True,
                              peak_idx=idx)

# set axes limits and labels
ytop = 1.3
letters = iter(string.ascii_uppercase)
for idx in [3, 2, 1, 0]:
    for ax in axes[idx]:
        ax.set_ylim(0, ytop)
        letter = next(letters)
        x = ax.get_xlim()[0] - 0.15*ax.get_xlim()[0]
        ax.text(x, ytop-0.15*ytop, letter)

for idx in range(3):
    axes[idx][1].set_title('')

#axes[-1][2].plot([0, 0], [-10, -10], **styleD2)
#axes[-1][2].plot([0, 0], [-10, -10], **styleD1)
axes[-1][2].legend(loc=1, ncol=4, bbox_to_anchor=(0.87, 1.6))

for ax in axes[0]:
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

fig.autofmt_xdate()
fig.savefig(file, dpi=300, format='jpg')