# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:09:50 2017

@author: Elizabeth

Comparison of initial FTIR spectra of olivines SC1-2 and Kiki 
"""
from __future__ import print_function
from pynams import styles
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
from olivine import thisfolder


specSCinit = SC.SC_untreated_Ea
specSC = SC.wb_800C_hyd_averagespec
specSCfinal = SC.wb_800C_68hr.average_spectra()
specKiki = kiki.wb_Kiki_init_ave
specKikiFinal = kiki.wb_Kiki_ox_ave

specSC.get_baseline()
specKiki.get_baseline()
#specKikiFinal.get_baseline()
#specKiki.get_baseline()

styleSC = {'color':'#2ca02c', 'linewidth':2}
styleKiki = {'color':'darkmagenta', 'linewidth':2}

kikioffset = 0.54
kikioffsetFinal = 0.5
SCoffset = 0.02

#%%
fig, ax = styles.plot_spectrum_outline()
#
x = specSC.wn_full
y1 = specSC.abs_full_cm
y2 = specSCfinal.abs_full_cm + SCoffset
ax.fill_between(x, y1, y2, where=y1>=y2, color=styleSC['color'], alpha=0.2)

x = specKiki.wn_full
y1 = specKiki.abs_full_cm + kikioffset
y2 = specKikiFinal.abs_full_cm + kikioffsetFinal
ax.fill_between(x, y1, y2, where=y1>=y2, color=styleKiki['color'], alpha=0.2)

#specSCinit.plot_spectrum(axes=ax, offset=-0.03)
specSC.plot_showbaseline(axes=ax, style=styleSC)
specKiki.plot_showbaseline(axes=ax, style=styleKiki, offset=kikioffset)
specSCfinal.plot_spectrum(axes=ax, offset=SCoffset, 
                          style={'color':styleSC['color'], 'linewidth':1})
specKikiFinal.plot_spectrum(axes=ax, 
                            style={'color':styleKiki['color'], 'linewidth':1},
                            offset=kikioffsetFinal)

fig.set_size_inches(6, 4)
ax.set_ylim(0, 1.5)
ax.set_title('')
xtxt = 3780
ax.text(xtxt, 1.3, 'Kilauea Iki', color=styleKiki['color'], 
        ha='left', va='center', backgroundcolor='w')
ax.text(xtxt, 0.24, 'San Carlos\nSC1-2', color='#2ca02c', ha='left', 
        backgroundcolor='none')
#ax.text(3480, 0.63, 'baseline')
ax.annotate('initial', xy=(3575, 1.1), xytext=(3690, 1.1), 
            color=styleKiki['color'], 
            arrowprops=dict(facecolor='k', arrowstyle='->',
                            color=styleKiki['color']))
ax.annotate('dehydrated', xy=(3500, 0.71), xytext=(3470, 0.58), 
            color=styleKiki['color'], backgroundcolor='w',
            arrowprops=dict(facecolor='k', arrowstyle='->',
                            color=styleKiki['color']))
ax.annotate('baseline', xy=(3550, 0.65), xytext=(3530, 0.5), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))
ax.annotate('hydrated', xy=(3520, 0.23), xytext=(3480, 0.3), 
            color=styleSC['color'], 
            arrowprops=dict(facecolor='k', arrowstyle='->',
                            color=styleSC['color']))
ax.annotate('dehydrated', xy=(3510, 0.08), xytext=(3460, 0.21), 
            color=styleSC['color'], 
            arrowprops=dict(facecolor='k', arrowstyle='->',
                            color=styleSC['color']))
ax.annotate('baseline', xy=(3470, 0.07), xytext=(3395, 0.02), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))


peaks = [3329, 3356, 3484, 3525, 3573, 3600]
for peak in peaks:
    idx = abs(specKiki.wn_full-peak).argmin()
    y = specKiki.abs_full_cm[idx] + kikioffset + 0.06
    ax.text(peak, y, '$\\leftarrow$'+str(peak),
            rotation=90, ha='center', va='bottom')

ax.set_ylabel('Absorbance (cm$^{-1}$)')    
fig.subplots_adjust(bottom=0.17, left=0.1, right=0.95, top=0.95)
fig.savefig(thisfolder+'Fig5_SC_vs_Kiki.jpg', dpi=200, format='jpg')

#print('done')