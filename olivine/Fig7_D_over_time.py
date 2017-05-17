# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:09:58 2017

@author: Ferriss
"""
import matplotlib.pyplot as plt
from pynams import dlib
from olivine import thisfolder

fast800 = dlib.KM98_fast.whatIsD(800, printout=False)
fast1000 = dlib.KM98_fast.whatIsD(1000, printout=False)
slow800 = dlib.KM98_slow.whatIsD(800, printout=False)
slow1000 = dlib.KM98_slow.whatIsD(1000, printout=False)
pnavTi1000 = dlib.pnav_Ti.whatIsD(1000, printout=False)[3]
pnavTi800 = dlib.pnav_Ti.whatIsD(800, printout=False)[3]
pnavSi800 = dlib.pnav_Si.whatIsD(800, printout=False)[3]

#%%
fig = plt.figure()
fig.set_size_inches(6.5, 4)
ax = fig.add_subplot(111)
ax.set_xlim(0, 70)
ax.set_xlabel('time (hours)')
ax.set_ylabel('log$_{10}$ diffusivity in m$^2$/s')

SC_style = {'color': '#2ca02c', 'marker':'o', 'markersize':12,
            'linewidth':8, 'alpha':0.5, 'linestyle':'none',
            'markerfacecolor':'none',
            'label':'bulk H, SC1-2 800C'}
SC_Ti_style = {'color': '#2ca02c', 'marker':'x', 'markersize':15,
               'label':'[Ti] in SC1-2 800C', 'linewidth':3, 
                'alpha':1, 'linestyle':'none'}
SC_Si_style = {'color': '#2ca02c', 'marker':'s', 'markersize':8,
                'markerfacecolor':'none', 'linestyle':'none',
                'linewidth':1,
               'label':'[Si] in SC1-2 800C'}

x = [1, 3, 7, 13, 19, 43, 68]
SC_x = x
SC_y = [-11.6, -10.7, -12.7, -11.3, -11.4, -11.9, -11.9]
SC_y_err = [1.5, 0.2, 2.1, 0.2, 0.1, 0.2, 0.2]

SC_Ti_x = x
SC_Ti_y = [-11.8, -10.7, -11, -11., -11.1, -11.4, -11.5]
SC_Ti_y_err = [1.8, 0.2, 0.2, 0.1, 0.1, 0., 0.1]

SC_Si_x = x
SC_Si_y = [-12., -12.6, -12.5, -12.5, -12.5, -12., -11.8]
SC_Si_y_err = [0., 0., 0., 0., 0, 0., 0]

ax.errorbar(SC_x, SC_y, yerr=SC_y_err, **SC_style)
ax.errorbar(SC_Ti_x, SC_Ti_y, yerr=SC_Ti_y_err, **SC_Ti_style)
ax.errorbar(SC_Si_x, SC_Si_y, yerr=SC_Si_y_err, **SC_Si_style)

ax.plot(ax.get_xlim(), [fast800[0], fast800[0]], 
        label='p.p. at 800$\degree$C', color='k')
ax.plot(ax.get_xlim(), [slow800[0], slow800[0]], 
        label='p.v. at 800$\degree$C', color='k', linewidth=5)
#ax.plot(ax.get_xlim(), [slow1000[0], slow1000[0]], 
#        label='p.v. at 1000$\degree$C', color='firebrick', linewidth=5,
#        alpha=0.5)
#ax.plot(ax.get_xlim(), [fast1000[0], fast1000[0]], 
#        label='p.p. at 1000$\degree$C', color='firebrick', alpha=0.5)
#ax.plot(ax.get_xlim(), [pnavTi1000, pnavTi1000], 
#        label='[Ti]$_{Fo}$ at 1000$\degree$C', color='orange')
pnavcolor = 'orange'
ax.plot(ax.get_xlim(), [pnavTi800, pnavTi800], linestyle='--',
        label='[Ti]$_{Fo}$ at 800$\degree$C', color=pnavcolor, linewidth=2)
ax.plot(ax.get_xlim(), [pnavSi800, pnavSi800], linestyle=':',
        label='[Si]$_{Fo}$ at 800$\degree$C', color=pnavcolor, linewidth=2)

#ax.set_ylim(-17, -9)
ax.legend(loc=1, bbox_to_anchor=(1.38, 1))

fig.savefig(thisfolder+'\Fig7_D_over_time.jpg', 
            dpi=400, format='jpg')    