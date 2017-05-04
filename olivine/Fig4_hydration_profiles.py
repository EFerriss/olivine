# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing hydration profiles in San Carlos olivines for bulk 
hydrogen, [Si-Fe2+] at 3600, and [Ti] at 3525 cm-1

All other profiles are going into the supplement.

Data details and peak heights are in SanCarlos_spectra.py. Baselines
were created in SanCarlos_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
reload(SC)
import itertools
from pynams import dlib
import numpy as np
import matplotlib.pyplot as plt
import pynams.experiments as exper
   
peaks = SC.peaks

# set up areas and convert them to water concentrations
conversion_factor_area2water = 0.6 # see Table1_concentrations.py
wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
wb2.get_baselines()
wb7.get_baselines()
wb2.make_areas()
wb7.make_areas()

profidx = itertools.cycle([0, 1, 2])
for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
        wb.areas[next(profidx)] = prof.areas

#%% CALCULATIONS FOR LEAST SQUARES DIFFUSIVITIES
# bulk H
D3 = dlib.KM98_slow.whatIsD(1000, printout=False) # pv mechanism diffusivities
true_solubility = exper.solubility_of_H_in_olivine(Celsius=1000, 
                                                   pressure_GPa=1, 
                                                   author='Mosenfelder',
                                                   printout=False)
metastable = np.mean(list(itertools.chain(*wb2.areas)))

wb7.D3, wb7.init, wb7.fin = wb7.fitD(peak_idx=None, init=metastable,
                                     fin=true_solubility, 
                                     wholeblock_data=False,
                                     log10Ds_m2s=D3, 
                                     vary_diffusivities=[False, False, True])

#%%
maxarea = max([max(areas) for areas in wb7.areas])
scale_final = true_solubility / maxarea # to scale up to true solubility

pidx = 0
peak_heights7 = [profile.peak_heights[pidx] for profile in wb7.profiles]
peak_heights2 = [profile.peak_heights[pidx] for profile in wb2.profiles]
maxy = max([max(heights) for heights in peak_heights7])
meta = np.mean(list(itertools.chain(*peak_heights2)))
#wb7.peak_D3 = [[]]*4
#trueC = exper.solubility_of_H_in_olivine(Celsius=1000, pressure_GPa=1, 
#                                 author='Mosenfelder')
#finfrac = trueC / maxarea
#for idx in range(4):
#    wb7.peak_D3[idx], init, fin = wb7.fitD(peak_idx=idx, 
#                                       heights_instead=True, 
#                                       wholeblock_data=False,
#                                       init=mean_metastable[idx], 
#                                       fin=max_peakheight[idx]*finfrac,
#                                       log10Ds_m2s=D3,
#                                       vary_diffusivities=[False, False, True])

##%%
#for idx in range(4):
#    print('peak at', wb7.profiles[0].peakpos[idx], 'cm-1')
#    print('{:.1f}'.format(wb7.peak_D3[idx][2]), 'log10 m2/s || c')
#    print()

#%% the figure
style2 = {'color':'#2ca02c', 'marker':'o', 'linestyle': 'none', 'markersize':4}
style7 = {'color':'#ff7f0e', 'marker':'s', 'linestyle': 'none', 'markersize':4}

fig = plt.figure()
fig.set_size_inches(6.5, 7)

xstart = 0.125
ypstart = 0.07
wgap = 0.01
width = 0.26
height = 0.16
hgap = 0.02
axes = []

for peak in range(len(peaks)+1):
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
axes[4][0].set_ylabel('bulk hydrogen\n(ppm H$_2$O)')
axes[0][0].set_ylabel('[Si-Fe$^{2+}$] peak\nheight (cm$^{-1}$)')
axes[1][0].set_ylabel('[Ti-3525] peak\nheight (cm$^{-1}$)')
axes[2][0].set_ylabel('[tri-Fe$^{3+}$] peak\nheight (cm$^{-1}$)')
axes[3][0].set_ylabel('[Mg] peak\nheight (cm$^{-1}$)')

## bulk water
idx = -1
wb2.plot_areas_3panels(axes3=axes[idx], styles3=[style2]*3, 
                       centered=True, show_errorbars=False)
wb7.plot_areas_3panels(axes3=axes[idx], styles3=[style7]*3, 
                       centered=True, show_errorbars=False)
str2 = 'hydrated SC1-2 (800$\degree$C)'
str7 = 'hydrated SC1-7 (1000$\degree$C)'
axes[-1][0].text(-1200, 45, str7, color=style7['color'])
axes[-1][0].text(-1200, 1, str2, color=style2['color'])
for idx, ax in enumerate(axes[idx]):
    ax.set_title(''.join(('Profile || ', wb2.directions[idx],
                          ' and R || ', wb2.raypaths[idx])))

### peak heights
for pidx, peak in enumerate(peaks): 
    currentaxes = axes[pidx]
    for axidx in range(3):
        # SC1-7
        prof = wb7.profiles[axidx]
        x = prof.positions_microns - prof.length_microns/2.
        y = prof.peak_heights[pidx]
        line = currentaxes[axidx].plot(x, y, 's', label=str(peak), 
                          markersize=4, color=style7['color'])
        
        # SC1-2
        prof = wb2.profiles[axidx]
        x = prof.positions_microns - prof.length_microns/2.
        line = currentaxes[axidx].plot(x, prof.peak_heights[pidx], 'o', 
                          label=str(peak), markersize=4, color=style2['color'])

ytops = iter([0.3, 0.7, 0.7, 0.3, 120])
for idx in range(5):
    ytop = next(ytops)
    for ax in axes[idx]:
        ax.set_ylim(0, ytop)

###### diffusion curves ######
D3 = dlib.KM98_slow.whatIsD(1000, printout=False) # pv mechanism diffusivities
true_solubility = exper.solubility_of_H_in_olivine(Celsius=1000, 
                                                   pressure_GPa=1, 
                                                   author='Mosenfelder',
                                                   printout=False)
metastable = np.mean(list(itertools.chain(*wb2.areas)))
for ax in axes[-1]:
    ax.plot(ax.get_xlim(), [metastable, metastable], ':', color=style2['color'])
wb7.plot_diffusion(axes3=axes[-1], 
                   log10D_m2s=D3, 
                   init=metastable, 
                   fin=true_solubility, 
                   show_line_at_1=False,
                   wholeblock_diffusion=True, 
                   show_data=False,
                   labelD=True, labelDy=90)

maxarea = max([max(areas) for areas in wb7.areas])
scale_final = true_solubility / maxarea # to scale up to true solubility
for idx in range(4):
    peak_heights7 = [profile.peak_heights[idx] for profile in wb7.profiles]
    peak_heights2 = [profile.peak_heights[idx] for profile in wb2.profiles]
    maxy = max([max(heights) for heights in peak_heights7])
    meta = np.mean(list(itertools.chain(*peak_heights2)))
    wb7.plot_diffusion(axes3=axes[idx], log10D_m2s=D3,
                       init=meta, fin=maxy*scale_final,
                       show_line_at_1=False, wholeblock_diffusion=True, 
                       show_data=False, labelD=False)
    for ax in axes[idx]:
        ax.plot(ax.get_xlim(), [meta, meta], ':', color=style2['color'])
        ax.set_ylim(0, maxy*scale_final)

fig.savefig(SC.thisfolder+'\..\Fig4_hydration_profiles.jpg', 
            dpi=300, format='jpg')        