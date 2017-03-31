# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing hydration profiles in San Carlos olivines
"""
from __future__ import print_function
from olivine import thisfolder, high_ending, low_ending
from olivine.SanCarlos import SanCarlos_spectra as SC
from pynams import dlib
import matplotlib.pyplot as plt
import numpy as np

# data
conversion_factor_area2water = 4./7. # see Table 1
wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
spec7 = SC.spec7
spec2 = SC.spec2

# figure details
xstart = 0.09
ypstart = 0.1
wgap = 0.01
width = 0.2
height = 0.8
wgapb = 0.08
offset = 0.4
length = 6.5
heighttotal = 3.5
style2 = {'color':'#2ca02c', 'marker':'o', 'linestyle': 'none'}
style7 = {'color':'#ff7f0e', 'marker':'s', 'linestyle': 'none'}
style2a = {'color':'#2ca02c', 'marker':'o', 'linestyle': 'none', 'alpha':0.3}
style7a = {'color':'#ff7f0e', 'marker':'s', 'linestyle': 'none', 'alpha':0.3}
style2D = {'color': style2['color'], 'linestyle': '-'}
style7D = {'color': style7['color'], 'linestyle': '-'}
styleb = {'color':'k', 'linestyle':'-', 'linewidth':4}
def plot_stuff(wb2, wb7, spec2, spec7, diffusivities):
    wb2.make_areas()
    wb7.make_areas()
    spec2.make_area(printout=False)
    spec7.make_area(printout=False)
    fig = plt.figure()
    fig.set_size_inches(length, heighttotal)
    ax1 = fig.add_axes([xstart, ypstart, width, height])
    ax4 = fig.add_axes([xstart+width+wgapb, ypstart, width, height])
    ax5 = fig.add_axes([xstart+width+wgapb+width+wgap, ypstart, width, height])
    ax6 = fig.add_axes([xstart+width+wgapb+2*width+2*wgap, ypstart, width, height])
    areas = []
    for wb in [wb2, wb7]:
        for prof in wb.profiles:
            prof.areas = prof.areas * conversion_factor_area2water
            areas.append(max(prof.areas))
    wb2.plot_areas_3panels(axes3=[ax4, ax5, ax6], styles3=[style2]*3, 
                           centered=True, show_errorbars=False)
    wb7.plot_areas_3panels(axes3=[ax4, ax5, ax6], styles3=[style7]*3, 
                           centered=True, show_errorbars=False)
    spec2.plot_showbaseline(axes=ax1, style=style2D)
    spec7.plot_showbaseline(axes=ax1, style=style7D, offset=offset)
    ax5.set_title('')
    ax1.set_xlim(4000, 3000)
    ax1.set_ylim(0, 1.25)
    for idx, ax in enumerate([ax4, ax5, ax6]):
#        if wb2.sample.lengths_microns[idx] > wb7.sample.lengths_microns[idx]:
#            set_x_lim = wb2.sample.lengths_microns[idx] / 2.
#        else:
#            set_x_lim = wb7.sample.lengths_microns[idx] / 2.
#        ax.set_xlim(-set_x_lim, set_x_lim)
        ax.set_ylim(0, 60)
    ax4.set_xlabel('x (mm)')
    ax5.set_xlabel('y (mm)')
    ax6.set_xlabel('z (mm)')
    ax4.set_ylabel('Hydrogen (ppm H$_2$O)')
    for ax in [ax5, ax6]:
        ax.axes.get_yaxis().set_ticks([])
    ax1.set_xlabel('wavenumbers (cm$^{-1}$)')
    ax1.set_ylabel('average absorbance (cm$^{-1}$)')
    ax1.text(3020, 0.05, 'SC1-2\nhydrated', color=style2['color'], ha='right')
    ax1.text(3500, 1., 'SC1-7\nhydrated', color=style7['color'], ha='left')
    xp2 = 0.8
    yp = 55
    ax4.text(ax4.get_xlim()[1]*xp2, yp, '  || [100]', ha='right', va='center')
    ax5.text(ax5.get_xlim()[1]*xp2, yp, '  || [010]', ha='right', va='center')
    ax6.text(ax6.get_xlim()[1]*xp2, yp, '  || [001]', ha='right', va='center')
    areas = list(wb2.areas[0]) + list(wb2.areas[1]) + list(wb2.areas[2])
    metastable_equilib = np.mean(areas) * conversion_factor_area2water
    for ax in [ax4, ax5, ax6]:
        ax.plot(ax.get_xlim(), [metastable_equilib, metastable_equilib], '--',
                color=style2['color'])
    init = metastable_equilib / max(wb7.areas[2])
    wb7.plot_diffusion(wholeblock_data=True, wholeblock_diffusion=True,
                       centered=True, log10D_m2s=diffusivities, fin=1, 
                       init=0, axes3=[ax4, ax5, ax6],
                       show_line_at_1=False, labelD=False)
    return fig, [ax4, ax5, ax6], metastable_equilib
    
# 1st figure
wb2.get_baselines()
wb7.get_baselines()
spec2.get_baseline(print_confirmation=False)
spec7.get_baseline(print_confirmation=False)

diff = dlib.KM98_slow.whatIsD(celsius=1000, printout=False)[0:3]
fig, ax3, metastable_equilib = plot_stuff(wb2, wb7, spec2, spec7, diff)



#%%
### add areas from high, linear baselines
wb2.get_baselines(baseline_ending=high_ending)
wb7.get_baselines(baseline_ending=high_ending)
wb2.make_areas()
wb7.make_areas()
spec2.get_baseline(baseline_ending=high_ending)
spec7.get_baseline(baseline_ending=high_ending)

for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = prof.areas * conversion_factor_area2water

wb2.plot_areas_3panels(axes3=[ax4, ax5, ax6], styles3=[style2]*3, 
                       centered=True, show_errorbars=False)
wb7.plot_areas_3panels(axes3=[ax4, ax5, ax6], styles3=[style7]*3, 
                       centered=True, show_errorbars=False)

spec2.plot_showbaseline(axes=ax1, style=style2D, style_base=styleb)
spec7.plot_showbaseline(axes=ax1, style=style7D, offset=offset, 
                        style_base=styleb)

### diffusion curves for *linear* baselines
slow = dlib.KM98_slow.whatIsD(celsius=1000, printout=False)[0:3]
#slow = list(np.array(slow) + 0.6)
initial=8
wb7.plot_diffusion(wholeblock_data=False, wholeblock_diffusion=True,
                   centered=True, log10D_m2s=slow, fin=1, 
                   init=initial/maxarea, axes3=[ax4, ax5, ax6],
                   show_line_at_1=False, labelD=False, 
                   style_diffusion=styleb)

faster = dlib.KM98_slow.whatIsD(celsius=1060, printout=False)[0:3]
wb7.plot_diffusion(wholeblock_data=False, wholeblock_diffusion=True,
                   centered=True, log10D_m2s=faster, fin=1, 
                   init=initial/maxarea, axes3=[ax4, ax5, ax6],
                   show_line_at_1=False, labelD=False, 
                   style_diffusion={'color':'blue'})

for ax in [ax4, ax5, ax6]:
    ax.plot(ax.get_xlim(), [initial, initial], '--k')

### add areas from low baselines
wb2.get_baselines(baseline_ending=low_ending)
wb7.get_baselines(baseline_ending=low_ending)
wb2.make_areas()
wb7.make_areas()
spec2.get_baseline(baseline_ending=low_ending)
spec7.get_baseline(baseline_ending=low_ending)
for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = prof.areas * conversion_factor_area2water
        areas.append(max(prof.areas))
wb2.plot_areas_3panels(axes3=[ax4, ax5, ax6], styles3=[style2a]*3, 
                       centered=True, show_errorbars=False)
wb7.plot_areas_3panels(axes3=[ax4, ax5, ax6], styles3=[style7a]*3, 
                       centered=True, show_errorbars=False)
spec2.plot_showbaseline(axes=ax1, style=style2D)
spec7.plot_showbaseline(axes=ax1, style=style7D, offset=offset)


### clean up axes

fig.savefig(thisfolder+'Fig4_hydration_profiles_range.jpg', dpi=200, format='jpg')
