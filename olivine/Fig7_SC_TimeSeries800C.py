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

#%%
fig = plt.figure()
fig.set_size_inches(6.5, 3)

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
           SC2_Si_c
           ]

colorTi = 'olivedrab'
colorSi = 'limegreen'
colora =  '#2ca02c'
colorb = 'limegreen'
colorc = 'olivedrab'
ax1styles = [
             {'color': colora, 'linestyle':'-', 'marker':'o', 
              'label':'SC1-2 bulk || a', 'markerfacecolor':'none', 
              'markersize':6, 'linewidth': 2},
             {'color': colora, 'linestyle':'-', 'marker':'p',
              'label':'SC1-2 bulk || b',
              'markersize':4, 'linewidth': 1},
             {'color': colora, 'linestyle':'--', 'marker':'s',
              'markerfacecolor':'none', 'label':'SC1-2 bulk || c',
              'markersize':4, 'linewidth': 1},
              
             {'color': colora, 'linestyle':'-', 'marker':'+', 
              'label':'SC1-2 [Ti] || a', 'markerfacecolor':'none', 
              'markersize':4, 'linewidth': 2},   
             {'color': colora, 'linestyle':'-', 'marker':'+', 
              'label':'SC1-2 [Ti] || a', 'markerfacecolor':'none', 
              'markersize':4, 'linewidth': 1}, 
             {'color': colora, 'linestyle':'--', 'marker':'+', 
              'label':'SC1-2 [Ti] || a', 'markerfacecolor':'none', 
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
ax1.text(xtext, -10.85, 'pp || a', ha='right')

y = [dlib.pp.whatIsD(800, printout=False)[1]] * 2
ax1.plot(x, y, '-', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -12.5, 'pp || b', ha='right')

y = [dlib.pp.whatIsD(800, printout=False)[2]] * 2
ax1.plot(x, y, '-', color='grey', linewidth=2, alpha=0.5)
ax1.text(xtext, -12.2, 'pp || c', ha='right')


for data, style in zip(ax1data, ax1styles):
    x = data.hours
    y = data.log10D
    ax1.plot(x, y, **style)

ax1.annotate('[Ti] || a', xy=(37, -11.25), xytext=(29, -11.6), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))
ax1.annotate('bulk || a', xy=(39, -11.45), xytext=(29, -11.85), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))
ax1.annotate('[Si] || a', xy=(39, -12.1), xytext=(29, -12.1), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))

ax1.annotate('[Ti] || c', xy=(6.3, -12.25), xytext=(8, -11.85), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))
ax1.annotate('bulk || c', xy=(7.8, -12.55), xytext=(8, -12.2), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))

ax1.annotate('[Ti] || b', xy=(7.8, -12.56), xytext=(1, -13.1), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))
ax1.annotate('bulk || b', xy=(7.8, -12.88), xytext=(1, -13.45), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))

ax1.annotate('[Si] || c', xy=(19, -13.7), xytext=(11.4, -13.7), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))
ax1.annotate('[Si] || b', xy=(19, -14), xytext=(11.4, -14), 
            arrowprops=dict(facecolor='k', arrowstyle='->'))

ax1.text(xtext, -14.4, 'SC1-2\ndehydration\n800$\degree$C, NNO-2.6', 
         ha='right')
#legend = ax1.legend(loc=2, ncol=4, shadow=True)
#legend.get_frame().set_alpha(1)
#legend.get_frame().set_facecolor('w')
#ax1.set_zorder(1)

#ax1.text(8.2, -11.5, 'pp || c')
#ax1.text(8.2, -12.4, 'pv || c')
#ax1.text(7.2, -12.1, 'pv || a')
#ax1.text(7, -14, '[Si]')
#ax1.text(9, -14, '[Mg]')
#ax1.text(8.8, -14.5, '[Ti]')
#ax1.text(9.425, -11.4, 'D$_{bulk}$, D$_{[Ti]}$\ndecrease', color='#2ca02c')
#ax1.text(9.425, -12.5, 'D$_{[Si]}$\nincreases', color='#2ca02c')
#ax1.text(9.22, -11.9, 'D$_{[tri]}$\ndecreases', color='darkmagenta', ha='right')

fig.savefig(file, dpi=200, format='jpg')
