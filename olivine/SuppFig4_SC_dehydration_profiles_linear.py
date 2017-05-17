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
import itertools
import numpy as np
from olivine import high_ending

water = 14.
peaks = SC.peaks
wb2 = SC.wb_800C_hyd
wb_list = [SC.wb_800C_hyd, SC.wb_800C_1hr, SC.wb_800C_3hr,
           SC.wb_800C_7hr, SC.wb_800C_13hr, SC.wb_800C_19hr, SC.wb_800C_43hr,
           SC.wb_800C_68hr]

for wb in wb_list:
    wb.get_baselines(baseline_ending=high_ending)
    wb.make_areas()
    wb.make_peakheights(peaks=peaks)
    wb.areas = [prof.areas for prof in wb.profiles]
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]

#%% the figure
# rainbow
styles = [wb.style for wb in wb_list]
for style in styles:
    style['color'] = '#2ca02c'
    style['markeredgecolor'] = '#2ca02c'

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

# whole block or raw data?
wbdata = True

# initials
initials = [0]*3
initials[2] = 14.
for idx in range(2):
    x, y = wb2.xy_picker(peak_idx=idx, wholeblock=False, 
                         heights_instead=True)
    initials[idx] = np.mean(list(itertools.chain(*y)))

    for ax3, init in zip(axes, initials):
        for ax in ax3:
            if wbdata is False:
                ax.plot(ax.get_xlim(), [init, init], ':', 
                        color=styles[0]['color'])
            else:
                ax.plot(ax.get_xlim(), [1., 1.], ':', 
                        color=styles[0]['color'])
        
## axes limits
if wbdata is False:
    ytops = [0.12, 0.2, 20]
elif wbdata is True:
    ytops = [1.4]*3
else:
    pass
ybots = [0.0, 0, 0]
for top, bot, ax3 in zip(ytops, ybots, axes):    
    for ax in ax3:
        ax.set_ylim(bot, top)

idx = 2
for wb, style in zip(wb_list, styles):
    wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                       centered=True, show_errorbars=False, 
                       wholeblock=wbdata, scale=1)

for idx in range(2):
    for wb, style in zip(wb_list, styles):
        wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                               centered=True, show_errorbars=False, 
                               peak_idx=idx, heights_instead=True,
                               scale=1., wholeblock=wbdata)
    axes[idx][1].set_title('')

for ax, direction, raypath in zip(axes[-1], wb2.directions, wb2.raypaths):
    ax.set_title(''.join(('|| ', direction, ', R || ', raypath)))


axes[0][2].legend(ncol=4, title='SC1-2 dehydration time', 
   bbox_to_anchor=(0.7, 0.32), fontsize=8)

#fig.suptitle('Non-normalized data, linear baselines')
fig.savefig(SC.thisfolder+'\..\SuppFig4_SC_dehydration_profiles_linear.jpg', 
            dpi=400, format='jpg')
