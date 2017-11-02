 # -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing hydration profiles in San Carlos olivines for bulk 
hydrogen and 4 major peaks.

All related profiles are going into the supplement.

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
import string 

# output file
file = os.path.join(olivine.__path__[0], 'Fig4_hydration_profiles.jpg')

# set up peaks and areas
peaks = SC.peaks
conversion_factor_area2water = 0.6 # see Table1_concentrations.py
wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
wb2.get_baselines()
wb7.get_baselines()
wb2.make_areas()
wb7.make_areas()
wb2.make_peakheights(peaks=peaks)
wb7.make_peakheights(peaks=peaks)

# convert areas to water concentrations
profidx = itertools.cycle([0, 1, 2])
for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
        wb.areas[next(profidx)] = prof.areas

#%% Assumptions for drawing diffusion curves
solubility = 58.
metastable = np.mean(list(itertools.chain(*wb2.areas)))
maxarea = max([max(areas) for areas in wb7.areas])
scale_final = solubility / maxarea # to scale up to true solubility

ytops = iter([60., 0.3, 0.7, 0.7, 0.3])
wb7.pv = 100.
wb7.peak_pv = [100.]*4


wb7.peak_D3 = [[]]*4
wb7.D3 = dlib.mix_olivine_mechanisms(celsius=1000, percent_slow=wb7.pv)
for idx, pv in enumerate(wb7.peak_pv):
    wb7.peak_D3[idx] = dlib.mix_olivine_mechanisms(celsius=1000, 
                                                   percent_slow=pv)

wb7.D3[1] = wb7.D3[1] + 1.
wb7.D3[2] = wb7.D3[2] + 0.6

wb7.peak_D3[2][1] = wb7.peak_D3[2][1] + 1.
wb7.peak_D3[3][1] = wb7.peak_D3[3][1] + 1.5

wb7.peak_D3[0][2] = wb7.peak_D3[0][2] + 0.7
wb7.peak_D3[1][2] = wb7.peak_D3[1][2] + 0.7
wb7.peak_D3[2][2] = wb7.peak_D3[2][2] + 0.6
wb7.peak_D3[3][2] = wb7.peak_D3[3][2] + 0.6

#% the figure
style2 = wb2.style
style7 = wb7.style
style7['label'] = 'SC1-7'
style2['label'] = 'SC1-2 (pp done)'
     
# make the axes
fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.13
ypstart = 0.09
wgap = 0.005
width = 0.27
height = 0.15
hgap = 0.03
ytxt_shifts = [0.2, 0.2, 0.2, 0.7, 0.2]
axes = []
for peak in range(len(peaks)+1):
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
axes[4][0].set_ylabel('bulk hydrogen\n(ppm H$_2$O)')
axes[0][0].set_ylabel('[Si-Fe$^{2+}$] peak\nheight (cm$^{-1}$)')
axes[1][0].set_ylabel('[Ti-3525] peak\nheight (cm$^{-1}$)')
axes[2][0].set_ylabel('[tri-Fe$^{3+}$] peak\nheight (cm$^{-1}$)')
axes[3][0].set_ylabel('[Mg] peak\nheight (cm$^{-1}$)')

# plot bulk water data
idx = -1
wb2.plot_areas_3panels(axes3=axes[idx], styles3=[style2]*3, 
                       centered=True, show_errorbars=False)
wb7.plot_areas_3panels(axes3=axes[idx], styles3=[style7]*3, 
                       centered=True, show_errorbars=False)
for idx, ax in enumerate(axes[idx]):
    ax.set_title(''.join(('|| ', wb2.directions[idx],
                          ', R || ', wb2.raypaths[idx])))

# peak heights
for pidx, peak in enumerate(peaks): 
    currentaxes = axes[pidx]
    for axidx in range(3):
        # SC1-7
        prof = wb7.profiles[axidx]
        x = prof.positions_microns - prof.length_microns/2.
        y = prof.peak_heights[pidx]
        line = currentaxes[axidx].plot(x, y, **style7)
        
        # SC1-2
        prof = wb2.profiles[axidx]
        x = prof.positions_microns - prof.length_microns/2.
        line = currentaxes[axidx].plot(x, prof.peak_heights[pidx], **style2)

# set axes limits and labels
for ax in axes:
    ax[0].set_xlim(-1400, 1400)    
    ax[1].set_xlim(-550, 550)
    ax[2].set_xlim(-1500, 1500)
        
# bulk H diffusion
for ax in axes[-1]:
    ax.plot(ax.get_xlim(), [metastable, metastable], ':', 
            color=style2['color'])
    ax.set_ylim(0, 60)
D4plot = [Dset for Dset in wb7.D3]
D3pv = dlib.pv.whatIsD(celsius=1000., printout=False)
wb7.plot_diffusion(axes3=axes[-1], # black lines, pv 
                   log10D_m2s=D3pv, 
                   init=metastable, 
                   fin=solubility, show_line_at_1=False,
                   wholeblock_diffusion=True, show_data=False,
                   labelD=False, labelDy=90, points=200,
                   style_diffusion={'color':'k','linewidth':2})
wb7.plot_diffusion(axes3=axes[-1], # orange lines, best fit
                   log10D_m2s=D4plot, 
                   init=metastable, 
                   fin=solubility, show_line_at_1=False,
                   wholeblock_diffusion=True, show_data=False,
                   labelD=False, labelDy=90, points=200,
                   style_diffusion={'color':style7['color'],'linewidth':1})

for D, Dpv, ax in zip(wb7.D3, D3pv, axes[-1]): 
    tstring = ''.join(('10$^{', '{:.1f}'.format(D), '}$ m$^2$/s'))
    ytxt = ax.get_ylim()[1] - ytxt_shifts[-1]*ax.get_ylim()[1]
    ax.text(0, ytxt, tstring, color=style7['color'], va='center', ha='center')

    tstring = ''.join(('10$^{', '{:.1f}'.format(Dpv), '}$ m$^2$/s'))
    ytxt = ax.get_ylim()[1] - ytxt_shifts[-1]*ax.get_ylim()[1]
    ax.text(0, 5, tstring, color='k', va='center', ha='center')


# peak-specific diffusion
for idx in range(4):
    peak_heights7 = [profile.peak_heights[idx] for profile in wb7.profiles]
    peak_heights2 = [profile.peak_heights[idx] for profile in wb2.profiles]
    maxy = max([max(heights) for heights in peak_heights7])
    meta = np.mean(list(itertools.chain(*peak_heights2)))
    for ax in axes[idx]:
        ax.plot(ax.get_xlim(), [meta, meta], ':', color=style2['color'])
        ax.set_ylim(0, maxy*scale_final)

    D4plot = [Dset for Dset in wb7.peak_D3[idx]]
    wb7.plot_diffusion(axes3=axes[idx], log10D_m2s=D4plot,
                       init=meta, fin=maxy*scale_final,
                       show_line_at_1=False, wholeblock_diffusion=True, 
                       show_data=False, labelD=False, points=200,
                       style_diffusion={'color':style7['color'],'linewidth':1})
    for D, ax in zip(D4plot, axes[idx]): 
        tstring = ''.join(('10$^{', '{:.1f}'.format(D), '}$ m$^2$/s'))
        ytxt = ax.get_ylim()[1] - ytxt_shifts[idx]*ax.get_ylim()[1]
        ax.text(0, ytxt, tstring, color=style7['color'], 
                va='center', ha='center')

axes[0][2].plot([0, 0], [-100, -100], '-', color=style7['color'],
    label='SC1-7 best fit')
axes[0][2].plot([0, 0], [-100, -100], '-', color='k',
    label='PV')
axes[0][2].legend(loc=1, ncol=4, bbox_to_anchor=(1., 0.35))

letters = iter(string.ascii_uppercase)
for idx in [4, 3, 2, 1, 0]:
    for ax in axes[idx]:
        letter = next(letters)
        x = ax.get_xlim()[0] - 0.1*ax.get_xlim()[0]
        y = ax.get_ylim()[1] - 0.15*ax.get_ylim()[1]
        ax.text(x, y, letter)

fig.savefig(file, dpi=200, format='jpg')
