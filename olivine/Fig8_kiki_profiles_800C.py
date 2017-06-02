# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Hydrogen profiles for Kilauea Iki olivine Kiki

Data details and peak heights are in Kiki_spectra.py. Baselines
were created in Kiki_baselines.py and are stored in the same
folder as the original FTIR data.
"""
from __future__ import print_function, division
from olivine.KilaueaIki import Kiki_spectra as kiki
import matplotlib.pyplot as plt
   
peaks = kiki.peaks

wbinit = kiki.wb_Kiki_init
wb_list = [
           kiki.wb_Kiki_init,
           kiki.wb_Kiki_1hr, 
           kiki.wb_Kiki_8hr, 
#           kiki.wb_Kiki_1000C_3hr,
#           kiki.wb_Kiki_1000C_6hr,
#           kiki.wb_Kiki_1000C_7hr,
#           kiki.wb_Kiki_ox
           ]
for wb in wb_list:
    wb.get_baselines()
    wb.make_areas()
    wb.make_peakheights(peaks)
    wb.peak_heights = [prof.peak_heights for prof in wb.profiles]

#%%
styles = [wb.style for wb in wb_list]
for style in styles:
    style['color'] = 'darkmagenta'
    style['markeredgecolor'] = 'darkmagenta'

fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.14
ypstart = 0.17
wgap = 0.01
width = 0.26
height = 0.17
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
axes[-1][0].set_ylabel('bulk hydrogen\nrelative to initial')
axes[0][0].set_ylabel('[Si-Fe$^{2+}$] peak\nheight / initial height')
axes[1][0].set_ylabel('[Ti-3525] peak\nheight / initial height')
axes[2][0].set_ylabel('[tri-Fe$^{3+}$-3356] peak\nheight / initial height')

# axes limits
#ytops = [0.2, 1., 0.2, 100]
ytops = [2.5, 1.5, 1.2, 2.]
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
                              wholeblock=True, show_line_at_1=True,
                              peak_idx=peakidx, heights_instead=hplot)
    ax3[1].set_title(' ')

for ax, direction, raypath in zip(axes[-1], wbinit.directions, wbinit.raypaths):
    ax.set_title(''.join(('|| ', direction, ', R || ', raypath)))

axes[-1][1].text(0, 1.8, 'noisy spectra at 8hrs', ha='center', va='center',
    color='darkmagenta')
#initial = mean of the initial across all profiles
#initials = [0]*4
#initials[3] = np.mean(list(itertools.chain(*wbinit.areas)))
#for idx in range(3):
#    x, y = wbinit.xy_picker(peak_idx=idx, wholeblock=False, 
#                            heights_instead=True)
#    initials[idx] = np.mean(list(itertools.chain(*y)))
#for ax3, init in zip(axes, initials):
#    for ax in ax3:
#        ax.plot(ax.get_xlim(), [init, init], ':', color=style3['color'])

#axes[0][2].legend(ncol=3, title='Kilauea Iki olivine', 
#   bbox_to_anchor=[0.7, -0.4], loc=1)

axes[1][2].legend(ncol=3, title='Kilauea Iki olivine', 
   bbox_to_anchor=[0.9, 0.3], loc=1)

for ax in axes[0]:
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=60)

fig.savefig(kiki.thisfolder+'\..\Fig8_kiki_profiles_800C.jpg', 
            dpi=400, format='jpg')        
