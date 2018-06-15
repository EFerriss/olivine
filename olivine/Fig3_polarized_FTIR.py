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
import os
import olivine

file = os.path.join(olivine.__path__[0], 'Fig3_polarized_FTIR.tif')

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

old_style = {'color': '#1f77b4', 'linestyle' : '-'}
kiki_style = {'color': 'darkmagenta', 'linestyle':'-'}
SC2_style = {'color': '#2ca02c', 'linestyle':'-'}

def plot_stuff(spec, ax, my_style):
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
    ax.set_ylabel('')
    ax.set_yticklabels(empty_string_labels)

ax = fig.add_axes([x, y+hspace+h, w, h])
spec = SC.SC_untreated_Ea
plot_stuff(spec, ax, old_style)
ax.text(3900, ytext, 'A. untreated\nSC1-1 E||a', va='top')
ax.set_ylabel('Absorbance (cm$^{-1}$)')

ax = fig.add_axes([x+wspace+w, y+hspace+h, w, h])
spec = SC.SC_untreated_Eb
plot_stuff(spec, ax, old_style)
ax.text(3900, ytext, 'B. untreated\nSC1-1 E||b', va='top')
remove_labels(ax)

ax = fig.add_axes([x+2*wspace+2*w, y+hspace+h, w, h])
spec = SC.SC_untreated_Ec
plot_stuff(spec, ax, old_style)
ax.text(3900, ytext, 'C. untreated\nSC1-1 E||c', va='top')
remove_labels(ax)

ax = fig.add_axes([x+3*wspace+3*w, y+hspace+h, w, h])
spec = SC.spec2
plot_stuff(spec, ax, SC2_style)
ax.text(3900, ytext, 'D. hydrated\nSC1-2 E||a', va='top')
remove_labels(ax)

ax = fig.add_axes([x, y, w, h])
spec = kiki.Kiki_init_Ea
plot_stuff(spec, ax, kiki_style)
ax.text(3900, ytext, 'E.\nKiki\nE||a', va='top')
ax.set_ylabel('Absorbance (cm$^{-1}$)')

ax = fig.add_axes([x+wspace+w, y, w, h])
spec = kiki.Kiki_init_Eb
plot_stuff(spec, ax, kiki_style)
ax.text(3900, ytext, 'F. Kiki E||b', va='top')
remove_labels(ax)

ax = fig.add_axes([x+2*wspace+2*w, y, w, h])
spec = kiki.Kiki_init_Ec
plot_stuff(spec, ax, kiki_style)
ax.text(3900, ytext, 'G. Kiki E||c', va='top')
remove_labels(ax)

ax = fig.add_axes([x+3*wspace+3*w, y, w, h])
spec = SC.SC_final_averaged
plot_stuff(spec, ax, SC2_style)
ax.text(3900, ytext, 'H. dehydrated\nSC1-2  E||a', va='top')
remove_labels(ax)

ax.text(5500, -0.3, 'Wavenumber (cm$^{-1}$)', ha='center')

fig.savefig(file, dpi=300, format='tif')
