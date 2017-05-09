# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Dehydration profiles for San Carlos olivine SC1-2

Data details and peak heights are in SanCarlos_spectra.py. Baselines
were created in SanCarlos_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
import matplotlib.pyplot as plt
from pynams import dlib
import itertools
import numpy as np
   
peaks = SC.peaks
fastdiffusion = dlib.KM98_fast.whatIsD(800, printout=False)[0:3]

wb2 = SC.wb_800C_hyd
wb_list = [SC.wb_800C_hyd, SC.wb_800C_1hr, SC.wb_800C_3hr,
           SC.wb_800C_7hr, SC.wb_800C_13hr, SC.wb_800C_19hr, SC.wb_800C_43hr,
           SC.wb_800C_68hr]

# set up areas and convert them to water concentrations
conversion_factor_area2water = 0.6 # see Table1_concentrations.py
for wb in wb_list:
    wb.get_baselines()
    wb.make_areas()
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
    wb.areas = [prof.areas for prof in wb.profiles]
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]

# not sure why I need to do this twice. There must be a bug somewhere.
wb = wb_list[0]
for prof in wb.profiles:
    prof.areas = list(prof.areas * conversion_factor_area2water)

#%%
#% the figure
style2 = {'color':'grey', 'marker':'o', 'linestyle': 'none', 'markersize':8,
          'label': 'hydrated', 'alpha':0.5,}
style1 = {'color':'r', 'marker':'+', 'linestyle':'none', 'markersize':9,
          'markeredgewidth':1.5, 'label':'1 hour'}
style3 = {'markeredgecolor':'chocolate', 'marker':'^', 'linestyle':'none', 
           'markersize':7, 'markeredgewidth':1.5, 'label':'3 hours',
           'alpha':0.5, 'markerfacecolor':'none'}
style7 = {'color':'goldenrod', 'marker':'x', 'linestyle':'none', 
           'markersize':6, 'markeredgewidth':1.5, 'label':'7 hours'}
style13 = {'color':'g', 'marker':'p', 'linestyle':'none', 'markersize':6,
          'markeredgewidth':1.5, 'label':'13 hours', 'alpha':0.4}
style19 = {'markeredgecolor':'b', 'marker':'s', 'linestyle':'none', 
           'markersize':4, 'markerfacecolor':'none',
          'markeredgewidth':1, 'label':'19 hours', 'alpha':0.5}
style43 = {'color':'indigo', 'marker':'x', 'linestyle':'none', 'markersize':4,
          'markeredgewidth':1, 'label':'43 hours'}
style68 = {'color':'violet', 'marker':'.', 'linestyle':'none', 'markersize':5,
             'markeredgewidth':1, 'label':'68 hours'}

styles = [style2, style1, style3, style7, style13, style19, style43, style68]

fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.125
ypstart = 0.09
wgap = 0.005
width = 0.26
height = 0.26
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
ytops = [0.14, 0.25, 20]
ybots = [0.0, 0, 0]
for top, bot, ax3 in zip(ytops, ybots, axes):    
    for ax in ax3:
        ax.set_ylim(bot, top)

# plot bulk H
idx = 2
for wb, style in zip(wb_list, styles):
    wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                       centered=True, show_errorbars=False)

for idx in range(2):
    for wb, style in zip(wb_list, styles):
        wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                               centered=True, show_errorbars=False, 
                               peak_idx=idx, heights_instead=True)
    axes[idx][1].set_title('')

for ax, direction, raypath in zip(axes[-1], wb2.directions, wb2.raypaths):
    ax.set_title(''.join(('|| ', direction, ', R || ', raypath)))


# initial = mean of the initial across all profiles
initials = [0]*3
initials[2] = np.mean(list(itertools.chain(*wb2.areas)))
for idx in range(2):
    x, y = wb2.xy_picker(peak_idx=idx, wholeblock=False, heights_instead=True)
    initials[idx] = np.mean(list(itertools.chain(*y)))
for ax3, init in zip(axes, initials):
    for ax in ax3:
        ax.plot(ax.get_xlim(), [init, init], ':', color=style2['color'])

axes[0][2].legend(loc='bottom right', ncol=4, title='SC1-2 dehydration time', 
   bbox_to_anchor=(0.7, 0.35))

fig.suptitle('Quadratic baselines')
fig.savefig(SC.thisfolder+'\..\Fig6_SC_dehydration_profiles.jpg', 
            dpi=400, format='jpg')        


