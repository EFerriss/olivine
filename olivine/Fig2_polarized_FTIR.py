# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:13:13 2017

@author: Elizabeth
H diffusion in olivine

Create subplots of initial polarized FTIR spectra for San Carlos olivine
and Kilauea Iki olivine, plus estimate water concentrations for San Carlos
olivine after final dehydration step
"""
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
from pynams import pynams, styles
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

plt.close('all')
numformat = '{:.0f}'

SCi_list = [SC.SC_untreated_Ea, SC.SC_untreated_Eb, SC.SC_untreated_Ec]
SCf = SC.SC_final_averaged
Kiki_list = [kiki.Kiki_init_Ea, kiki.Kiki_init_Eb, kiki.Kiki_init_Ec]
spec_list = Kiki_list + SCi_list

#%% Get water concentration estimates from FTIR
# All baselines made and saved in Kiki_baseline.py and SanCarlos_baseline.py
baselines = ['-high-baseline.CSV', '-baseline.CSV', '-low-baseline.CSV']

kiki_area = ufloat(0, 0)
kiki_Withers = ufloat(0, 0)
kiki_Bell = ufloat(0, 0)
kiki_SIMS = ufloat(14, 1.2)
print()
print('Kilauea Iki olivine')
for spec in Kiki_list:
    areas = []
    for baseline in baselines:
        spec.get_baseline(baseline_ending=baseline, print_confirmation=False)
        areas.append(spec.make_area(printout=False))
    spec.area = ufloat(np.mean(areas), np.std(areas))
    print('{:.3u}'.format(spec.area), 'cm-2 area || 1 direcion')
    spec.Withers = pynams.area2water(spec.area, phase='olivine',
                                   calibration='Withers')
    spec.Bell = pynams.area2water(spec.area, phase='olivine',
                                  calibration='Bell')
    kiki_area = kiki_area + spec.area
    kiki_Withers = kiki_Withers + spec.Withers
    kiki_Bell = kiki_Bell + spec.Bell
kiki_ave = np.mean([kiki_Withers, kiki_Bell, kiki_SIMS])
print('{:.3u}'.format(kiki_area), 'cm-2 area')
print(kiki_Withers, 'ppm H2O with Withers calibration') 
print(kiki_Bell, 'ppm H2O with Bell calibration')
print(kiki_SIMS, 'ppm H2O by nanoSIMS')
print(kiki_ave, 'ppm H2O average')

SC_area = ufloat(0, 0)
SC_Withers = ufloat(0, 0)
SC_Bell = ufloat(0, 0)
SC_SIMS = ufloat(5, 0.87)
print()
print('San Carlos olivine initial')
for spec in SCi_list:
    areas = []
    for baseline in baselines:
        spec.get_baseline(baseline_ending=baseline, print_confirmation=False)
        areas.append(spec.make_area(printout=False))
    spec.area = ufloat(np.mean(areas), np.std(areas))
    spec.Withers = pynams.area2water(spec.area, phase='olivine',
                                   calibration='Withers')
    spec.Bell = pynams.area2water(spec.area, phase='olivine',
                                  calibration='Bell')
    SC_area = SC_area + spec.area
    SC_Withers = SC_Withers + spec.Withers
    SC_Bell = SC_Bell + spec.Bell
    print('{:.2u}'.format(spec.area), 'cm-2 area || 1 direcion')
SC_ave = np.mean([SC_Bell, SC_Withers, SC_SIMS])

print('{:.2u}'.format(SC_area), 'cm-2 area total')
print(SC_Withers, 'ppm H2O with Withers calibration') 
print(SC_Bell, 'ppm H2O with Bell calibration')
print(SC_SIMS, 'ppm H2O by nanoSIMS')
print(SC_ave, 'ppm H2O average')

SCf_area = ufloat(0, 0)
SCf_Withers = ufloat(0, 0)
SCf_Bell = ufloat(0, 0)
spec = SC.SC_final_averaged
areas = []
for baseline in baselines:
    spec.get_baseline(baseline_ending=baseline, print_confirmation=False)
    areas.append(spec.make_area(printout=False))
#    spec.plot_showbaseline()
spec.area = ufloat(np.mean(areas), np.std(areas))
spec.Withers = pynams.area2water(spec.area, phase='olivine',
                               calibration='Withers')
spec.Bell = pynams.area2water(spec.area, phase='olivine',
                              calibration='Bell')

print()
print('San Carlos olivine initial vs final E||a')
print('{:.2u}'.format(SC.SC_untreated_Ea.area), 'area cm-2 initial')
print('{:.2u}'.format(SC.SC_final_averaged.area), 'area cm-2 final')

#%% Figure showing baselines
fig = plt.figure()
fig.set_size_inches(6.5, 4)

x = 0.12
y = 0.2
w = 0.16
h = 0.27
wspace = 0.04
hspace = 0.12
ylim = 0.65
ylimSC = ylim
ytext = 0.6

def plot_stuff(spec, ax):
    my_style = {'color': 'blue', 'linestyle' : '-'}
    spec.get_baseline(print_confirmation=False)
    spec.plot_showbaseline(axes=ax, style=my_style)
    spec.get_baseline(baseline_ending='-high-baseline.CSV', 
                      print_confirmation=False)
    ax.plot(spec.base_wn, spec.base_abs, **styles.style_1)
    spec.get_baseline(baseline_ending='-low-baseline.CSV', 
                      print_confirmation=False)
    ax.plot(spec.base_wn, spec.base_abs, **styles.style_1)
    ax.set_xlim(4000, 3000)
    ax.set_ylim(0, ylimSC)
    plt.setp(ax.get_xticklabels(), rotation=45)    

def remove_labels(ax):
    labels = [item.get_text() for item in ax.get_yticklabels()]
    empty_string_labels = ['']*len(labels)
    ax.set_yticklabels(empty_string_labels)

ax = fig.add_axes([x+wspace+w, y+hspace+h, w, h])
spec = kiki.Kiki_init_Ea
plot_stuff(spec, ax)
ax.text(3900, ytext, 'Kiki\nE||a', va='top')
#ylabel = ''.join(('Absorbance (cm$^{-1}$)\nKilauea Iki olivine\nSIMS: ',
#                  str(kiki_SIMS)))
ax.set_ylabel('Absorbance (cm$^{-1}$)\nKilauea Iki olivine')

ax = fig.add_axes([x+2*wspace+2*w, y+hspace+h, w, h])
spec = kiki.Kiki_init_Eb
plot_stuff(spec, ax)
ax.text(3900, ytext, 'Kiki E||b', va='top')
remove_labels(ax)

ax = fig.add_axes([x+3*wspace+3*w, y+hspace+h, w, h])
spec = kiki.Kiki_init_Ec
plot_stuff(spec, ax)
ax.text(3900, ytext, 'Kiki E||c', va='top')
remove_labels(ax)

ax = fig.add_axes([x, y, w, h])
spec = SC.SC_final_averaged
plot_stuff(spec, ax)
#ax.text(3900, ytext, 'dehydrated\nSC1-2  E||a\n\nSIMS:\n'+str(SC_SIMS), va='top')
ax.text(3900, ytext, 'dehydrated\nSC1-2  E||a', va='top')
ax.set_ylabel('Absorbance (cm$^{-1}$)\nSan Carlos olivine')

ax = fig.add_axes([x+wspace+w, y, w, h])
spec = SC.SC_untreated_Ea
plot_stuff(spec, ax)
ax.text(3900, ytext, 'untreated\nSC1-1 E||a', va='top')
remove_labels(ax)

ax = fig.add_axes([x+2*wspace+2*w, y, w, h])
spec = SC.SC_untreated_Eb
plot_stuff(spec, ax)
ax.text(3900, ytext, 'untreated\nSC1-1 E||b', va='top')
remove_labels(ax)

ax = fig.add_axes([x+3*wspace+3*w, y, w, h])
spec = SC.SC_untreated_Ec
plot_stuff(spec, ax)
ax.text(3900, ytext, 'untreated\nSC1-1 E||c', va='top')
remove_labels(ax)

ax.text(5500, -0.4, 'Wavenumber (cm$^{-1}$)', ha='center')

fig.savefig(SC.thisfolder+'\..\Fig2_polarized_FTIR.jpg', dpi=200, format='jpg')
