# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Heating of Kilauea Iki olivine

Data details and peak heights are in Kiki_spectra.py. Baselines
were created in Kiki_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.KilaueaIki import Kiki_spectra as kiki
from pynams import dlib
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#%%
water = 15.
peaks = kiki.peaks
initial = kiki.wb_Kiki_init
final = kiki.wb_Kiki_1hr
wb_list = [initial, final]

for wb in wb_list:
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks=peaks)
    wb.areas = [prof.areas for prof in wb.profiles]
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]
    wb.style['color'] = 'darkmagenta'
    wb.style['markeredgecolor'] = 'darkmagenta'

# best-fit diffusivities || a
fast = dlib.KM98_fast.whatIsD(800, printout=False)[0:3]
slow = dlib.KM98_slow.whatIsD(800, printout=False)[0:3]
final.D_list = []
for ploc in [0, 1, 2, None]:
    fitD3, fiti, fitf = final.fitD(wholeblock_data=True, 
                                wholeblock_diffusion=True,
                                log10Ds_m2s=fast, show_plot=False,
                                vary_diffusivities=[True, False, False],
                                peak_idx=ploc, heights_instead=True)
    final.D_list.append(fitD3)
   
#%%
# manually set upper limit values for plot
final.D_list[0][0] = ufloat(-12.5, 0)
final.D_list[1][0] = ufloat(-12.5, 0)
#final.D_list[3][0] = ufloat(-12.0, 0)

styles = [wb.style for wb in wb_list]
styleD = {'color':'darkmagenta', 'linewidth':3, 'marker':None, 'linestyle':'--',
          'alpha':0.75, 'label':'fit || a'}
styleslow = {'color':'k', 'linewidth':3, 'label':'p.v', 'alpha':0.5}
stylefast = {'color':'k', 'linewidth':1, 'label':'p.p.'}

fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.125
ypstart = 0.11
wgap = 0.01
width = 0.26
height = 0.19
hgap = 0.03
axes = []

# create axes
for peak in range(4):
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
axes[2][0].set_ylabel('[tri-Fe$^{3+}$] peak\nheight rel. to init')

# whole block or raw data?
wbdata = True

ytops = [2.5, 1.4, 1.4, 1.4]
ybots = [0.0, 0, 0, 0]
for top, bot, ax3 in zip(ytops, ybots, axes):    
    for ax in ax3:
        ax.set_ylim(bot, top)

idx = -1
for wb, style in zip(wb_list, styles):
    wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                       centered=True, show_errorbars=False, 
                       wholeblock=wbdata, scale=1, show_line_at_1=True)

for idx in range(3):
    for wb, style in zip(wb_list, styles):
        wb.plot_areas_3panels(axes3=axes[idx], styles3=[style]*3, 
                               centered=True, show_errorbars=False, 
                               peak_idx=idx, heights_instead=True,
                               scale=1., wholeblock=wbdata, 
                               show_line_at_1=True)
    axes[idx][1].set_title('')

fast = dlib.KM98_fast.whatIsD(800, printout=False)[0:3]
DSi = list(np.array(fast) - 1)
peaklocs = [0, 1, 2, None]
ytxts = [0.1, 0.1, 0.525, 0.1]
for ax3, ploc, D3fit, ytxt in zip(axes, peaklocs, final.D_list, ytxts):
    fD3 = [diff.n for diff in D3fit]
    final.plot_diffusion(log10D_m2s=fD3, show_data=False, axes3=ax3,
                         wholeblock_diffusion=True, labelDy=0.4, 
                         labelD=False, style_diffusion=styleD)
    final.plot_diffusion(log10D_m2s=fast, show_data=False, axes3=ax3,
                         wholeblock_diffusion=True, labelDy=0.4, 
                         labelD=False, style_diffusion=stylefast)
    final.plot_diffusion(log10D_m2s=slow, show_data=False, axes3=ax3,
                         wholeblock_diffusion=True, labelDy=0.4, 
                         labelD=False, style_diffusion=styleslow)  
    string = ''.join(('{:.1f}'.format(D3fit[0]), 
                       '\nlogD in m2/s'))
    ax3[0].text(0, ytxt, string, color=styleD['color'], 
       va='bottom', ha='center')

wb = initial
for ax, direction, raypath in zip(axes[-1], wb.directions, wb.raypaths):
    ax.set_title(''.join(('|| ', direction, ', R || ', raypath)))

axes[1][2].legend(loc=1, ncol=2,
                  bbox_to_anchor=[0.9, 0.5],)


for ax in axes[0]:
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=60)
    
fig.savefig(kiki.thisfolder+'\..\SuppFig13_kiki_1hr.jpg', 
            dpi=400, format='jpg')    
