# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure(s) showing additional hydration profiles in San Carlos olivine
SC1-7 and SC1-2
"""
from __future__ import print_function
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine import thisfolder, high_ending, low_ending
import matplotlib.pyplot as plt
import numpy as np

# the data details are stored in SanCarlos_spectra.py
wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd

style2 = {'color':'#2ca02c', 'marker':'o', 'linestyle': 'none', 'markersize':4}
style7 = {'color':'#ff7f0e', 'marker':'s', 'linestyle': 'none', 'markersize':4}

#%% regular quadratic baselines
wb7.get_baselines(baseline_ending=high_ending)
wb2.get_baselines(baseline_ending=high_ending)
wb7.make_areas()
wb2.make_areas()

fig = plt.figure()
fig.set_size_inches(6.5, 10)

peaks = [3600, 3573, 3525, 3484, 3396, 3356, 3236]

# make the axes
xstart = 0.08
ypstart = 0.07
wgap = 0.01
width = 0.26
height = 0.1
hgap = 0.02
axes = []
for idx in range(len(peaks)+1):
    ax1 = fig.add_axes([xstart, ypstart, width, height])
    ax2 = fig.add_axes([xstart+width+wgap, ypstart, width, height])
    ax3 = fig.add_axes([xstart+2*width+2*wgap, ypstart, width, height])
    axes.append([ax1, ax2, ax3])
    ypstart = ypstart + 0.01 + height

wb7.plot_areas_3panels(axes3=axes[-1], styles3=[style7]*3, centered=True)
wb2.plot_areas_3panels(axes3=axes[-1], styles3=[style2]*3, centered=True)

axes[0][0].set_xlabel('x (mm)')
axes[0][1].set_xlabel('y (mm)')
axes[0][2].set_xlabel('z (mm)')
axes[3][0].set_ylabel('Peak height, cm$^{-1}$')
for idx, ax3 in enumerate(axes):
    for ax in ax3:
        if idx != 0:
            ax.axes.get_xaxis().set_ticks([])
        ax.set_ylim(0, 0.25)
    ax3[1].axes.get_yaxis().set_ticks([])
    ax3[2].axes.get_yaxis().set_ticks([])
    ax3[0].set_xlim(-1300, 1300)
    ax3[1].set_xlim(-950, 950)
    ax3[2].set_xlim(-1300, 1300)

        
# plot peak heights
for idx, peak in enumerate(peaks): 
    currentaxes = axes[idx]
    for axidx in range(3):
        # SC1-7
        prof = wb7.profiles[axidx]
        heights = []
        for spec in prof.spectra:
            idx = np.abs(peak - spec.base_wn).argmin()
            heights.append(spec.abs_nobase_cm[idx])
        x = prof.positions_microns - prof.length_microns/2.
        line = currentaxes[axidx].plot(x, heights, 's', label=str(peak), 
                          markersize=4, color=style7['color'])

        # SC1-2
        prof = wb2.profiles[axidx]
        heights2 = []
        for spec in prof.spectra:
            idx = np.abs(peak - spec.base_wn).argmin()
            heights2.append(spec.abs_nobase_cm[idx])
        x = prof.positions_microns - prof.length_microns/2.
        line = currentaxes[axidx].plot(x, heights2, 'o', label=str(peak), 
                          markersize=4, color=style2['color'])

# change y-axis limits
ytops = iter([0.3, 1.3, 0.7, 0.4, 0.9, 0.3, 0.2, 120])
for ax3 in axes:
    ytop = next(ytops)
    for ax in ax3:
        ax.set_ylim(0, ytop)
    
# label the peaks on the right side
for idx, peak in enumerate(peaks):
    ax = axes[idx][2]
    peaklabel = ''.join((str(peak), ' cm$^{-1}$'))
    ax.text(1400, ax.get_ylim()[1]/2., peaklabel, ha='left', va='center')
axes[-1][1].set_title('Linear baselines')
axes[-1][0].set_ylabel('Hydrogen, ppm H$_2$O')
axes[-1][2].text(1400, axes[-1][2].get_ylim()[1]/2., 'bulk H', 
    ha='left', va='center')
axes[-1][0].text(-1200, 70, 'SC1-7', color=style7['color'])
axes[-1][0].text(-1200, 5, 'SC1-2', color=style2['color'])

fig.savefig(thisfolder+'SuppFig2_AdditionalHydrationProfiles.jpg',
            dpi=200, format='jpg')
