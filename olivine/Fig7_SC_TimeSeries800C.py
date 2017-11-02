# -*- coding: utf-8 -*-
"""
@author: Elizabeth Ferriss

Time series data at 800C
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

matplotlib.rcParams.update({'font.size': 8})

GAS_CONSTANT = 0.00831 # kJ/mol K

file = os.path.join(olivine.__path__[0], 'Fig7_SC_TimeSeries800C.jpg')

datafile = os.path.join(pynams.__path__[0], 'diffusion', 'literaturevalues.csv')
olivine = pd.read_csv(datafile)
olivine = olivine[olivine.celsius == 800]
olivine.loc[olivine["name"] == 'SC1-2', "color"] = '#2ca02c'

pp = dlib.pp
pv = dlib.pv
pnav = dlib.pnav_Ti

SC2_data_all = olivine[olivine.name == 'SC1-2']
SC2_data_all = SC2_data_all[SC2_data_all.maxmin == 'no']
SC2_data = SC2_data_all[SC2_data_all.hours != 17.4] # remove hydration data
SC2_bulk = SC2_data[SC2_data.mechanism == 'bulk']
SC2_bulk_a = SC2_bulk[SC2_bulk.orientation == 'a']
SC2_bulk_b = SC2_bulk[SC2_bulk.orientation == 'b']
SC2_bulk_c = SC2_bulk[SC2_bulk.orientation == 'c']

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
hydration_bulk_a = hydration_a[hydration_a.mechanism == 'bulk']
hydration_bulk_b = hydration_b[hydration_b.mechanism == 'bulk']
hydration_bulk_c = hydration_c[hydration_c.mechanism == 'bulk']

hydration_Ti_a = hydration_a[hydration_a.mechanism == '[Ti]']
hydration_Ti_b = hydration_b[hydration_b.mechanism == '[Ti]']
hydration_Ti_c = hydration_c[hydration_c.mechanism == '[Ti]']

kiki_data = olivine[olivine.name == 'kiki']
kiki_data = kiki_data[kiki_data.celsius == 800]

kiki_bulk = kiki_data[kiki_data.mechanism == 'bulk']
kiki_bulk_a = kiki_bulk[kiki_bulk.orientation == 'a']
kiki_bulk_b = kiki_bulk[kiki_bulk.orientation == 'b']
kiki_bulk_c = kiki_bulk[kiki_bulk.orientation == 'c']

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

xstart = 0.1
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
           SC2_bulk_a,
           SC2_bulk_b,
           SC2_bulk_c,
           
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
              'label':'SC1-2 bulk || a', 'markerfacecolor':'none', 
              'markersize':6, 'linewidth': 2},
             {'color': colora, 'linestyle':'-', 'marker':'o',
              'label':'SC1-2 bulk || b', 'markerfacecolor':'none',
              'markersize':6, 'linewidth': 1},
             {'color': colora, 'linestyle':'--', 'marker':'o',
              'markerfacecolor':'none', 'label':'SC1-2 bulk || c',
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
ax1.text(xtext, -10.85, 'PP || a', ha='right')

y = [dlib.pp.whatIsD(800, printout=False)[1]] * 2
ax1.plot(x, y, '-', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -12.5, 'PP || b', ha='right')

y = [dlib.pp.whatIsD(800, printout=False)[2]] * 2
ax1.plot(x, y, '-', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -12.2, 'PP || c', ha='right')

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
ax1.text(55, -11.525, 'bulk || a', rotation=-2)
ax1.text(55, -11.8, '[Si] || a', rotation=4)

ax1.text(35, -12.5, '[Ti] || c', rotation=-4)
ax1.text(35, -12.675, 'bulk || c', rotation=-7)
ax1.text(35, -13.3, '[Si] || c', rotation=12)

ax1.text(25, -12.75, '[Ti] || b', rotation=-7)
ax1.text(25, -12.95, 'bulk || b', rotation=-7)
ax1.text(25, -13.78, '[Si] || b', rotation=12)
#
#ax1.annotate('[Ti] || b', xy=(18.2, -12.65), xytext=(11.4, -13.1), 
#            arrowprops=dict(facecolor='k', arrowstyle='->'))
#ax1.annotate('bulk || b', xy=(18.9, -12.88), xytext=(11.4, -13.35), 
#            arrowprops=dict(facecolor='k', arrowstyle='->'))
#ax1.annotate('[Si] || b', xy=(22, -13.9), xytext=(11.4, -13.9), 
#            arrowprops=dict(facecolor='k', arrowstyle='->'))

#ax1.text(xtext, -14.4, 'SC1-2\ndehydration\n800$\degree$C, NNO-2.6', 
#         ha='right', color=colora)

fig.savefig(file, dpi=200, format='jpg')
