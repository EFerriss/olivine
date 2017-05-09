# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Dehydration profiles for San Carlos olivine SC1-2 after 3 hours

Data details and peak heights are in SanCarlos_spectra.py. Baselines
were created in SanCarlos_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
import matplotlib.pyplot as plt
import itertools
import numpy as np
   
peaks = SC.peaks

#%%
# blocks of data to be plotted
wb2 = SC.wb_800C_hyd
wb1 = SC.wb_800C_3hr

# WHY DOES THE ORDER MATTER SO MUCH FOR wb2?
wb_list = [wb1, wb2]

# set up areas and convert them to water concentrations
conversion_factor_area2water = 0.6 # see Table1_concentrations.py
for wb in wb_list:
    wb.get_baselines()
    wb.make_areas()
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
    wb.areas = [prof.areas for prof in wb.profiles]
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]

#%%

#% the figure
style2 = {'color':'#2ca02c', 'marker':'o', 'linestyle': 'none', 'markersize':4,
          'alpha':0.3}
styledata = {'color':'k', 'marker':'+', 'linestyle':'none', 'markersize':6,
             'markeredgewidth':1.5}
style7 = {'color':'#ff7f0e', 'marker':'s', 'linestyle': 'none', 'markersize':4}
styleD = {'color': 'grey', 'linestyle':'-', 'linewidth':3}

fig = plt.figure()
fig.set_size_inches(6.5, 4)
xstart = 0.125
ypstart = 0.1
wgap = 0.005
width = 0.26
height = 0.24
hgap = 0.03
axes = []

# create axes
for peak in range(3):
    ax1 = fig.add_axes([xstart, ypstart, width, height])
    ax2 = fig.add_axes([xstart+width+wgap, ypstart, width, height])
    ax3 = fig.add_axes([xstart+2*width+2*wgap, ypstart, width, height])
    ax1.set_xlim(-1300, 1300)
    ax2.set_xlim(-950, 950)
    ax3.set_xlim(-1300, 1300)
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
axes[-1][0].set_ylabel('bulk hydrogen\n(ppm H$_2$O)')
axes[0][0].set_ylabel('[Si-Fe$^{2+}$] peak\nheight (cm$^{-1}$)')
axes[1][0].set_ylabel('[Ti-3525] peak\nheight (cm$^{-1}$)')

# axes limits
ytops = iter([0.15, 0.25, 20])
for idx in range(len(axes)):
    ytop = next(ytops)
    for ax in axes[idx]:
        ax.set_ylim(0, ytop)

# plot bulk H
idx = 2
wb2.plot_areas_3panels(axes3=axes[idx], styles3=[style2]*3, 
                       centered=True, show_errorbars=False)
wb1.plot_areas_3panels(axes3=axes[idx], styles3=[styledata]*3,
                       centered=True, show_errorbars=False)

# peak heights
for idx in range(2):
    wb2.plot_areas_3panels(axes3=axes[idx], styles3=[style2]*3, 
                           centered=True, show_errorbars=False, 
                           peak_idx=idx, heights_instead=True)
    wb1.plot_areas_3panels(axes3=axes[idx], styles3=[styledata]*3, 
                           centered=True, show_errorbars=False, 
                           peak_idx=idx, heights_instead=True)    
    axes[idx][1].set_title('')

for ax, direction, raypath in zip(axes[-1], wb2.directions, wb2.raypaths):
    ax.set_title(''.join(('Profile || ', direction, ' and R || ', raypath)))

fig.suptitle('SC1-2 dehydrated 3 hours')

# initial = mean of the initial across all profiles
initials = [0]*3
initials[2] = np.mean(list(itertools.chain(*wb2.areas)))
for idx in range(2):
    x, y = wb2.xy_picker(peak_idx=idx, wholeblock=False, heights_instead=True)
    initials[idx] = np.mean(list(itertools.chain(*y)))
for ax3, init in zip(axes, initials):
    for ax in ax3:
        ax.plot(ax.get_xlim(), [init, init], ':', color=style2['color'])

fig.savefig(SC.thisfolder+'\..\SuppFig5_SC_dehyd_3hr.jpg', 
            dpi=300, format='jpg')        
