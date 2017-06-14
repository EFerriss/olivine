# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Dehydration San Carlos olivine SC1-2

Data details and peak heights are in SanCarlos_spectra.py. Baselines
were created in SanCarlos_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.SanCarlos import SanCarlos_spectra as SC
from pynams import dlib
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

water = 14.
peaks = SC.peaks
initial = SC.wb_800C_hyd
final = SC.wb_800C_7hr
wb_list = [initial, final]

for wb in wb_list:
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=peaks)
    wb.areas = [prof.areas for prof in wb.profiles]
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]
    wb.style['color'] = '#2ca02c'
    wb.style['markeredgecolor'] = '#2ca02c'

# best-fit diffusivities || a
fast = dlib.KM98_fast.whatIsD(800, printout=False)[0:3]
slow = dlib.KM98_slow.whatIsD(800, printout=False)[0:3]
final.D_list = []
vD = [[True, False, False], [True, False, False], [True, False, False]]
D3 = [slow, fast, fast]
finals = [0.4, 0., 0.15]
for f, D, ploc, varyD in zip(finals, D3, [0, 1, None], vD):
    fitD3, fiti, fitf = final.fitD(wholeblock_data=True, 
                                wholeblock_diffusion=True,
                                log10Ds_m2s=D, show_plot=False,
                                vary_diffusivities=varyD,
                                fin=f,
                                peak_idx=ploc, heights_instead=True)
    final.D_list.append(fitD3)
   
#%%
final.D_list[0] = [ufloat(-12.5, 0), ufloat(-15.3, 0), ufloat(-14.2, 0)]
final.D_list[2][0] = ufloat(-11.4, 0)

styles = [wb.style for wb in wb_list]
styleD = {'color':'#2ca02c', 'linewidth':3, 'marker':None, 'linestyle':'--',
          'alpha':0.75, 'label':'least-squares'}

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
axes[-1][0].set_ylabel('bulk hydrogen\n(ppm H$_2$O) rel. to init')
axes[0][0].set_ylabel('[Si-Fe$^{2+}$] peak\nheight rel. to init)')
axes[1][0].set_ylabel('[Ti-3525] peak\nheight rel. to init')

# whole block or raw data?
wbdata = True

ytops = [1.4]*3
ybots = [0.0, 0, 0]
for top, bot, ax3 in zip(ytops, ybots, axes):    
    for ax in ax3:
        ax.set_ylim(bot, top)

idx = 2
for wb, style in zip(wb_list, styles):
    wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                       centered=True, show_errorbars=False, 
                       wholeblock=wbdata, scale=1, show_line_at_1=True)

for idx in range(2):
    for wb, style in zip(wb_list, styles):
        wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                               centered=True, show_errorbars=False, 
                               peak_idx=idx, heights_instead=True,
                               scale=1., wholeblock=wbdata, 
                               show_line_at_1=True)
    axes[idx][1].set_title('')

fast = dlib.KM98_fast.whatIsD(800, printout=False)[0:3]
DSi = list(np.array(fast) - 1)
D3 = [fast, fast, fast]
peaklocs = [0, 1, None]
ytext = [0.2, 0.2, 0.2]
for f, ax3, D, ploc, D3fit, yt in zip(finals, axes, D3, peaklocs, final.D_list, ytext):
    final.plot_diffusion(log10D_m2s=D, show_data=False, axes3=ax3,
                         wholeblock_diffusion=True, labelDy=0.4, 
                         labelD=False)
    fD3 = [diff.n for diff in D3fit]
    final.plot_diffusion(log10D_m2s=fD3, show_data=False, axes3=ax3,
                         wholeblock_diffusion=True, labelDy=0.4, 
                         fin=f,
                         labelD=False, style_diffusion=styleD)
    string = ''.join(('best fit || a\n', 
                      '{:.1f}'.format(D3fit[0]), 
                       '\nlogD in m2/s'))
    ax3[0].text(0, yt, string, color=styleD['color'], 
       va='center', ha='center')
        
wb = initial
for ax, direction, raypath in zip(axes[-1], wb.directions, wb.raypaths):
    ax.set_title(''.join(('|| ', direction, ', R || ', raypath)))

axes[0][2].plot(0, -10, '-k', linewidth=1, label='p.p. mechanism')
axes[0][2].legend(loc=4)

fig.savefig(SC.thisfolder+'\..\SuppFig8_SC_7hr.jpg', 
            dpi=400, format='jpg')    
