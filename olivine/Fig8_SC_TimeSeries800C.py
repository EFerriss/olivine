# -*- coding: utf-8 -*-
"""
@author: Elizabeth Ferriss

Time series data at 800C
"""

from __future__ import print_function, division
import matplotlib.pyplot as plt
import os
import olivine
from pynams import dlib
import pandas as pd

GAS_CONSTANT = 0.00831 # kJ/mol K

file = os.path.join(olivine.__path__[0], 'Fig8_SC_TimeSeries800C.tif')
dfile = os.path.join(olivine.__path__[0], 'mydata.csv')

olivine = pd.read_csv(dfile)
olivine = olivine[olivine.Celsius == 800]
olivine.loc[olivine["name"] == 'SC1-2', "color"] = '#2ca02c'

pp = dlib.pp
pv = dlib.pv
pnav = dlib.pnav_Ti

SC2_data_all = olivine[olivine.name == 'SC1-2']
SC2_data_all = SC2_data_all[SC2_data_all.maximum_val == False]
SC2_data = SC2_data_all[SC2_data_all.hours != 17.4] # remove hydration data
SC2_total = SC2_data[SC2_data.mechanism == 'total']
SC2_total_a = SC2_total[SC2_total.orientation == 'a']
SC2_total_b = SC2_total[SC2_total.orientation == 'b']
SC2_total_c = SC2_total[SC2_total.orientation == 'c']

SC2_Ti = SC2_data[SC2_data.mechanism == '[Ti]']
SC2_Ti_a = SC2_Ti[SC2_Ti.orientation == 'a']
SC2_Ti_b = SC2_Ti[SC2_Ti.orientation == 'b']
SC2_Ti_c = SC2_Ti[SC2_Ti.orientation == 'c']

SC2_Si = SC2_data[SC2_data.mechanism == '[Si]']
SC2_Si_a = SC2_Si[SC2_Si.orientation == 'a']
SC2_Si_b = SC2_Si[SC2_Si.orientation == 'b']
SC2_Si_c = SC2_Si[SC2_Si.orientation == 'c']

hydration = SC2_data_all[SC2_data_all.hours == 17.4]
hydration_a = hydration[hydration.orientation == 'a']
hydration_b = hydration[hydration.orientation == 'b']
hydration_c = hydration[hydration.orientation == 'c']
hydration_total_a = hydration_a[hydration_a.mechanism == 'total']
hydration_total_b = hydration_b[hydration_b.mechanism == 'total']
hydration_total_c = hydration_c[hydration_c.mechanism == 'total']

hydration_Ti_a = hydration_a[hydration_a.mechanism == '[Ti]']
hydration_Ti_b = hydration_b[hydration_b.mechanism == '[Ti]']
hydration_Ti_c = hydration_c[hydration_c.mechanism == '[Ti]']

kiki_data = olivine[olivine.name == 'kiki']
kiki_data = kiki_data[kiki_data.Celsius == 800]

kiki_total = kiki_data[kiki_data.mechanism == 'total']
kiki_total_a = kiki_total[kiki_total.orientation == 'a']
kiki_total_b = kiki_total[kiki_total.orientation == 'b']
kiki_total_c = kiki_total[kiki_total.orientation == 'c']

kiki_Ti = kiki_data[kiki_data.mechanism == '[Ti]']
kiki_Ti_a = kiki_Ti[kiki_Ti.orientation == 'a']
kiki_Ti_b = kiki_Ti[kiki_Ti.orientation == 'b']
kiki_Ti_c = kiki_Ti[kiki_Ti.orientation == 'c']

kiki_Si = kiki_data[kiki_data.mechanism == '[Si]']
kiki_Si_a = kiki_Si[kiki_Si.orientation == 'a']
kiki_Si_b = kiki_Si[kiki_Si.orientation == 'b']
kiki_Si_c = kiki_Si[kiki_Si.orientation == 'c']

kiki_tri = kiki_data[kiki_data.mechanism == '[tri]']
kiki_tri_a = kiki_tri[kiki_tri.orientation == 'a']
kiki_tri_b = kiki_tri[kiki_tri.orientation == 'b']
kiki_tri_c = kiki_tri[kiki_tri.orientation == 'c']

#%%
fig = plt.figure()
fig.set_size_inches(6.5, 5)

xstart = 0.13
ypstart = 0.13
wgap = 0.18
width = 0.85
height = 0.8
hgap = 0.07
ax1 = fig.add_axes([xstart, ypstart, width, height])
ax1.set_xlim(0, 70)
ax1.set_ylim(-14.5, -10.5)
ax1.set_xlabel('time (hours)')
ax1.set_ylabel('log$_{10}$ Diffusivity in m$^2$/s')

ax1data = [
           SC2_total_a,
           SC2_total_b,
           SC2_total_c,
           
           SC2_Ti_a,
           SC2_Ti_b,
           SC2_Ti_c,
           
           SC2_Si_a,
           SC2_Si_b,
           SC2_Si_c,
           ]

colora =  '#2ca02c'
ax1styles = [
             {'color': colora, 'linestyle':'-', 'marker':'o', 
              'label':'SC1-2 total || a', 'markerfacecolor':'none', 
              'markersize':6, 'linewidth': 2},
             {'color': colora, 'linestyle':'-', 'marker':'o',
              'label':'SC1-2 total || b', 'markerfacecolor':'none',
              'markersize':6, 'linewidth': 1},
             {'color': colora, 'linestyle':'--', 'marker':'o',
              'markerfacecolor':'none', 'label':'SC1-2 total || c',
              'markersize':6, 'linewidth': 1},
              
             {'color': colora, 'linestyle':'-', 'marker':'p', 
              'label':'SC1-2 [Ti] || a', 'markerfacecolor':colora, 
              'markersize':4, 'linewidth': 2},   
             {'color': colora, 'linestyle':'-', 'marker':'p', 
              'label':'SC1-2 [Ti] || a', 'markerfacecolor':colora, 
              'markersize':4, 'linewidth': 1}, 
             {'color': colora, 'linestyle':'--', 'marker':'p', 
              'label':'SC1-2 [Ti] || a', 'markerfacecolor':colora, 
              'markersize':4, 'linewidth': 1}, 
              
             {'color': colora, 'linestyle':'-', 'marker':'x', 
              'label':'SC1-2 [Si] || a', 'markerfacecolor':'none', 
              'markersize':5, 'linewidth': 2},  
             {'color': colora, 'linestyle':'-', 'marker':'x', 
              'label':'SC1-2 [Si] || a', 'markerfacecolor':'none', 
              'markersize':5, 'linewidth': 1},  
             {'color': colora, 'linestyle':'--', 'marker':'x', 
              'label':'SC1-2 [Si] || a', 'markerfacecolor':'none', 
              'markersize':5, 'linewidth': 1},  
             ]

x = ax1.get_xlim()
xtext = 69
y = [dlib.pp.whatIsD(800, printout=False)[0]] * 2
ax1.plot(x, y, '-', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -10.85, 'redox || a', ha='right')

y = [dlib.pp.whatIsD(800, printout=False)[1]] * 2
ax1.plot(x, y, '-', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -12.5, 'redox || b', ha='right')

y = [dlib.pp.whatIsD(800, printout=False)[2]] * 2
ax1.plot(x, y, '-', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -12.2, 'redox || c', ha='right')

y = [dlib.pv.whatIsD(800, printout=False)[2]] * 2
ax1.plot(x, y, '--', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -13.9, 'PV || c', ha='right')

y = [dlib.pv.whatIsD(800, printout=False)[0]] * 2
ax1.plot(x, y, '--', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -14.35, 'PV || a and b', ha='right')


for data, style in zip(ax1data, ax1styles):
    x = data.hours
    y = data.log10D
    ax1.plot(x, y, **style)

ax1.text(55, -11.325, '[Ti] || a', rotation=-4)
ax1.text(55, -11.525, 'total || a', rotation=-2)
ax1.text(55, -11.8, '[Si] || a', rotation=4)

ax1.text(35, -12.5, '[Ti] || c', rotation=-4)
ax1.text(35, -12.675, 'total || c', rotation=-7)
ax1.text(35, -13.3, '[Si] || c', rotation=12)

ax1.text(25, -12.75, '[Ti] || b', rotation=-7)
ax1.text(25, -12.95, 'total || b', rotation=-7)
ax1.text(25, -13.78, '[Si] || b', rotation=12)

fig.savefig(file, dpi=300, format='tif')
