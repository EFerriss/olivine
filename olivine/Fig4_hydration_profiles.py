# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing hydration profiles in San Carlos olivines
"""
from olivine import thisfolder
from olivine.SanCarlos import SanCarlos_spectra as SC
from pynams import styles, dlib
from pynams.diffusion.models import diffusion3Dwb

wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd

wb2.get_baselines()

high_ending = '-high-baseline.CSV'
low_ending = '-low-baseline.CSV'

#%%
slow = dlib.KM98_slow.whatIsD(celsius=1000, printout=False)

wb7.get_baselines()
wb7.make_areas()
fig, ax3 = wb7.plot_diffusion(wholeblock_data=False, wholeblock_diffusion=True, 
                              centered=False, log10D_m2s=slow,
                              fin=1., init=15/96.6, show_line_at_init=False)
wb2.plot_areas_3panels(axes3=ax3, styles3=[styles.style_points0]*3, 
                       centered=False)

wb7.get_baselines(baseline_ending=high_ending)
wb7.make_areas()
wb7.plot_areas_3panels(axes3=ax3)

wb7.get_baselines(baseline_ending=low_ending)
wb7.make_areas()
wb7.plot_areas_3panels(axes3=ax3)

for idx, ax in enumerate(ax3):
    ax.set_xlim(0, wb7.lengths[idx])
    ax.set_ylim(0, 150)

fig.set_size_inches(12, 6)