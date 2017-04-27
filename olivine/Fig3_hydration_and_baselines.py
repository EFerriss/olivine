# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:09:50 2017

@author: Elizabeth

Show SC1-7 hydration
"""
from __future__ import print_function
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine import thisfolder
import matplotlib.pyplot as plt

wb7 = SC.wb_1000C_SC1_7
wb7.get_baselines()

wb2 = SC.wb_800C_hyd
wb2.get_baselines()

spec7 = wb7.average_spectra()
spec2 = wb2.average_spectra()
speci = SC.SC_untreated_Ea

fig = plt.figure()
fig.set_size_inches(6.5, 4)

xstart = 0.1
ypstart = 0.1
wgap = 0.1
width1 = 0.47
width2 = 0.75 - width1
height = 0.8
hgap = 0.07
height2 = (height-hgap)/2.
ax = fig.add_axes([xstart, ypstart, width1, height])
ax2 = fig.add_axes([xstart+width1+wgap, ypstart+height2+hgap, width2, height2])
ax3 = fig.add_axes([xstart+width1+wgap, ypstart, width2, height2])

speci.plot_spectrum(axes=ax, label='initial', offset=-0.03,
                    style={'linewidth':4, 'alpha':0.5})
spec7.plot_spectrum(axes=ax, label='SC1-7', offset=-0.07)
spec2.plot_spectrum(axes=ax, label='SC1-2')
ax.set_ylim(0, 1.)
ax.set_title('')
ax.set_xlabel('wavenumbers (cm$^{-1}$)')
ax.set_ylabel('absorbance (cm$^{-1}$)')
ax.text(3530, 0.02, 'untreated SC1-1', color='#1f77b4')
ax.text(3630, 0.15, 'hydrated\nSC1-2', color='#2ca02c', ha='right')
ax.text(3620, 0.5, 'hydrated\nSC1-7', color='#ff7f0e', ha='right')
ax.text(3950, 0.92, 'A', fontsize=14)

peaks = [3236, 3356, 3396, 3484, 3525, 3573, 3600]
labels = ['[Mg]', '[tri]', '[tri]', '[Si]', '[Ti]', '[Ti]', '[Si]']
for pidx, peak in enumerate(peaks):
    idx = abs(speci.wn_full-peak).argmin()
    y = spec7.abs_full_cm[idx] - 0.05
    ax.text(peak, y, ' '.join(('$\\leftarrow$', str(peak), labels[pidx])), 
            rotation=90, ha='center', va='bottom')

ax2.text(3950, 0.67, 'B', fontsize=14)
ax2.text(3900, 0.3, 'hydrated\nSC1-7\nwith', color='#ff7f0e', va='bottom')
ax2.text(3900, 0.3, 'baseline', va='top')
speci.plot_spectrum(axes=ax2, label='initial', offset=-0.03,
                    style={'linewidth':5, 'alpha':0.5})
spec7.plot_spectrum(axes=ax2, label='SC1-7', offset=-0.07)
spec7.fname = 'SC1-7-average'
spec7.get_baseline(folder=SC.FTIR_file_location)
ax2.plot(spec7.base_wn, spec7.base_abs-0.07,'k')
ax2.set_ylim(0, 0.8)
ax2.set_title('')
ax2.set_ylabel('absorbance (cm$^{-1}$)')
ax2.text(3520, 0.02, 'untreated SC1-1', color='#1f77b4')

ax3.text(3950, 0.42, 'C', fontsize=14)
ax3.text(3900, 0.18, 'hydrated\nSC1-2\nwith', color='#2ca02c', va='bottom')
ax3.text(3900, 0.18, 'baseline', va='top')
speci.plot_spectrum(axes=ax3, label='initial', offset=-0.03,
                    style={'linewidth':4, 'alpha':0.5})
spec2.plot_spectrum(axes=ax3, label='SC1-2', style={'color':'#2ca02c'})
spec2.fname = 'SC1-2-average'
spec2.get_baseline(folder=SC.FTIR_file_location)
ax3.plot(spec2.base_wn, spec2.base_abs,'k')
ax3.set_ylim(0, 0.5)
ax3.set_title('')
ax3.set_ylabel('absorbance (cm$^{-1}$)')
ax3.set_xlabel('wavenumbers (cm$^{-1}$)')
ax3.text(3530, 0.02, 'untreated SC1-1', color='#1f77b4')

fig.savefig(thisfolder+'Fig3_hydration_and_baselines.jpg', dpi=200, 
            format='jpg')
