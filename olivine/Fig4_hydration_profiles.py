# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing hydration profiles in San Carlos olivines for bulk 
hydrogen, [Si-Fe2+] at 3600, and [Ti] at 3525 cm-1

All other profiles are going into the supplement.
"""
from __future__ import print_function
from olivine import thisfolder
from olivine.SanCarlos import SanCarlos_spectra as SC
from pynams import dlib
import numpy as np
import matplotlib.pyplot as plt
import itertools
import pynams.experiments as exper

conversion_factor_area2water = 0.6 # see Table1_concentrations.py

wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
wb2.get_baselines()
wb7.get_baselines()
wb2.make_areas()
wb7.make_areas()

areas = []
profidx = itertools.cycle([0, 1, 2])
for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
        wb.areas[next(profidx)] = prof.areas
        areas.append(max(prof.areas))
maxarea = max(areas)
metastable = np.mean([ar for ar in wb2.areas][0])
print('max H SC1-7', maxarea, 'ppm H2O')
print('metastable equilibrium', metastable, 'ppm H2O')
print()

style2 = {'color':'#2ca02c', 'marker':'o', 'linestyle': 'none'}
style7 = {'color':'#ff7f0e', 'marker':'s', 'linestyle': 'none'}
style7D = {'color':'#ff7f0e', 'linestyle': '-'}

#%%
fig = plt.figure()
fig.set_size_inches(6.5, 6)

peaks = ['bulk H', 3600, 3525]

# make the axes
xstart = 0.125
ypstart = 0.07
wgap = 0.01
width = 0.26
height = 0.27
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
axes[2][0].set_ylabel('bulk hydrogen\n(ppm H$_2$O)')
axes[1][0].set_ylabel('[Si-Fe$^{2+}$] peak\nheight (cm$^{-1}$)')
axes[0][0].set_ylabel('[Ti-3525] peak\nheight (cm$^{-1}$)')

# bulk water
wb2.plot_areas_3panels(axes3=axes[2], styles3=[style2]*3, 
                       centered=True, show_errorbars=False)
wb7.plot_areas_3panels(axes3=axes[2], styles3=[style7]*3, 
                       centered=True, show_errorbars=False)
for idx, ax in enumerate(axes[2]):
    ax.set_ylim(0, 120)
    ax.set_title(''.join(('Profile || ', wb2.directions[idx],
                          ' and R || ', wb2.raypaths[idx])))
#str2 = 'SC1-2 hydrated\n17.5hr at 800$\degree$C, 1GPa'    
#str7 = 'SC1-7 hydrated\n7hr at 1000$\degree$C, 1GPa'
str2 = 'hydrated SC1-2 (800$\degree$C)'
str7 = 'hydrated SC1-7 (1000$\degree$C)'
axes[2][0].text(-1200, 45, str7, color=style7['color'])
axes[2][0].text(-1200, 3, str2, color=style2['color'])

# plot peak heights
max_peakheight = [0, 0]
mean_metastable = [0, 0]

for pidx, peak in enumerate([3525, 3600]): 
    currentaxes = axes[pidx]
    for axidx in range(3):
        # SC1-7
        prof = wb7.profiles[axidx]
        heights = []
        for spec in prof.spectra:
            idx = np.abs(peak - spec.base_wn).argmin()
            heights.append(spec.abs_nobase_cm[idx])
            if spec.abs_nobase_cm[idx] > max_peakheight[pidx]:
                max_peakheight[pidx] = spec.abs_nobase_cm[idx]
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
        mean_metastable[pidx] = np.mean([h for h in heights2][0])

    print()
    print('peak', peak, 'cm-1')
    print('max peak height', max_peakheight[pidx])
    print('mean SC1-2', mean_metastable[pidx])

for idx, ax in enumerate(axes[0]):
    ax.set_ylim(0, 0.6)

for idx, ax in enumerate(axes[1]):
    ax.set_ylim(0, 0.3)

#### diffusion! ######
# bulk H
trueC = exper.solubility_of_H_in_olivine(Celsius=1000, pressure_GPa=1, 
                                 author='Mosenfelder')

#D3 = [-12., -12., -11.1] # log10 m2/s
D3 = dlib.KM98_slow.whatIsD(1000)
finfrac = trueC / maxarea
wb7.plot_diffusion(axes3=axes[2], fin=finfrac, show_line_at_1=False,
                   wholeblock_diffusion=True, show_data=False,
                   init=metastable/maxarea, log10D_m2s=D3, labelD=True)

# [Si peak]
#D3Si = [-12.8, -13.5, -11.2] # log10 m2/s
wb7.plot_diffusion(axes3=axes[1], fin=max_peakheight[1]*finfrac/maxarea,
                   show_line_at_1=False, wholeblock_diffusion=True, 
                   show_data=False, labelD=True, log10D_m2s=D3,
                   init=mean_metastable[1]/maxarea)

# [Ti peak]
#D3Ti = [-12.8, -12.6, -11.1] # log10 m2/s
wb7.plot_diffusion(axes3=axes[0], fin=max_peakheight[0]*finfrac/maxarea,
                   show_line_at_1=False, wholeblock_diffusion=True, 
                   show_data=False, labelD=True, log10D_m2s=D3,
                   init=mean_metastable[0]/maxarea)

metastables = mean_metastable + [metastable]
for idx, ax3 in enumerate(axes):
    meta = metastables[idx]
    for ax in ax3:
        ax.plot(ax.get_xlim(), [meta, meta], ':', color=style2['color'])
    

fig.savefig(thisfolder+'Fig4_hydration_profiles.jpg', dpi=200, format='jpg')
