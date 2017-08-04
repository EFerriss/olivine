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
from uncertainties import ufloat
import itertools
from pynams import dlib
import numpy as np
import matplotlib.pyplot as plt
import os
import olivine

file = os.path.join(olivine.__path__[0], 'Fig4_hydration_profiles.jpg')
   
peaks = SC.peaks

# set up areas and convert them to water concentrations
conversion_factor_area2water = 0.6 # see Table1_concentrations.py
wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
wb2.get_baselines()
wb7.get_baselines()
wb2.make_areas()
wb7.make_areas()
wb2.make_peakheights(peaks=peaks)
wb7.make_peakheights(peaks=peaks)

profidx = itertools.cycle([0, 1, 2])
for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = list(prof.areas * conversion_factor_area2water)
        wb.areas[next(profidx)] = prof.areas

D3 = dlib.KM98_slow.whatIsD(1000, printout=False) # pv mechanism diffusivities
true_solubility = 58.
#true_solubility = exper.solubility_of_H_in_olivine(Celsius=1000, 
#                                                   pressure_GPa=1, 
#                                                   author='Mosenfelder',
#                                                   printout=False)
metastable = np.mean(list(itertools.chain(*wb2.areas)))
maxarea = max([max(areas) for areas in wb7.areas])
scale_final = true_solubility / maxarea # to scale up to true solubility

#### for least-squares best fits
#wb7.peak_D3 = [[]]*4
#for idx in range(4):
#    peak_heights7 = [profile.peak_heights[idx] for profile in wb7.profiles]
#    peak_heights2 = [profile.peak_heights[idx] for profile in wb2.profiles]
#    maxy = max([max(heights) for heights in peak_heights7])
#    meta = np.mean(list(itertools.chain(*peak_heights2)))
#    wb7.peak_D3[idx], init, fin = wb7.fitD(peak_idx=idx, show_plot=False,
#                                       heights_instead=True, 
#                                       wholeblock_data=False,
#                                       init=meta, 
#                                       fin=maxy*scale_final,
#                                       log10Ds_m2s=D3,
#                                       vary_final=False,
#                                       vary_diffusivities=[False, False, True])
#wb7.D3, wb7.init, wb7.fin = wb7.fitD(peak_idx=None, init=metastable,
#                                     fin=true_solubility, show_plot=False,
#                                     wholeblock_data=False,
#                                     log10Ds_m2s=D3, 
#                                     vary_diffusivities=[False, False, True])
#

#%% The least squares fits are sooooo low! I don't believe them!
### manually setting all of the diffusivities such that bulk H || c is the
### consistestent with established values for proton-vacancy diffusion 
### and the relative errors remain constant
slow = dlib.KM98_slow.whatIsD(celsius=1000, printout=False)
uslow = [ufloat(D, 0) for D in slow[0:3]]
wb7.D3 = np.copy(uslow)
wb7.peak_D3 = np.copy([np.copy(uslow)] * (len(peaks)+1))
wb7.D3[2] = ufloat(-10.8, 0)
wb7.peak_D3[3][2] = ufloat(-10.5, 0)
wb7.peak_D3[2][2] = ufloat(-10.8, 0)
wb7.peak_D3[1][2] = ufloat(-11.1, 0)
wb7.peak_D3[0][2] = ufloat(-11.5, 0)

#% the figure
style2 = wb2.style
style7 = wb7.style
styleD = {'color': 'grey', 'linestyle':'-', 'linewidth':3, 
          'label':'p.v.'}
style7['label'] = 'SC1-7 (p.v.)'
style2['label'] = 'SC1-2 (p.p. done)'
     
fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.125
ypstart = 0.09
wgap = 0.005
width = 0.26
height = 0.15
hgap = 0.03
ytxt_shift = 0.3
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

## bulk water
idx = -1
wb2.plot_areas_3panels(axes3=axes[idx], styles3=[style2]*3, 
                       centered=True, show_errorbars=False)
wb7.plot_areas_3panels(axes3=axes[idx], styles3=[style7]*3, 
                       centered=True, show_errorbars=False)
for idx, ax in enumerate(axes[idx]):
    ax.set_title(''.join(('|| ', wb2.directions[idx],
                          ', R || ', wb2.raypaths[idx])))

### peak heights
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

# axes limits
ytops = iter([0.3, 0.7, 0.7, 0.3, 58])
for idx in range(5):
    ytop = next(ytops)
    for ax in axes[idx]:
        ax.set_ylim(0, ytop)
for ax in axes:
    ax[0].set_xlim(-1400, 1400)    
    ax[1].set_xlim(-550, 550)
    ax[2].set_xlim(-1500, 1500)

# diffusion
for ax in axes[-1]:
    ax.plot(ax.get_xlim(), [metastable, metastable], ':', color=style2['color'])
wb7.plot_diffusion(axes3=axes[-1], 
                   log10D_m2s=D3, 
                   init=metastable, 
                   fin=true_solubility, 
                   show_line_at_1=False,
                   wholeblock_diffusion=True, 
                   show_data=False, style_diffusion=styleD,
                   labelD=False, labelDy=90)
D4plot = [D.n for D in wb7.D3]
wb7.plot_diffusion(axes3=axes[-1], log10D_m2s=D4plot, init=metastable, 
                   fin=true_solubility, show_line_at_1=False,
                   wholeblock_diffusion=True, show_data=False,
                   labelD=False, labelDy=90, points=200,
                   style_diffusion={'color':style7['color'],'linewidth':1})
string = ''.join(('logD in m$^2$/s\n','{:.1f}'.format(D4plot[2])))
ytxt = axes[-1][2].get_ylim()[1] - ytxt_shift*axes[idx][2].get_ylim()[1]
axes[-1][2].text(0, ytxt, string, color=style7['color'], 
                  va='center', ha='center')


for idx in range(4):
    peak_heights7 = [profile.peak_heights[idx] for profile in wb7.profiles]
    peak_heights2 = [profile.peak_heights[idx] for profile in wb2.profiles]
    maxy = max([max(heights) for heights in peak_heights7])
    meta = np.mean(list(itertools.chain(*peak_heights2)))
    wb7.plot_diffusion(axes3=axes[idx], log10D_m2s=D3,
                       init=meta, fin=maxy*scale_final,
                       show_line_at_1=False, wholeblock_diffusion=True, 
                       show_data=False, labelD=False, style_diffusion=styleD)
    for ax in axes[idx]:
        ax.plot(ax.get_xlim(), [meta, meta], ':', color=style2['color'])
        ax.set_ylim(0, maxy*scale_final)

    D4plot = [D.n for D in wb7.peak_D3[idx]]
    print()
    print(idx)
    print('initial', meta)
    print('final', maxy*scale_final)
    wb7.plot_diffusion(axes3=axes[idx], log10D_m2s=D4plot,
                       init=meta, fin=maxy*scale_final,
                       show_line_at_1=False, wholeblock_diffusion=True, 
                       show_data=False, labelD=False, points=200,
                       style_diffusion={'color':style7['color'],'linewidth':1,
                                        'label':'best-fit'})
    string = ''.join(('logD in m$^2$/s\n','{:.1f}'.format(D4plot[2])))
    ytxt = axes[idx][2].get_ylim()[1] - ytxt_shift*axes[idx][2].get_ylim()[1]
    axes[idx][2].text(0, ytxt, string, color=style7['color'], 
                      va='center', ha='center')

axes[0][2].legend(loc=1, ncol=2, bbox_to_anchor=(-0.25, 0))

fig.savefig(file, dpi=300, format='jpg')        