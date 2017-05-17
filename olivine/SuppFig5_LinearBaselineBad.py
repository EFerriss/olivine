# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:38:59 2017

@author: Ferriss

Example of an SC1-2 spectrum for which linear baselines will not work.
"""

from __future__ import print_function
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine import thisfolder

#%%
idx = 0
spec = SC.wb_800C_43hr.profiles[0].spectra[idx]
loc = SC.wb_800C_13hr.profiles[0].positions_microns[idx]
spec.get_baseline()
fig, ax = spec.plot_showbaseline(style={'color':'#2ca02c'})
fig.set_size_inches(6.5, 4)
#spec.get_baseline(baseline_ending=high_ending)
#spec.plot_showbaseline(axes=ax)
ax.set_ylim(0, 0.25)

peaks = [3329, 3356]
for peak in peaks:
    idx = abs(spec.wn_full-peak).argmin()
    y = spec.abs_full_cm[idx] + 0.01
    ax.text(peak, y, '$\\leftarrow$'+str(peak), fontsize=8, 
            rotation=90, ha='center', va='bottom')

txt = ''.join(('FTIR spectrum\n', str(loc), ' $\mu$m from edge of SC1-2',
               '\nAfter 43 hours at 800$\degree$C'))
ax.text(3950, 0.21, txt, fontsize=12, ha='left', va='center', 
        backgroundcolor='w')

#txt = 'linear baseline\nresults in\nnegative\narea'
#ax.annotate(txt, xy=(3500, 0.07), xytext=(3460, 0.11), #backgroundcolor='w',
#            ha='center', va='center',
#            arrowprops=dict(facecolor='k', arrowstyle='->'))

txt = 'quadratic baseline\nused to determine\narea for profile'
ax.annotate(txt, xy=(3350, 0.07), xytext=(3020, 0.03), backgroundcolor='w',
            ha='right', va='center',
            arrowprops=dict(facecolor='k', arrowstyle='->'))

fig.savefig(thisfolder+'SuppFig5_LinearBaselinesBad.jpg', 
            dpi=400, format='jpg')
