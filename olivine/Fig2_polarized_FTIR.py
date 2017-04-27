# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:13:13 2017

@author: Elizabeth
H diffusion in olivine

Create subplots of initial polarized FTIR spectra for San Carlos olivine
and Kilauea Iki olivine, plus estimate water concentrations for San Carlos
olivine after final dehydration step
"""
from __future__ import print_function
from olivine.SanCarlos import SanCarlos_spectra as SC
from olivine.KilaueaIki import Kiki_spectra as kiki
from pynams import styles
import matplotlib.pyplot as plt

plt.close('all')
numformat = '{:.0f}'

fig = plt.figure()
fig.set_size_inches(6.5, 4)

x = 0.1
y = 0.19
w = 0.18
h = 0.31
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

ax = fig.add_axes([x, y+hspace+h, w, h])
spec = SC.spec2
plot_stuff(spec, ax)
ax.text(3900, ytext, 'hydrated\nSC1-2 E||a', va='top')
ax.set_ylabel('Absorbance (cm$^{-1}$)')

ax = fig.add_axes([x+wspace+w, y+hspace+h, w, h])
spec = kiki.Kiki_init_Ea
plot_stuff(spec, ax)
ax.text(3900, ytext, 'Kiki\nE||a', va='top')
remove_labels(ax)

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
ax.set_ylabel('Absorbance (cm$^{-1}$)')

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

ax.text(5500, -0.3, 'Wavenumber (cm$^{-1}$)', ha='center')

fig.savefig(SC.thisfolder+'\..\Fig2_polarized_FTIR.jpg', dpi=200, format='jpg')
