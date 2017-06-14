# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:09:58 2017

@author: Ferriss
"""
import matplotlib.pyplot as plt
from pynams import dlib
from olivine import thisfolder
import numpy as np

#%% the data

# SC1-2 dehydration
SC_x = [1, 3, 7, 13, 19, 43, 68]
SC_y = [-10.8, -10.8, -11.4, -11.2, -11.3, -11.7, -11.6]
SC_y_err = [0., 0., 0., 0.1, 0.1, 0.2, 0.2]
SC_y_err[0] = 0. # for clarity
SC_y_err[2] = 0. # for clarity
SC_Ti_y = [-11.8, -10.7, -11, -11., -11.1, -11.4, -11.5]
SC_Ti_y_err = [1.8, 0.2, 0.2, 0.1, 0.1, 0., 0.1]
SC_Ti_y_err[0] = 0. # for clarity
SC_Si_y = [-12.5, -12.5, -12.5, -12.5, -12.5, -12., -11.8] # changed idx 0, 1
SC_Si_y_err = [0., 0., 0., 0., 0, 0., 0]
#### manual updates for SC [Ti] that retain original error limits
SC_Ti_y_err_up = SC_Ti_y_err
SC_Ti_y_err_lo = SC_Ti_y_err
idxs = [0, 1]
replacements = [-10.8, -10.8]
for idx, replacement in zip(idxs, replacements):
    SC_Ti_y_err_up[idx] =  SC_Ti_y[idx] + SC_Ti_y_err_up[idx] - replacement
    SC_Ti_y_err_lo[idx] =  SC_Ti_y[idx] - SC_Ti_y_err_up[idx] - replacement
    SC_Ti_y_err = [SC_Ti_y_err_lo, SC_Ti_y_err_up]
    SC_Ti_y[idx] = replacement
# upper limits
SC_Si_uplims = np.zeros_like(SC_x)
SC_Si_uplims[[0, 1, 2, 3, 4]] = True
for idx in range(5):
    SC_Si_y_err[idx] = 0.4

# SC1-7 hydration 
slowc = dlib.KM98_slow.whatIsD(celsius=1000, printout=False)[2]
SC7_x = [7]
SC7_labels = ['bulk', '[Si]', '[Ti]', '[tri]', '[Mg]']
SC7_y = [-10.8, -11.5, -11.1, -10.8, -10.5]
SC7_y_err = [0]*len(SC7_y)

# Kilauea Iki
kiki_800_x = [1, 8]
kiki_800 = [-12.5, -12.5] # changed idx 1
kiki_800_err = [0., 0.] #[2.2, 1.7]
kiki_800_tri = [-10, -10.1]
kiki_800_tri_err = [0.1, 0.1]
kiki_800_Ti = [-12.5, -12.5]
kiki_800_Ti_err = [0.4, 0.]
kiki_800_Si = [-12.5, -12.5]
kiki_800_Si_err = [0., 0.4]
kiki_1000_x = [3, 6, 7, 8]
kiki_1000 = [-11.68, -11.68, -11.68, -11.68]
kiki_1000_tri = [-11.73, -11.73, -11.73, -11.73]
kiki_1000_Ti = [-11.73, -11.73, -11.70, -11.70]
kiki_1000_Si = [-11.66, -11.66, -11.66, -11.66]

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
fig.set_size_inches(6.5, 7)
xstart = 0.1
ystart = 0.075
width = 0.65
height = 0.4
hgap = 0.1
ax = fig.add_axes([xstart, ystart+height+hgap, width, height])
ax.set_xlabel('time (hours)')
ax.set_ylabel('log$_{10}$ diffusivity || a in m$^2$/s')
ax.set_xlim(0, 70)
ax.set_ylim(-16, -9.5)
ax.text(68, -10., '800$\degree$C, D || [100]', fontsize=14, ha='right')
ax.text(68, -10.7, 'p.p.', ha='right')
ax.text(68, -15.7, 'p.v.', ha='right')
ax.text(68, -14.2, '[Mg]$_{Fo}$', ha='right')
ax.text(68, -15.1, '[Ti]$_{Fo}$', ha='right')

ax2 = fig.add_axes([xstart, ystart, width, height])
ax2.set_xlim(0, 10)
ax2.set_ylim(-16, -9.5)
ax2.set_xlabel('time (hours)')
ax2.set_ylabel('log$_{10}$ diffusivity || c in m$^2$/s')
xt = 9.8
ax2.text(xt, -10., '1000$\degree$C, D || [001]', fontsize=14, ha='right')
ax2.text(xt, -10.95, 'p.p.', ha='right')
ax2.text(xt, -11.65, 'p.v.', ha='right')
ax2.text(xt, -12.6, '[Mg]$_{Fo}$', ha='right')
ax2.text(xt, -13.5, '[Ti]$_{Fo}$', ha='right')
ax2.text(xt, -15.5, '[Si]$_{Fo}$', ha='right')

pnavcolor = 'k'
SC_style = {'color': '#2ca02c', 'marker':'o', 'markersize':10,
            'linewidth':2, 'alpha':1, 'linestyle':'-',
            'markerfacecolor':'#2ca02c', 'markeredgecolor':'k',
            'label':'bulk H, SC1-2'}
SC_Ti_style = {'color': '#2ca02c', 'marker':'*', 'markersize':10,
               'label':'[Ti] in SC1-2', 'linewidth':1, 
                'alpha':0.8, 'linestyle':'--', 
                'markerfacecolor':'#2ca02c', 'markeredgecolor':'k',}
SC_Si_style = {'color': '#2ca02c', 'marker':'s', 'markersize':8,
               'markerfacecolor':'#2ca02c', 'markeredgecolor':'k',
                'alpha':0.8, 'linestyle':':', 'linewidth':1,
               'label':'[Si] in SC1-2'}
Mg_style = {'marker':'p', 'markersize':10, 
            'linestyle':'-.', 'linewidth':1, 'alpha':0.8,
            'markerfacecolor':'#ff7f0e', 'markeredgecolor':'k',}
tri_style = {'marker':'^', 'markersize':10, #'markerfacecolor':'none', 
            'linestyle':'none', 'linewidth':1, 'alpha':0.8,
            'markerfacecolor':'#ff7f0e', 'markeredgecolor':'k',}

SC7_style = SC_style.copy()
SC7_Ti_style = SC_Ti_style.copy()
SC7_Si_style = SC_Si_style.copy()
SC7_Mg_style = Mg_style.copy()
SC7_tri_style = tri_style.copy()
kiki_style = SC_style.copy()
kiki_Ti_style = SC_Ti_style.copy()
kiki_Si_style = SC_Si_style.copy()
kiki_Mg_style = Mg_style.copy()
kiki_tri_style = tri_style.copy()
kiki_style['color'] = 'darkmagenta'
kiki_style['markerfacecolor'] = 'darkmagenta'
SC7_style['color'] = '#ff7f0e'
SC7_style['markerfacecolor'] = '#ff7f0e'
SC7_Ti_style['markerfacecolor'] = SC7_style['markerfacecolor']
SC7_Si_style['markerfacecolor'] = SC7_style['markerfacecolor']
SC7_Ti_style['color'] = SC7_style['color']
SC7_Si_style['color'] = SC7_style['color']
SC7_Mg_style['color'] = SC7_style['color']
SC7_tri_style['color'] = SC7_style['color']
SC7_style['label'] = 'bulk H, SC1-7'
SC7_Ti_style['label'] = '[Ti] in SC1-7'
SC7_Si_style['label'] = '[Si] in SC1-7'
SC7_Mg_style['label'] = '[Mg] in SC1-7'
SC7_tri_style['label'] = '[tri] in SC1-7'
kiki_style['label'] = 'bulk H, Kiki'
kiki_style['alpha'] = 1
kiki_Ti_style['markerfacecolor'] = kiki_style['markerfacecolor']
kiki_Si_style['markerfacecolor'] = kiki_style['markerfacecolor']
kiki_tri_style['markerfacecolor'] = kiki_style['markerfacecolor']
kiki_Ti_style['color'] = kiki_style['color']
kiki_Si_style['color'] = kiki_style['color']
kiki_tri_style['color'] = kiki_style['color']
kiki_Ti_style['label'] = '[Ti] in Kiki'
kiki_Si_style['label'] = '[Si] in Kiki'
kiki_tri_style['label'] = '[tri] in Kiki'         
SC_hyd_style = SC_style.copy()
SC_Ti_hyd_style = SC_Ti_style.copy()
SC_hyd_style['label'] = 'SC1-2 hydr.\nbulk, [Ti]'
SC_hyd_style['linestyle'] = 'none'
SC_hyd_style['markersize'] = SC_style['markersize'] + 2
                        
ax.plot(17.4, fast800[0], **SC_hyd_style)

ax.errorbar(SC_x, SC_y, yerr=SC_y_err, **SC_style)
ax.errorbar(SC_x, SC_Ti_y, yerr=SC_Ti_y_err, **SC_Ti_style)
ax.errorbar(SC_x, SC_Si_y, yerr=SC_Si_y_err, uplims=SC_Si_uplims, **SC_Si_style)

ax.errorbar(kiki_800_x, kiki_800, yerr=kiki_800_err, **kiki_style)
ax.errorbar(kiki_800_x, kiki_800_Si, yerr=kiki_800_Si_err, uplims=True, **kiki_Si_style)
ax.errorbar(kiki_800_x, kiki_800_tri, yerr=kiki_800_tri_err, **kiki_tri_style)
ax.errorbar(kiki_800_x, kiki_800_Ti, yerr=kiki_800_Ti_err, uplims=True, **kiki_Ti_style)

ax2.errorbar(SC7_x, SC7_y[0], yerr=SC7_y_err[0], **SC7_style)
ax2.errorbar(SC7_x, SC7_y[1], yerr=SC7_y_err[1], **SC7_Si_style)
ax2.errorbar(SC7_x, SC7_y[2], yerr=SC7_y_err[2], **SC7_Ti_style)
ax2.errorbar(SC7_x, SC7_y[3], yerr=SC7_y_err[3], **SC7_tri_style)
ax2.errorbar(SC7_x, SC7_y[4], yerr=SC7_y_err[4], **SC7_Mg_style)

ax2.plot(kiki_1000_x, kiki_1000, **kiki_style)
ax2.plot(kiki_1000_x, kiki_1000_Si, **kiki_Si_style)
ax2.plot(kiki_1000_x, kiki_1000_tri, **kiki_tri_style)
ax2.plot(kiki_1000_x, kiki_1000_Ti, **kiki_Ti_style)

ax.plot(ax.get_xlim(), [fast800[0], fast800[0]], 
        label='p.p.', color='k')
ax.plot(ax.get_xlim(), [slow800[0], slow800[0]], 
        label='p.v.', color='k', linewidth=3)
ax.plot(ax.get_xlim(), [pnavMg800, pnavMg800], 
        linestyle=Mg_style['linestyle'],
        label='[Mg]$_{Fo}$', color=pnavcolor, linewidth=2)
ax.plot(ax.get_xlim(), [pnavTi800, pnavTi800], 
        linestyle=SC_Ti_style['linestyle'],
        label='[Ti]$_{Fo}$', color=pnavcolor, linewidth=2)
ax.plot(ax.get_xlim(), [pnavSi800, pnavSi800], 
        linestyle=SC_Si_style['linestyle'],
        label='[Si]$_{Fo}$', color=pnavcolor, linewidth=2)

ax2.plot(ax.get_xlim(), [fast1000[2], fast1000[2]], 
        label='p.p. at 1000$\degree$C', color='k')
ax2.plot(ax.get_xlim(), [slow1000[2], slow1000[2]], 
        label='p.v. at 1000$\degree$C', color='k', linewidth=3)
ax2.plot(ax.get_xlim(), [pnavMg1000, pnavMg1000], 
         linestyle=Mg_style['linestyle'],
         label='[Mg]$_{Fo}$ at 1000$\degree$C', color=pnavcolor, linewidth=2)
ax2.plot(ax.get_xlim(), [pnavTi1000, pnavTi1000], 
         linestyle=SC_Ti_style['linestyle'],
        label='[Ti]$_{Fo}$ at 1000$\degree$C', color=pnavcolor, linewidth=2)
ax2.plot(ax.get_xlim(), [pnavSi1000, pnavSi1000], 
         linestyle=SC_Si_style['linestyle'],
        label='[Si]$_{Fo}$ at 1000$\degree$C', color=pnavcolor, linewidth=2)

ax.errorbar(-10, 0, yerr=0, **SC7_style)
ax.errorbar(-10, 0, yerr=0, **SC7_Ti_style)
ax.errorbar(-10, 0, yerr=0, **SC7_Mg_style)
ax.errorbar(-10, 0, yerr=0, **SC7_Si_style)
ax.errorbar(-10, 0, yerr=0, **SC7_tri_style)
ax.legend(loc=1, bbox_to_anchor=(1.375, 1))

ax.text(2, -15.8, '$\downarrow$ to [Si]$_{Fo}$')

fig.savefig(thisfolder+'\Fig5_D_over_time.jpg', 
            dpi=400, format='jpg')    