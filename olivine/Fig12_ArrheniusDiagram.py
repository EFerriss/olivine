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
from matplotlib.patches import Ellipse

matplotlib.rcParams.update({'font.size': 8})

GAS_CONSTANT = 0.00831 # kJ/mol K

file = os.path.join(olivine.__path__[0], 'Fig12_ArrheniusDiagram.tif')

# get the data from file in pynams
datafile = os.path.join(pynams.__path__[0], 'diffusion', 'literaturevalues.csv')
olivine = pd.read_csv(datafile)
olivine.loc[olivine["name"] == 'IEFERJAIC', "color"] = "darkmagenta"
olivine.loc[olivine["name"] == 'SC1-7', "color"] = '#ff7f0e'
olivine.loc[olivine["name"] == 'SC1-2', "color"] = '#2ca02c'

pp = dlib.pp
pv = dlib.pv
pnav = dlib.pnav_Ti

megan = olivine[olivine.name == 'IEMN1KI02']
chen = olivine[olivine.Author == 'Chen et al.']
gaetani = olivine[olivine.Author == 'Gaetani et al.']
hauri = olivine[olivine.Author == 'Hauri']
portnyagin = olivine[olivine.Author == 'Portnyagin et al.']
novella = olivine[olivine.Author == 'Novella et al.']

kiki_data = olivine[olivine.name == 'IEFERJAIC']
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

novella_a = novella[novella.orientation == 'a']
novella_b = novella[novella.orientation == 'b']
novella_c = novella[novella.orientation == 'c']

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
ax1.set_xlim(6, 10.5)
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

novellaD = dlib.Diffusivities(celsius=[[750, 800, 900]]*4,
                              log10D=[novella_a.log10D,
                                      novella_b.log10D,
                                      novella_c.log10D,
                                      []])
novellaD.activation_energy_kJmol = [229, 172, 188]
novellaD.D0_m2s = [10**-0.7, 10**-5, 10**-3.5]

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

style_novella = {'color':'blue', 'linewidth':1, 'linestyle':'-', 'alpha':0.5}
plotline(novellaD, 0, ax1, style=style_novella)
plotline(novellaD, 1, ax1, style=style_novella)
plotline(novellaD, 2, ax1, style=style_novella)
    
# ellipse around unoriented estimates
unoriented_data = Ellipse(xy=(6.7, -11), width=1, height=1.2, angle=20, 
                          color='grey', alpha=0.1)
ax1.add_artist(unoriented_data)


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
#           chen,
#           gaetani,
#           portnyagin,
           hauri,
           
#           novella_a,
#           novella_b,
#           novella_c
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
             {'color': 'blue', 'linestyle':'none', 'marker':'o',
              'markerfacecolor':'none',
              'markersize':6},
              
#             {'color': 'grey', 'linestyle':'none', 'marker':'^',
#              'label':'Chen et al. 2011', 'markerfacecolor':'none',
#              'markersize':6},
#             {'color': 'grey', 'linestyle':'none', 'marker':'^',
#              'label':'Gaetani et al. 2012', 'markerfacecolor':'none',
#              'markersize':6},
#             {'color': 'grey', 'linestyle':'none', 'marker':'^',
#              'label':'Portnyagin et al. 2008', 'markerfacecolor':'none',
#              'markersize':6},
             {'color': 'grey', 'linestyle':'none', 'marker':'^',
              'label':'Hauri 2002', 'markerfacecolor':'none',
              'markersize':6},
              
#             {'color': 'k', 'linestyle':'none', 'marker':'o',
#              'label':'Novella et al. 2017 || a', 'markerfacecolor':'none',
#              'markersize':6},
#             {'color': 'k', 'linestyle':'none', 'marker':'+',
#              'label':'Novella et al. 2017 || b', 'markerfacecolor':'none',
#              'markersize':6},
#             {'color': 'k', 'linestyle':'none', 'marker':'s',
#              'label':'Novella et al. 2017 || c', 'markerfacecolor':'none',
#              'markersize':6},
             ]

for data, style in zip(ax1data, ax1styles):
    x = 1e4 / (data.celsius + 273.15)
    y = data.log10D
    ax1.plot(x, y, **style)

xtxt = 9.36
#ax1.text(xtxt, -11, 'redox || a', color='grey')
ax1.text(xtxt, -11.65, 'SC1-2 || a', color=color2)
#ax1.text(xtxt, -12.67, 'redox || b', color='grey')
#ax1.text(xtxt, -12.25, 'redox || c', color='grey')
ax1.text(xtxt, -12.95, 'SC1-2 || c', color=color2)
ax1.text(xtxt, -13.4, 'SC1-2 || b', color=color2)

xtxt = 7.475
ax1.text(xtxt, -11., 'Kiki || a', color='darkmagenta')
ax1.text(xtxt+0.25, -11.8, 'Kiki || c', color='darkmagenta')
ax1.text(xtxt, -12.25, 'Kiki || b', color='darkmagenta')

xtxt = 9.85
ax1.text(xtxt, -12.47, 'self-D || a', color='blue', alpha=0.5)
ax1.text(xtxt, -13.9, 'self-D || b', color='blue', alpha=0.5)
ax1.text(xtxt, -13.15, 'self-D || c', color='blue', alpha=0.5)

ax1.text(6.25, -10.45, 'Kilauea Iki\ndehydrating || a', color='blue')
ax1.text(6.7, -11, 'unoriented\nestimates', color='grey', 
         va='center', ha='center')

ax1.text(7.05, -11.1, 'PV || c', color='grey')
ax1.text(6.8, -12.1, 'PV || a and b', color='grey')
ax1.text(7, -13.6, '[Si]')
ax1.text(9, -14, '[Mg]')
ax1.text(8.8, -14.5, '[Ti]')
ax1.text(6.8, -9.9, 'olivine dehydrating during ascent', color='red',
            rotation=-15.3)

xtxt = 8.8
ax1.text(xtxt, -10.45, 'redox || a', color='grey', rotation = -15)
ax1.text(xtxt, -12.35, 'redox || b', color='grey', rotation = -20)
ax1.text(xtxt, -11.9, 'redox || c', color='grey', rotation = -10)


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

fig.savefig(file, dpi=300, format='tif')
