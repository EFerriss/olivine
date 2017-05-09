# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Dehydration profiles for Kilauea Iki olivine Kiki

Data details and peak heights are in Kiki_spectra.py. Baselines
were created in Kiki_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.KilaueaIki import Kiki_spectra as kiki
from olivine.KilaueaIki.Kiki_baselines import baseline
import matplotlib.pyplot as plt
from pynams import styles as st
import itertools
import numpy as np
reload(kiki)
   
peaks = kiki.peaks

wbinit = kiki.wb_Kiki_8hr
wb_list = [
           kiki.wb_Kiki_init,
           kiki.wb_Kiki_1hr, 
           kiki.wb_Kiki_8hr, 
           kiki.wb_Kiki_1000C_3hr,
           kiki.wb_Kiki_1000C_6hr,
           kiki.wb_Kiki_1000C_7hr,
           kiki.wb_Kiki_ox
           ]

#%%
# set up areas and convert them to water concentrations
#conversion_factor_area2water = 0.3 # see Table1_concentrations.py
for wb in wb_list:
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks)
#    for prof in wb.profiles:
#        prof.areas = list(prof.areas * conversion_factor_area2water)
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]


#%%
#% the figure
styleinit = {'color':'grey', 'marker':'o', 'linestyle': 'none', 'markersize':8,
             'label': 'initial', 'alpha':0.5,}
style1 = {'color':'r', 'marker':'+', 'linestyle':'none', 'markersize':9,
          'markeredgewidth':1.5, 'label':'1 hr 800$\degree$C QFM-2'}
style3 = {'markeredgecolor':'chocolate', 'marker':'^', 'linestyle':'none', 
           'markersize':7, 'markeredgewidth':1.5, 'color':'chocolate',
           'label':'8 hr 800$\degree$C QFM-2',
           'markerfacecolor':'none'}
style7 = {'color':'goldenrod', 'marker':'x', 'linestyle':'none', 
           'markersize':6, 'markeredgewidth':1.5, 
           'label':'+3 hr 1000$\degree$C QFM-2'}
style13 = {'color':'g', 'marker':'p', 'linestyle':'none', 'markersize':6,
          'markeredgewidth':1.5, 'alpha':0.4, 
          'label':'6 hr 1000$\degree$C QFM-2'}
style19 = {'markeredgecolor':'b', 'marker':'s', 'linestyle':'none', 
           'markersize':4, 'markerfacecolor':'none', 'color':'b',
          'markeredgewidth':1, 'alpha':0.5, 
          'label':'7 hr 1000$\degree$C QFM-2'}
style43 = {'color':'indigo', 'marker':'x', 'linestyle':'none', 'markersize':4,
          'markeredgewidth':1,
          'label':'+1 more hr at\n1000$\degree$C QFM+2.7'}

styles = [styleinit, style1, style3, style7, style13, style19, style43]

#%%
fig, axs = st.plot_spectrum_outline()
for style, wb in zip(styles, wb_list):   
    spec = wb.profiles[1].spectra[6]
    spec.make_baseline(**baseline)
    spec.plot_subtractbaseline(axes=axs, style={'color':style['color']},
                               label=style['label'])

for peak in peaks:
    axs.text(peak, 0.2, str(peak), va='center', ha='center')
axs.set_ylim(0, 0.6)
axs.legend()

#%%
fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.14
ypstart = 0.17
wgap = 0.005
width = 0.26
height = 0.17
hgap = 0.03
axes = []

# create axes
for peak in range(4):
    ax1 = fig.add_axes([xstart, ypstart, width, height])
    ax2 = fig.add_axes([xstart+width+wgap, ypstart, width, height])
    ax3 = fig.add_axes([xstart+2*width+2*wgap, ypstart, width, height])
#    ax1.set_xlim(-1200, 1200)
#    ax2.set_xlim(-950, 950)
#    ax3.set_xlim(-700, 700)
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
axes[2][0].set_ylabel('[tri-Fe$^{3+}$-3356] peak\nheight (cm$^{-1}$)')

# axes limits
ytops = [0.2, 0.2, 0.2, 100]
ybots = [0, 0, 0, 0]
for top, bot, ax3 in zip(ytops, ybots, axes):    
    for ax in ax3:
        ax.set_ylim(bot, top)

# plot, baby, plot
plotheight = [True, True, True, False]    
for ax3, peakidx, hplot in zip(axes, [0, 1, 2, None], plotheight):
    for wb, style in zip(wb_list, styles):
        wb.plot_areas_3panels(axes3=ax3, styles3=[style]*3,
                              centered=True, show_errorbars=False, 
                              wholeblock=False,
                              peak_idx=peakidx, heights_instead=hplot)
    ax3[1].set_title(' ')

for ax, direction, raypath in zip(axes[-1], wbinit.directions, wbinit.raypaths):
    ax.set_title(''.join(('|| ', direction, ', R || ', raypath)))

#initial = mean of the initial across all profiles
initials = [0]*4
initials[3] = np.mean(list(itertools.chain(*wbinit.areas)))
for idx in range(3):
    x, y = wbinit.xy_picker(peak_idx=idx, wholeblock=False, 
                            heights_instead=True)
    initials[idx] = np.mean(list(itertools.chain(*y)))
for ax3, init in zip(axes, initials):
    for ax in ax3:
        ax.plot(ax.get_xlim(), [init, init], ':', color=style3['color'])

axes[0][2].legend(ncol=3, title='Kilauea Iki olivine', 
   bbox_to_anchor=[1, -0.4], loc=1)

fig.suptitle('Quadratic baselines')
fig.savefig(kiki.thisfolder+'\..\Fig7_kiki_dehydration_profiles.jpg', 
            dpi=400, format='jpg')        
#
#
