# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:09:58 2017

@author: Ferriss
"""
import matplotlib.pyplot as plt
from pynams import dlib
from olivine import thisfolder

#%% the data

# SC1-2 dehydration
SC_x = [1, 3, 7, 13, 19, 43, 68]
SC_y = [-11.6, -10.7, -12.7, -11.3, -11.4, -11.9, -11.9]
SC_y_err = [1.5, 0.2, 2.1, 0.2, 0.1, 0.2, 0.2]
SC_Ti_y = [-11.8, -10.7, -11, -11., -11.1, -11.4, -11.5]
SC_Ti_y_err = [1.8, 0.2, 0.2, 0.1, 0.1, 0., 0.1]
SC_Si_y = [-12., -12.6, -12.5, -12.5, -12.5, -12., -11.8]
SC_Si_y_err = [0., 0., 0., 0., 0, 0., 0]

# SC1-7 hydration 
SC7_x = [7]
SC7_y = [-13.1]
SC7_y_err = [2.2]
SC7_Si_y = [-13.5]
SC7_Si_y_err = [21.]
SC7_Ti_y = [-13.3]
SC7_Ti_y_err = [5.9]
SC7_tri_y = [-13]
SC7_tri_y_err = [-2.1]
SC7_Mg_y = [-12.7]
SC7_Mg_y_err = [1.1]

# expected diffusivities
fast800 = dlib.KM98_fast.whatIsD(800, printout=False)
fast1000 = dlib.KM98_fast.whatIsD(1000, printout=False)
slow800 = dlib.KM98_slow.whatIsD(800, printout=False)
slow1000 = dlib.KM98_slow.whatIsD(1000, printout=False)
pnavTi1000 = dlib.pnav_Ti.whatIsD(1000, printout=False)[3]
pnavTi800 = dlib.pnav_Ti.whatIsD(800, printout=False)[3]
pnavSi800 = dlib.pnav_Si.whatIsD(800, printout=False)[3]
pnavSi1000 = dlib.pnav_Si.whatIsD(1000, printout=False)[3]
pnavMg800 = dlib.pnav_Mg.whatIsD(800, printout=False)[3]
pnavMg1000 = dlib.pnav_Mg.whatIsD(1000, printout=False)[3]

fig = plt.figure()
fig.set_size_inches(6.5, 8)
xstart = 0.1
ystart = 0.075
width = 0.65
height = 0.4
hgap = 0.1
ax = fig.add_axes([xstart, ystart+height+hgap, width, height])
ax.set_xlabel('time (hours)')
ax.set_ylabel('log$_{10}$ diffusivity || a in m$^2$/s')
ax.set_xlim(0, 70)
ax.set_ylim(-20, -9)
ax.text(68, -10, '800$\degree$C, D || [100]', fontsize=14, ha='right')

ax2 = fig.add_axes([xstart, ystart, width, height])
ax2.set_xlim(ax.get_xlim())
ax2.set_ylim(-16, -10)
ax2.set_xlabel('time (hours)')
ax2.set_ylabel('log$_{10}$ diffusivity || c in m$^2$/s')
ax2.text(68, -10.5, '1000$\degree$C, D || [001]', fontsize=14, ha='right')

pnavcolor = 'k'
SC_style = {'color': '#2ca02c', 'marker':'o', 'markersize':20,
            'linewidth':2, 'alpha':1, 'linestyle':'none',
            'markerfacecolor':'none',
            'label':'bulk H, SC1-2'}
SC_Ti_style = {'color': '#2ca02c', 'marker':'x', 'markersize':15,
               'label':'[Ti] in SC1-2', 'linewidth':2, 
                'alpha':1, 'linestyle':'none'}
SC_Si_style = {'color': '#2ca02c', 'marker':'s', 'markersize':8,
                'markerfacecolor':'none', 'linestyle':'none',
                'linewidth':1,
               'label':'[Si] in SC1-2'}
Mg_style = {'marker':'p', 'markersize':12, 'markerfacecolor':'none', 
            'linestyle':'none', 'linewidth':3}
tri_style = {'marker':'^', 'markersize':10, 'markerfacecolor':'none', 
            'linestyle':'none', 'linewidth':1}

SC7_style = SC_style.copy()
SC7_Ti_style = SC_Ti_style.copy()
SC7_Si_style = SC_Si_style.copy()
SC7_Mg_style = Mg_style.copy()
SC7_tri_style = tri_style.copy()
SC7_style['color'] = '#ff7f0e'
SC7_Ti_style['color'] = SC7_style['color']
SC7_Si_style['color'] = SC7_style['color']
SC7_Mg_style['color'] = SC7_style['color']
SC7_tri_style['color'] = SC7_style['color']
SC7_style['label'] = 'bulk H, SC1-7'
SC7_Ti_style['label'] = '[Ti] in SC1-7'
SC7_Si_style['label'] = '[Si] in SC1-7'
SC7_Mg_style['label'] = '[Mg] in SC1-7'
SC7_tri_style['label'] = '[tri] in SC1-7'

ax.errorbar(SC_x, SC_y, yerr=SC_y_err, **SC_style)
ax.errorbar(SC_x, SC_Ti_y, yerr=SC_Ti_y_err, **SC_Ti_style)
ax.errorbar(SC_x, SC_Si_y, yerr=SC_Si_y_err, **SC_Si_style)
ax2.errorbar(SC7_x, SC7_y, yerr=SC7_y_err, **SC7_style)
ax2.errorbar(SC7_x, SC7_Ti_y, yerr=SC7_Ti_y_err, **SC7_Ti_style)
ax2.errorbar(SC7_x, SC7_Mg_y, yerr=SC7_Mg_y_err, **SC7_Mg_style)
ax2.errorbar(SC7_x, SC7_Si_y, yerr=SC7_Si_y_err, **SC7_Si_style)
ax2.errorbar(SC7_x, SC7_tri_y, yerr=SC7_tri_y_err, **SC7_tri_style)

ax.plot(ax.get_xlim(), [fast800[0], fast800[0]], 
        label='p.p.', color='k')
ax.plot(ax.get_xlim(), [slow800[0], slow800[0]], 
        label='p.v.', color='k', linewidth=5)
ax.plot(ax.get_xlim(), [pnavMg800, pnavMg800], linestyle='-.',
        label='[Mg]$_{Fo}$', color=pnavcolor, linewidth=2)
ax.plot(ax.get_xlim(), [pnavTi800, pnavTi800], linestyle='--',
        label='[Ti]$_{Fo}$', color=pnavcolor, linewidth=2)
ax.plot(ax.get_xlim(), [pnavSi800, pnavSi800], linestyle=':',
        label='[Si]$_{Fo}$', color=pnavcolor, linewidth=2)
ax.errorbar(-10, 0, yerr=0, **SC7_style)
ax.errorbar(-10, 0, yerr=0, **SC7_Ti_style)
ax.errorbar(-10, 0, yerr=0, **SC7_Mg_style)
ax.errorbar(-10, 0, yerr=0, **SC7_Si_style)
ax.errorbar(-10, 0, yerr=0, **SC7_tri_style)

ax.legend(loc=1, bbox_to_anchor=(1.375, 1))

ax2.plot(ax.get_xlim(), [fast1000[2], fast1000[2]], 
        label='p.p. at 1000$\degree$C', color='k')
ax2.plot(ax.get_xlim(), [slow1000[2], slow1000[2]], 
        label='p.v. at 1000$\degree$C', color='k', linewidth=5)
ax2.plot(ax.get_xlim(), [pnavMg1000, pnavMg1000], linestyle='-.',
        label='[Mg]$_{Fo}$ at 1000$\degree$C', color=pnavcolor, linewidth=2)
ax2.plot(ax.get_xlim(), [pnavTi1000, pnavTi1000], linestyle='--',
        label='[Ti]$_{Fo}$ at 1000$\degree$C', color=pnavcolor, linewidth=2)
ax2.plot(ax.get_xlim(), [pnavSi1000, pnavSi1000], linestyle=':',
        label='[Si]$_{Fo}$ at 1000$\degree$C', color=pnavcolor, linewidth=2)

fig.savefig(thisfolder+'\Fig5_D_over_time.jpg', 
            dpi=400, format='jpg')    