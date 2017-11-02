# -*- coding: utf-8 -*-
"""
@author: Elizabeth Ferriss

Arrhenius diagram showing selected results for 
H movement in olivine.

Additional results can be visualized at the 
Arrhenius diagram app online at 
https://arrheniusdiagram.herokuapp.com/
"""

from __future__ import print_function, division
import matplotlib.pyplot as plt
import os
import olivine
import pynams
from pynams import dlib
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.patches as patches
from pynams import dlib


matplotlib.rcParams.update({'font.size': 8})

GAS_CONSTANT = 0.00831 # kJ/mol K

file = os.path.join(olivine.__path__[0], 'Fig10_ArrheniusDiagram.jpg')

# get the data from file in pynams
datafile = os.path.join(pynams.__path__[0], 'diffusion', 'literaturevalues.csv')
olivine = pd.read_csv(datafile)
olivine.loc[olivine["name"] == 'kiki', "color"] = "darkmagenta"
olivine.loc[olivine["name"] == 'SC1-7', "color"] = '#ff7f0e'
olivine.loc[olivine["name"] == 'SC1-2', "color"] = '#2ca02c'

pp = dlib.pp
pv = dlib.pv
pnav = dlib.pnav_Ti

megan = olivine[olivine.Author == 'Newcombe et al.']
chen = olivine[olivine.Author == 'Chen et al.']
gaetani = olivine[olivine.Author == 'Gaetani et al.']
hauri = olivine[olivine.Author == 'Hauri']
portnyagin = olivine[olivine.Author == 'Portnyagin et al.']

kiki_data = olivine[olivine.name == 'kiki']
kiki_data = kiki_data[kiki_data.maxmin == 'no']
kiki_bulk = kiki_data[kiki_data.mechanism == 'bulk']
kiki_bulk_a = kiki_bulk[kiki_bulk.orientation == 'a']
kiki_bulk_b = kiki_bulk[kiki_bulk.orientation == 'b']
kiki_bulk_c = kiki_bulk[kiki_bulk.orientation == 'c']

SC7_data = olivine[olivine.name == 'SC1-7']
SC7_data = SC7_data[SC7_data.maxmin == 'no']
SC7_bulk = SC7_data[SC7_data.mechanism == 'bulk']
SC7_bulk_a = SC7_bulk[SC7_bulk.orientation == 'a']
SC7_bulk_b = SC7_bulk[SC7_bulk.orientation == 'b']
SC7_bulk_c = SC7_bulk[SC7_bulk.orientation == 'c']

SC2_data = olivine[olivine.name == 'SC1-2']
SC2_data = SC2_data[SC2_data.hours == 68.]
SC2_data = SC2_data[SC2_data.maxmin == 'no']
SC2_bulk = SC2_data[SC2_data.mechanism == 'bulk']
SC2_bulk_a = SC2_bulk[SC2_bulk.orientation == 'a']
SC2_bulk_b = SC2_bulk[SC2_bulk.orientation == 'b']
SC2_bulk_c = SC2_bulk[SC2_bulk.orientation == 'c']

kiki_Ti = kiki_data[kiki_data.mechanism == '[Ti]']
kiki_Ti = kiki_Ti[kiki_Ti.maxmin == 'no']
kiki_Ti_a = kiki_Ti[kiki_Ti.orientation == 'a']
kiki_Ti_b = kiki_Ti[kiki_Ti.orientation == 'b']
kiki_Ti_c = kiki_Ti[kiki_Ti.orientation == 'c']

SC7_Ti = SC7_data[SC7_data.mechanism == '[Ti]']
SC7_Ti_a = SC7_Ti[SC7_Ti.orientation == 'a']
SC7_Ti_b = SC7_Ti[SC7_Ti.orientation == 'b']
SC7_Ti_c = SC7_Ti[SC7_Ti.orientation == 'c']

SC2_Ti = SC2_data[SC2_data.mechanism == '[Ti]']
SC2_Ti_a = SC2_Ti[SC2_Ti.orientation == 'a']
SC2_Ti_b = SC2_Ti[SC2_Ti.orientation == 'b']
SC2_Ti_c = SC2_Ti[SC2_Ti.orientation == 'c']

kiki_Si = kiki_data[kiki_data.mechanism == '[Si]']
kiki_Si = kiki_Si[kiki_Si.maxmin == 'no']
kiki_Si_a = kiki_Si[kiki_Si.orientation == 'a']
kiki_Si_b = kiki_Si[kiki_Si.orientation == 'b']
kiki_Si_c = kiki_Si[kiki_Si.orientation == 'c']

SC7_Si = SC7_data[SC7_data.mechanism == '[Si]']
SC7_Si_a = SC7_Si[SC7_Si.orientation == 'a']
SC7_Si_b = SC7_Si[SC7_Si.orientation == 'b']
SC7_Si_c = SC7_Si[SC7_Si.orientation == 'c']

SC2_Si = SC2_data[SC2_data.mechanism == '[Si]']
SC2_Si_a = SC2_Si[SC2_Si.orientation == 'a']
SC2_Si_b = SC2_Si[SC2_Si.orientation == 'b']
SC2_Si_c = SC2_Si[SC2_Si.orientation == 'c']

SC7_tri = SC7_data[SC7_data.mechanism == '[tri]']
SC7_tri_a = SC7_tri[SC7_tri.orientation == 'a']
SC7_tri_b = SC7_tri[SC7_tri.orientation == 'b']
SC7_tri_c = SC7_tri[SC7_tri.orientation == 'c']

SC7_Mg = SC7_data[SC7_data.mechanism == '[Mg]']
SC7_Mg_a = SC7_Mg[SC7_Mg.orientation == 'a']
SC7_Mg_b = SC7_Mg[SC7_Mg.orientation == 'b']
SC7_Mg_c = SC7_Mg[SC7_Mg.orientation == 'c']

kiki_tri = kiki_data[kiki_data.mechanism == '[tri]']
kiki_tri_a = kiki_tri[kiki_tri.orientation == 'a']
kiki_tri_b = kiki_tri[kiki_tri.orientation == 'b']
kiki_tri_c = kiki_tri[kiki_tri.orientation == 'c']
#%%
fig = plt.figure()
fig.set_size_inches(6.5, 5)

xstart = 0.1
ypstart = 0.1
wgap = 0.18
width = 0.85
height = 0.8
hgap = 0.07
ax1 = fig.add_axes([xstart, ypstart, width, height])
ax1.set_xlim(6, 10)
ax1.set_ylim(-16, -8)


def plotline(mech, orient, ax, style={'color':'k'}):
    """
    Take diffusivity, e.g., pp, and index representing orientation
    Plot best-fit line only from min to max of actual measurements
    on axis ax using style dictionary
    """
    min_celsius = min(mech.celsius[orient])
    max_celsius = max(mech.celsius[orient])    
    celsius = np.array([min_celsius, max_celsius])
    kelvin = celsius + 273.15
    x = 1e4/kelvin    
    try:
        D0 = mech.D0_m2s[orient].n
    except AttributeError:
        D0 = mech.D0_m2s[orient]   
    try:
        Ea = mech.activation_energy_kJmol[orient].n
    except AttributeError:
        Ea = mech.activation_energy_kJmol[orient]

    D = D0 * np.exp(-Ea / (GAS_CONSTANT*kelvin))
    y = np.log10(D)
    ax.plot(x, y, **style)
    
celsius_labels = np.array([800, 1000, 1200])
ax1.set_xlabel('1e4 / Temperature (K)')
ax1.set_ylabel('log$_{10}$ Diffusivity (m$^2$/s)')
ax_celsius = ax1.twiny()
ax_celsius.set_xlim(ax1.get_xlim())
parasite_tick_locations = 1e4/(celsius_labels + 273.15)
ax_celsius.set_xticks(parasite_tick_locations)
ax_celsius.set_xticklabels(celsius_labels)
ax_celsius.set_xlabel("Temperature ($\degree$C)")

pp.celsius[3] = pp.celsius[0]
pp.activation_energy_kJmol[3] = 140.
pp.D0_m2s[3] = 0.0000027

### fits
my_data = dlib.Diffusivities(celsius=[[800, 1000, 1200],
                                        [800, 1000], 
                                        [800, 1000], []],
                               log10D=[[-11.6, -10.9, -10], 
                                       [-13.2, -12.2], 
                                       [-12.9, -11.9], []])
my_data.activation_energy_kJmol = [130, 130, 130, 0]
my_data.D0_m2s = [0.000004, 0.000000135, 0.000000275, 0]
plotline(my_data, 0, ax1, style={'color':'red', 'linewidth':6, 'alpha':0.5})
plotline(my_data, 1, ax1, style={'color':'red', 'linewidth':6, 'alpha':0.5})
plotline(my_data, 2, ax1, style={'color':'red', 'linewidth':6, 'alpha':0.5})

plotline(pp, 0, ax1, style={'color':'grey', 'linewidth':2})
plotline(pp, 1, ax1, style={'color':'grey', 'linewidth':2})
plotline(pp, 2, ax1, style={'color':'grey', 'linewidth':2})

plotline(pv, 0, ax1, style={'color':'grey', 'linewidth':2, 'linestyle':'--',
                            'alpha':0.75})
plotline(pv, 1, ax1, style={'color':'grey', 'linewidth':2, 'linestyle':'--', 
                            'alpha':0.75})
plotline(pv, 2, ax1, style={'color':'grey', 'linewidth':2, 'linestyle':'--', 
                            'alpha':0.75})

for pnav in [dlib.pnav_Mg, dlib.pnav_Si, dlib.pnav_Ti]:
    x = 1e4 / (np.array(pnav.celsius[3]) + 273.15)
    y = pnav.log10D[3]
    p = np.polyfit(x, y, 1)
    xplot = [min(x), max(x)]
    yplot = np.polyval(p, xplot)
    ax1.plot(xplot, yplot, ':', color='grey')

ax1data = [
           SC2_bulk_a,
           SC2_bulk_b,
           SC2_bulk_c,

           kiki_bulk_a,
           kiki_bulk_b,
           kiki_bulk_c,

           megan,
           chen,
           gaetani,
           portnyagin,
           hauri
           ]

color2 = '#2ca02c'
ax1styles = [
             {'color': '#2ca02c', 'linestyle':'none', 'marker':'o', 
              'label':'SC1-2 bulk || a', 'markerfacecolor': 'none', 
              'markersize':6},
              {'color':'#2ca02c', 'linestyle':'none', 'marker':'x',
              'markerfacecolor': color2, 'label':'SC1-2 bulk || b',
              'markersize':4},
             {'color': '#2ca02c', 'linestyle':'none', 'marker':'s',
              'markerfacecolor':color2, 'label':'SC1-2 bulk || c',
              'markersize':4},
             {'color': 'darkmagenta', 'linestyle':'none', 'marker':'o',
              'label':'kiki bulk || a', 'markerfacecolor':'none',
              'markersize':6},
               {'color': 'darkmagenta', 'linestyle':'none', 'marker':'x',
              'markerfacecolor':'none', 'label':'kiki bulk || b',
              'markersize':4},
              {'color':'darkmagenta', 'linestyle':'none', 'marker':'s',
              'markerfacecolor': 'darkmagenta', 'label':'SC1-2 bulk || c',
              'markersize':4}, 
             {'color': 'blue', 'linestyle':'none', 'marker':'*',
              'markerfacecolor':'none',
              'markersize':10},
             {'color': 'grey', 'linestyle':'none', 'marker':'^',
              'label':'Chen et al. 2011', 'markerfacecolor':'none',
              'markersize':6},
             {'color': 'grey', 'linestyle':'none', 'marker':'^',
              'label':'Gaetani et al. 2012', 'markerfacecolor':'none',
              'markersize':6},
             {'color': 'grey', 'linestyle':'none', 'marker':'^',
              'label':'Portnyagin et al. 2008', 'markerfacecolor':'none',
              'markersize':6},
             {'color': 'grey', 'linestyle':'none', 'marker':'^',
              'label':'Hauri 2002', 'markerfacecolor':'none',
              'markersize':6},
             ]

for data, style in zip(ax1data, ax1styles):
    x = 1e4 / (data.celsius + 273.15)
    y = data.log10D
    ax1.plot(x, y, **style)

xtxt = 9.38
ax1.text(xtxt, -11, 'PP || a')
ax1.text(xtxt, -11.7, 'SC1-2 || a', color=color2)
ax1.text(xtxt, -12.6, 'PP || b')
ax1.text(xtxt, -12.3, 'PP || c')
ax1.text(xtxt, -12.95, 'SC1-2 || c', color=color2)
ax1.text(xtxt, -13.3, 'SC1-2 || b', color=color2)

xtxt = 7.5
ax1.text(xtxt, -11., 'Kiki || a', color='darkmagenta')
ax1.text(xtxt+0.25, -11.8, 'Kiki || c', color='darkmagenta')
ax1.text(xtxt, -12.25, 'Kiki || b', color='darkmagenta')

ax1.text(6.3, -10.3, 'Kilauea Iki\ndehydrating || a', color='blue')
ax1.text(6.5, -11.36, 'unoriented\nestimates', color='grey')

ax1.text(7.05, -11.1, 'PV || c', rotation=0)
ax1.text(6.8, -12.1, 'PV || a and b')
ax1.text(7, -13.6, '[Si]')
ax1.text(9, -14, '[Mg]')
ax1.text(8.8, -14.5, '[Ti]')
ax1.text(7.4, -10.3, 'olivine dehydrating during ascent', color='red',
            rotation=-13)

col_labels=['E$_a$ (kJ/mol)','D$_0$ (m$^2$/s)']
row_labels=['|| a','|| b','|| c']
table_vals=[[my_data.activation_energy_kJmol[0], my_data.D0_m2s[0]],
            [my_data.activation_energy_kJmol[1], my_data.D0_m2s[1]],
            [my_data.activation_energy_kJmol[2], my_data.D0_m2s[2]]]
the_table = plt.table(cellText=table_vals,
                      colWidths = [0.12]*3,
                      rowLabels=row_labels,
                      colLabels=col_labels,
                      loc=3,
                      bbox=[0.05, 0.02, 0.25, 0.2])
plt.text(6.05, -14.15, 'Arrhenius laws for H\nin natural dehydrating olivine',
         size=8, color='red')

fig.savefig(file, dpi=200, format='jpg')
