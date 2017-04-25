# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:25:29 2017

@author: Elizabeth

Figure showing hydration profiles in San Carlos olivines
"""
from __future__ import print_function
from olivine import thisfolder
from olivine.SanCarlos import SanCarlos_spectra as SC
from pynams import dlib
#from pynams.diffusion.models import diffusion3Dwb
import matplotlib.pyplot as plt

conversion_factor_area2water = 0.6 # see Table1_concentrations.py

wb7 = SC.wb_1000C_SC1_7
wb2 = SC.wb_800C_hyd
wb2.get_baselines()
wb7.get_baselines()
wb2.make_areas()
wb7.make_areas()

areas = []
for wb in [wb2, wb7]:
    for prof in wb.profiles:
        prof.areas = prof.areas * conversion_factor_area2water
        areas.append(max(prof.areas))
maxarea = max(areas)

#%%
slow = dlib.KM98_slow.whatIsD(celsius=1000, printout=False)

fig = plt.figure()
fig.set_size_inches(6.5, 2.7)

xstart = 0.1
ypstart = 0.17
wgap = 0.01
width = 0.27
height = 0.8
ax4 = fig.add_axes([xstart, ypstart, width, height])
ax5 = fig.add_axes([xstart+width+wgap, ypstart, width, height])
ax6 = fig.add_axes([xstart+2*width+2*wgap, ypstart, width, height])

style2 = {'color':'#2ca02c', 'marker':'o', 'linestyle': 'none'}
style7 = {'color':'#ff7f0e', 'marker':'s', 'linestyle': 'none'}
style7D = {'color':'#ff7f0e', 'linestyle': '-'}

wb2.plot_areas_3panels(axes3=[ax4, ax5, ax6], styles3=[style2]*3, 
                       centered=True, show_errorbars=False)
wb7.plot_areas_3panels(axes3=[ax4, ax5, ax6], styles3=[style7]*3, 
                       centered=True, show_errorbars=False)

for ax in [ax4, ax5, ax6]:
    ax.set_ylim(0, 60)

for ax in [ax5, ax6]:
    ax.axes.get_yaxis().set_ticks([])

ax4.set_xlabel('x (mm)')
ax5.set_xlabel('y (mm)')
ax6.set_xlabel('z (mm)')
ax4.set_ylabel('Hydrogen (ppm H$_2$O)')

xp = -0.7
xp2 = 0.8
yp = 55
fs = 16
fs2 = 10
ax4.text(ax4.get_xlim()[1]*xp, yp, 'A', ha='right', va='center', fontsize=fs)
ax5.text(ax5.get_xlim()[1]*xp, yp, 'B', ha='right', va='center', fontsize=fs)
ax6.text(ax6.get_xlim()[1]*xp, yp, 'C', ha='right', va='center', fontsize=fs)
ax4.text(ax4.get_xlim()[1]*xp2, yp, '  || [100]', 
         ha='right', va='center', fontsize=fs2)
ax5.text(ax5.get_xlim()[1]*xp2, yp, '  || [010]', 
         ha='right', va='center', fontsize=fs2)
ax6.text(ax6.get_xlim()[1]*xp2, yp, '  || [001]', 
         ha='right', va='center', fontsize=fs2)
ax5.set_title('')

#initial=14
#D3 = dlib.mix_olivine_mechanisms(celsius=1000, percent_slow=100)[0:3]
#print(D3)
#wb7.plot_diffusion(wholeblock_data=False, wholeblock_diffusion=True,
#                   centered=True, log10D_m2s=D3, fin=1, 
#                   init=initial/maxarea, axes3=[ax4, ax5, ax6],
#                   show_line_at_1=False, labelD=False)
#for ax in [ax4, ax5, ax6]:
#    ax.plot(ax.get_xlim(), [initial, initial], '--k')
#
str2 = 'SC1-2 hydrated\n17.5hr at 800$\degree$C, 1GPa'    
str7 = 'SC1-7 hydrated\n7hr at 1000$\degree$C, 1GPa'
#strD = 'expected profile for SC1-7\nbased on proton-vacancy\ndiffusivities at 1000$\degree$C'
#strm = ''.join(('$\\uparrow$ "metastable equilibrium"\nat ', str(initial), 
#                ' ppm H$_2$O used as initial\nfor proton-vacancy diffusion'))

ax4.text(-1200, 39, str7, color=style7['color'])
ax4.text(-1200, 3, str2, color=style2['color'])
#ax4.text(-1200, 19, strD, color='k', va='bottom')
#ax5.text(-500, initial, strm, va='top')

fig.savefig(thisfolder+'Fig4_hydration_profiles.jpg', dpi=200, format='jpg')