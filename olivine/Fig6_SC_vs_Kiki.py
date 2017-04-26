# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:09:50 2017

@author: Elizabeth

Comparison of initial FTIR spectra of olivines SC1-2 and Kiki 
before dehydration
"""
from __future__ import print_function
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
from olivine import thisfolder

styleSC = {'color':'#2ca02c'}
styleKiki = {'color':'purple', 'linewidth':2}

specSC = SC.wb_800C_hyd.average_spectra()
specKiki = kiki.wb_Kiki_init.average_spectra()

#%%
fig, ax = specSC.plot_spectrum(style=styleSC)
specKiki.plot_spectrum(axes=ax, style=styleKiki)

fig.set_size_inches(6, 3.5)
ax.set_ylim(0, 0.8)
ax.set_title('')
ax.text(3760, 0.55, 'Kilauea Iki', color=styleKiki['color'], 
        ha='left', va='center')
ax.text(3330, 0.116, 'hydrated San Carlos', color='#2ca02c', ha='left')


peaks = [3329, 3356, 3484, 3525, 3573, 3600]
for peak in peaks:
    idx = abs(specKiki.wn_full-peak).argmin()
    y = specKiki.abs_full_cm[idx] + 0.03
    ax.text(peak, y, '$\\leftarrow$'+str(peak),
            rotation=90, ha='center', va='bottom')
    
fig.savefig(thisfolder+'Fig6_SC_vs_Kiki.jpg', dpi=200, format='jpg')
