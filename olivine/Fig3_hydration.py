# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:09:50 2017

@author: Elizabeth

Show SC1-7 hydration
"""
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine import thisfolder
import numpy as np
from uncertainties import ufloat

wb7 = SC.wb_1000C_SC1_7
wb7.get_baselines()

wb2 = SC.wb_800C_hyd
wb2.get_baselines()

spec7 = wb7.average_spectra()
spec2 = wb2.average_spectra()
speci = SC.SC_untreated_Ea

#%%

fig, ax = speci.plot_spectrum(label='initial', offset=-0.03)
spec7.plot_spectrum(axes=ax, label='SC1-7', offset=-0.07)
spec2.plot_spectrum(axes=ax, label='SC1-2')
ax.set_ylim(0, 0.9)
ax.set_title('')
ax.text(3530, 0.02, 'untreated SC1-1', color='#1f77b4')
ax.text(3630, 0.15, 'hydrated\nSC1-2', color='#2ca02c', ha='right')
ax.text(3620, 0.5, 'hydrated\nSC1-7', color='#ff7f0e', ha='right')

peaks = [3236, 3356, 3396, 3484, 3525, 3573, 3600]
for peak in peaks:
    idx = abs(speci.wn_full-peak).argmin()
    y = spec7.abs_full_cm[idx] - 0.05
    ax.text(peak, y, '$\\leftarrow$'+str(peak), 
            rotation=90, ha='center', va='bottom')
#fig.set_size_inches(9, 9)
ax.grid(False)
fig.set_size_inches(3.5, 3.5)
fig.savefig(thisfolder+'Fig3_hydration.jpg', dpi=200, format='jpg')

#%% areas to water
high_ending = '-high-baseline.CSV'
low_ending = '-low-baseline.CSV'

speci.get_baseline()
speci.make_area()
speci.water = ufloat(4, 1) # From FTIR + SIMS, see Table 1

for wb in [wb7, wb2]:
    wb.areas = []
    for prof in wb.profiles:
        for spec in prof.spectra:
            spec.get_baseline(print_confirmation=False)
            wb.areas.append(spec.make_area(printout=False))
    wb.area = ufloat(np.average(wb.areas), np.std(wb.areas))
    print()
    print(wb.name)
    print(wb.area, 'cm-2 area with only 1 baseline')
    print('{:.3}'.format((wb.area/speci.area).n), 
          'times relative increase from initial area')
    print('{:.3}'.format(((wb.area/speci.area)*speci.water)), 'ppm H2O')
#    print(pynams.area2water(wb.area, phase='ol'), 'ppm H2O Bell')
#    print(pynams.area2water(wb.area, phase='ol', calibration='Withers'),
#          'ppm H2O Withers')