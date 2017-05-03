# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing hydration profiles in San Carlos olivines for bulk 
hydrogen, [Si-Fe2+] at 3600, and [Ti] at 3525 cm-1

All other profiles are going into the supplement.
"""
from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
from pynams import dlib
import numpy as np
import matplotlib.pyplot as plt
import itertools
import pynams.experiments as exper

wb7 = SC.wb_1000C_SC1_7
for prof in wb7.profiles:
    print(prof.name)
    print(prof.peak_heights)
    print()
    
#%%    
conversion_factor_area2water = 0.6 # see Table1_concentrations.py
peaks = SC.peaks

wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
#wb2.get_baselines()
#wb7.get_baselines()
#wb2.make_areas()
#wb7.make_areas()
#areas = []
#profidx = itertools.cycle([0, 1, 2])
#for wb in [wb2, wb7]:
#    for prof in wb.profiles:
#        prof.areas = list(prof.areas * conversion_factor_area2water)
#        wb.areas[next(profidx)] = prof.areas
#        areas.append(max(prof.areas))
#maxarea = max(areas)
#metastable = np.mean([ar for ar in wb2.areas][0])

for prof in wb7.profiles:
    print(prof.name)
    print(prof.peak_heights)
    print()

#%%
max_peakheight = list(np.zeros(len(peaks)))
mean_peakmetastable = [[]] * (len(peaks))
for pidx, peak in enumerate(peaks[1:]): 
    prof.peak_heights[pidx] = []
    for axidx in range(3):
        # SC1-7
        prof = wb7.profiles[axidx]
        print(prof.peak_heights)
#        for idx in range(len(prof.spectra)):
#            height = prof.peak_heights[idx]
#            print(height)
#            if height > max_peakheight[pidx]:
#                max_peakheight[pidx] = height
#        x = prof.positions_microns - prof.length_microns/2.
#        y = prof.peak_heights[pidx]
#        # SC1-2
#        prof = wb2.profiles[axidx]
#        prof.peak_heights[pidx] = []
#        for spec in prof.spectra:
#            idx = np.abs(peak - spec.base_wn).argmin()
#            prof.peak_heights[pidx].append(spec.abs_nobase_cm[idx])
#        x = prof.positions_microns - prof.length_microns/2.
#        mean_metastable[pidx] = np.mean([h for h in prof.peak_heights[pidx]][0])
#
#%%
D3 = log10Ds_m2s=dlib.KM98_slow.whatIsD(1000, printout=False)
wb7.D3, wb7.init, wb7.fin = wb7.fitD(peak_idx=None, init=metastable,
                                     fin=maxarea, wholeblock_data=False,
                                     log10Ds_m2s=D3, 
                                     vary_diffusivities=[False, False, True])

#%%
wb7.peak_D3 = [[]]*4
trueC = exper.solubility_of_H_in_olivine(Celsius=1000, pressure_GPa=1, 
                                 author='Mosenfelder')
finfrac = trueC / maxarea
for idx in range(4):
    wb7.peak_D3[idx], init, fin = wb7.fitD(peak_idx=idx, 
                                       heights_instead=True, 
                                       wholeblock_data=False,
                                       init=mean_metastable[idx], 
                                       fin=max_peakheight[idx]*finfrac,
                                       log10Ds_m2s=D3,
                                       vary_diffusivities=[False, False, True])

#%%
for idx in range(4):
    print('peak at', wb7.profiles[0].peakpos[idx], 'cm-1')
    print('{:.1f}'.format(wb7.peak_D3[idx][2]), 'log10 m2/s || c')
    print()
#%%
#pidx = 0
#D31, init1, fin1 = wb7.fitD(peak_idx=pidx,
#                            heights_instead=True,
#                            init=mean_metastable[pidx], 
#                            fin=max_peakheight[pidx], 
#                            vary_final=False, 
#                            vary_initial=False,
#                            log10Ds_m2s=dlib.KM98_slow.whatIsD(1000)[0:3],
#                            vary_diffusivities=[False, False, True],
#                            show_plot=True, 
#                            wholeblock_diffusion=True,
#                            wholeblock_data=False)


#%% the figure
style2 = {'color':'#2ca02c', 'marker':'o', 'linestyle': 'none'}
style7 = {'color':'#ff7f0e', 'marker':'s', 'linestyle': 'none'}
style7D = {'color':'#ff7f0e', 'linestyle': '-'}

fig = plt.figure()
fig.set_size_inches(6.5, 8)

xstart = 0.125
ypstart = 0.07
wgap = 0.01
width = 0.26
height = 0.15
hgap = 0.025
axes = []

for peak in peaks:
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
axes[3][0].set_ylabel('[Si-Fe$^{2+}$] peak\nheight (cm$^{-1}$)')
axes[2][0].set_ylabel('[Ti-3525] peak\nheight (cm$^{-1}$)')
axes[1][0].set_ylabel('[tri-Fe$^{3+}$] peak\nheight (cm$^{-1}$)')
axes[0][0].set_ylabel('[Mg] peak\nheight (cm$^{-1}$)')

# bulk water
idx = -1
wb2.plot_areas_3panels(axes3=axes[idx], styles3=[style2]*3, 
                       centered=True, show_errorbars=False)
wb7.plot_areas_3panels(axes3=axes[idx], styles3=[style7]*3, 
                       centered=True, show_errorbars=False)
str2 = 'hydrated SC1-2 (800$\degree$C)'
str7 = 'hydrated SC1-7 (1000$\degree$C)'
axes[2][0].text(-1200, 0.35, str7, color=style7['color'])
axes[2][0].text(-1200, 0.1, str2, color=style2['color'])
for idx, ax in enumerate(axes[idx]):
    ax.set_title(''.join(('Profile || ', wb2.directions[idx],
                          ' and R || ', wb2.raypaths[idx])))

## peak heights
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

ytops = iter([0.1, 0.2, 0.7, 0.3, 120])
for idx in range(5):
    ytop = next(ytops)
    for ax in axes[idx]:
        ax.set_ylim(0, ytop)

##### diffusion! ######
trueC = exper.solubility_of_H_in_olivine(Celsius=1000, pressure_GPa=1, 
                                 author='Mosenfelder')
D3 = dlib.KM98_slow.whatIsD(1000)
finfrac = trueC / maxarea
#fin=max_peakheight[idx]*finfrac/maxarea
#wb7.plot_diffusion(axes3=axes[-1], fin=finfrac, show_line_at_1=False,
#                   wholeblock_diffusion=True, show_data=False,
#                   init=metastable/maxarea, log10D_m2s=D3, labelD=True)
#
#for idx in range(4):
#    wb7.plot_diffusion(axes3=axes[idx], log10D_m2s=D3,
#                       init=mean_metastable[idx]/maxarea,
#                       fin=max_peakheight[idx]*finfrac/maxarea,
#                       show_line_at_1=False, wholeblock_diffusion=True, 
#                       show_data=False, labelD=False)

#%%

#%%

#%%
Dpeaks = [[]]*4
for idx in range(4):
    final = max_peakheight[idx]*finfrac/maxarea
    Dpeaks[idx], init, fin = wb7.fitD(peak_idx=None, heights_instead=True,
                                      init=mean_metastable[idx]/maxarea,
                                      fin=final,
                                      wholeblock_data=False, 
                                      show_plot=False,
                                      log10Ds_m2s=D3, 
                                      vary_diffusivities=[False, False, False],
                                      wholeblock_diffusion=True)

#%%
#    wb7.plot_diffusion(axes3=axes[idx], log10D_m2s=Dpeaks[idx],
#                       init=mean_metastable[idx]/maxarea,
#                       fin=max_peakheight[idx]*finfrac/maxarea,
#                       show_line_at_1=False, wholeblock_diffusion=True, 
#                       show_data=False, labelD=False, 
#                       style_diffusion={'color':style7['color']})


#metastables = mean_metastable + [metastable]
#for idx, ax3 in enumerate(axes):
#    meta = metastables[idx]
#    for ax in ax3:
#        ax.plot(ax.get_xlim(), [meta, meta], ':', color=style2['color'])
#    
#fig.savefig(thisfolder+'Fig4_hydration_profiles.jpg', dpi=200, format='jpg')

#%% best-fits to SC1-7 data
#D31, init1, fin1 = wb7.fitD(init=metastable, 
#                            fin=exper.solubility_of_H_in_olivine(1000), 
#                            vary_final=False, vary_initial=False,
#                            log10Ds_m2s=dlib.KM98_slow.whatIsD(1000)[0:3],
#                            vary_diffusivities=[False, False, True],
#                            show_plot=True, wholeblock_diffusion=True,
#                            wholeblock_data=False)

