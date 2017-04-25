# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:30:47 2017

@author: Elizabeth

Show schematics for olivine hydration in piston cylinder

Figure modified from pynams function pynams.experiments.pressure_design()
"""
from pynams.experiments import style_buffer, style_capsule, make_capsule_shape
from pynams.experiments import style_pressure_medium, style_MgO
from pynams.experiments import style_graphite, style_pyrophyllite
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
from olivine import thisfolder

fig = plt.figure()
fig.set_size_inches(3.5, 2.5)

xstart = 0.12
ypstart = 0.15
width = 0.25
wspace = 0.05
height = 0.75

# general setup
capsule_material = 'copper'
pressure_medium_material='BaCO$_3$'
sleeve_material='pyrophyllite'
buffer_material='sample, H$_2$O,\nNi, NiO,\nSan Carlos\nolivine and\nenstatite\n'
h_graphite_button=1.5
h_pressure_medium=33.35
h_graphite_cylinder=33.35
h_sleeve=11.5
h_sleeve_bottom=1.
h_capsule = 8.5
h_lid=2.4
h_MgO_base=10.5
h_MgO_wafer=1.5
h_MgO_top=10.4
od_pressure_medium=18.9
od_graphite_cylinder=11.5
id_graphite_cylinder=10.0
id_sleeve=8.7
id_capsule=5.95
d_graphite_button = od_pressure_medium
od_MgO_base = id_graphite_cylinder
od_sleeve = id_graphite_cylinder

for style in [style_graphite, style_MgO, style_capsule, style_buffer]:
    style['label'] = None
    
# SC1-2
ax = fig.add_axes([xstart, ypstart, width, height])
ax.set_xlim(0, od_pressure_medium)
ax.set_xlabel('SC1-2 (mm)')
ax.set_ylabel('(mm)')
h_guts = h_MgO_base + h_sleeve + h_MgO_wafer + h_MgO_top
highest_point = max(h_pressure_medium, h_graphite_cylinder, h_guts)
ax.set_ylim(0., h_graphite_button + highest_point + 2.)
plt.tick_params(axis='x', top='off')
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

th_gc = (od_graphite_cylinder - id_graphite_cylinder) / 2.
xgc = (od_pressure_medium - od_graphite_cylinder) / 2.
pressure_medium = patches.Rectangle((0., h_graphite_button), # (x,y)
                                    od_pressure_medium, # width
                                    h_pressure_medium, # height
                                    **style_pressure_medium)

graphite_button = patches.Rectangle((0., 0.), d_graphite_button,
                                    h_graphite_button, **style_graphite)

graphite_cylinder = patches.Rectangle((xgc, h_graphite_button), 
                         od_graphite_cylinder, h_graphite_cylinder, 
                         **style_graphite)

the_guts = patches.Rectangle((xgc + th_gc, h_graphite_button), 
                             id_graphite_cylinder,
                             h_graphite_cylinder, facecolor='w')
                         
MgO_base = patches.Rectangle((xgc+th_gc, h_graphite_button),
                             od_MgO_base, h_MgO_base, **style_MgO)

sleeve_path = make_capsule_shape(x=xgc + th_gc, 
                                 y=h_graphite_button + h_MgO_base,
                                 height=h_sleeve, 
                                 outerD=od_sleeve, 
                                 innerD=id_sleeve)
sleeve = patches.PathPatch(sleeve_path, **style_pyrophyllite)
th_sleeve = (od_sleeve - id_sleeve) / 2.

capsule_path = make_capsule_shape(x=xgc + th_gc + th_sleeve, 
               y=h_graphite_button + h_MgO_base + h_sleeve_bottom,
               height=h_capsule + h_lid/2., outerD=id_sleeve, innerD=id_capsule,
               shape='suaged')  
style_capsule['facecolor'] = 'orange'
capsule = patches.PathPatch(capsule_path, **style_capsule)

MgO_wafer = patches.Rectangle((xgc + th_gc, 
                               h_graphite_button + h_MgO_base + h_sleeve),
                               od_MgO_base, h_MgO_wafer, **style_MgO)

MgO_top = patches.Rectangle((xgc + th_gc, 
                h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer),
                od_MgO_base, h_MgO_top, **style_MgO)

thermocouple = patches.Rectangle((od_pressure_medium/2.-0.5, 
                h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer),
                1., h_MgO_top, facecolor='w')
ax.plot([od_pressure_medium/2-0.15, od_pressure_medium/2.-0.15],
        [h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer + h_MgO_top + 2.,
         h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer], 
         color='r', linewidth=1)
ax.plot([od_pressure_medium/2+0.15, od_pressure_medium/2.+0.15],
        [h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer + h_MgO_top + 2.,
         h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer], 
         color='b', linewidth=1)

th_capsule = (id_sleeve - id_capsule) / 2.
buffer_inside = patches.Rectangle((xgc + th_gc + th_sleeve + th_capsule,
                h_graphite_button + h_MgO_base + h_sleeve_bottom + th_capsule),
                id_capsule, h_capsule - th_capsule, **style_buffer)

th_flap = th_capsule / 2.
x = xgc + th_gc + th_sleeve + th_flap
ystart = h_graphite_button + h_MgO_base + h_sleeve_bottom + th_capsule
y = ystart + h_capsule - th_flap*2
th_lid = h_lid / 2.
th_capsule = (id_sleeve - id_capsule) / 2.
lid_verts = [(x + th_capsule - th_flap, y), 
             (x, y),
             (x, y + th_lid), 
             (x + id_sleeve - th_capsule, y + th_lid), 
             (x + id_sleeve - th_capsule, y), 
             (x + id_sleeve - th_capsule - th_flap, y), 
             (x + id_sleeve - th_capsule - th_flap, y - th_lid), 
             (x + th_capsule - th_flap, y - th_lid), 
             (0., 0.)]
lid_codes = [Path.MOVETO] + ([Path.LINETO] * 7) + [Path.CLOSEPOLY]
lid_path = Path(lid_verts, lid_codes)
lid = patches.PathPatch(lid_path, **style_capsule)

ax.add_patch(pressure_medium)
ax.add_patch(graphite_button)
ax.add_patch(graphite_cylinder)
ax.add_patch(the_guts)
ax.add_patch(MgO_base)
ax.add_patch(sleeve)
ax.add_patch(buffer_inside)
ax.add_patch(MgO_wafer)
ax.add_patch(MgO_top)
ax.add_patch(thermocouple)
ax.add_patch(capsule)
ax.add_patch(lid)
#ax.set_title('SC1-2')

### SC1-7 
for style in [style_graphite, style_MgO, style_capsule, style_buffer]:
    style['label'] = None

id_capsule=6.7
h_capsule = 10.
h_lid=1.
h_pressure_medium=32.0
h_graphite_cylinder=32.0
h_MgO_wafer=1.4
h_MgO_base = 9.6
h_MgO_top = 9.9

ax = fig.add_axes([xstart + width + wspace, ypstart, width, height])
ax.set_xlim(0, od_pressure_medium)
ax.set_xlabel('SC1-7 (mm)')
ax.set_ylim(0., h_graphite_button + highest_point + 2.)
plt.tick_params(axis='x', top='off')
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
labels = [item.get_text() for item in ax.get_yticklabels()]
empty_string_labels = ['']*len(labels)
ax.set_yticklabels(empty_string_labels)

th_gc = (od_graphite_cylinder - id_graphite_cylinder) / 2.
xgc = (od_pressure_medium - od_graphite_cylinder) / 2.
style_pressure_medium['label'] = pressure_medium_material
pressure_medium = patches.Rectangle((0, h_graphite_button), # (x,y)
                                    od_pressure_medium, # width
                                    h_pressure_medium, # height
                                    **style_pressure_medium)

graphite_button = patches.Rectangle((0., 0.), d_graphite_button,
                                    h_graphite_button, **style_graphite)

style_graphite['label'] = 'graphite'
graphite_cylinder = patches.Rectangle((xgc, h_graphite_button), 
                         od_graphite_cylinder, h_graphite_cylinder, 
                         **style_graphite)

the_guts = patches.Rectangle((xgc + th_gc, h_graphite_button), 
                             id_graphite_cylinder,
                             h_graphite_cylinder, facecolor='w')
                         
MgO_base = patches.Rectangle((xgc+th_gc, h_graphite_button),
                             od_MgO_base, h_MgO_base, **style_MgO)

style_pyrophyllite['label'] = 'pyrophyllite'
sleeve_path = make_capsule_shape(x=xgc + th_gc, 
                                 y=h_graphite_button + h_MgO_base,
                                 height=h_sleeve, 
                                 outerD=od_sleeve, 
                                 innerD=id_sleeve)
sleeve = patches.PathPatch(sleeve_path, **style_pyrophyllite)
th_sleeve = (od_sleeve - id_sleeve) / 2.

capsule_path = make_capsule_shape(x=xgc + th_gc + th_sleeve, 
               y=h_graphite_button + h_MgO_base + h_sleeve_bottom,
               height=h_capsule, outerD=id_sleeve, innerD=id_capsule)
capsule = patches.PathPatch(capsule_path, **style_capsule)
    
MgO_wafer = patches.Rectangle((xgc + th_gc, 
                               h_graphite_button + h_MgO_base + h_sleeve),
                               od_MgO_base, h_MgO_wafer, **style_MgO)

style_MgO['label'] = 'MgO'
MgO_top = patches.Rectangle((xgc + th_gc, 
                h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer),
                od_MgO_base, h_MgO_top, **style_MgO)

thermocouple = patches.Rectangle((od_pressure_medium/2.-0.5, 
                h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer),
                1., h_MgO_top, facecolor='w')
ax.plot([od_pressure_medium/2-0.15, od_pressure_medium/2.-0.15],
        [h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer + h_MgO_top + 2.,
         h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer], 
         color='r', linewidth=1)
ax.plot([od_pressure_medium/2+0.15, od_pressure_medium/2.+0.15],
        [h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer + h_MgO_top + 2.,
         h_graphite_button + h_MgO_base + h_sleeve + h_MgO_wafer], 
         color='b', linewidth=1)

th_capsule = (id_sleeve - id_capsule) / 2.
style_buffer['label'] = buffer_material
buffer_inside = patches.Rectangle((xgc + th_gc + th_sleeve + th_capsule,
                h_graphite_button + h_MgO_base + h_sleeve_bottom + th_capsule),
                id_capsule, h_capsule - th_capsule, **style_buffer)

x = xgc + th_gc + th_sleeve
y = h_graphite_button + h_MgO_base + h_sleeve_bottom + h_capsule
th_lid = h_lid / 2.
th_capsule = (id_sleeve - id_capsule) / 2.
lid_verts = [(x + th_capsule, y), 
             (x, y),
             (x, y + th_lid), 
             (x + id_sleeve, y + th_lid), 
             (x + id_sleeve, y), 
             (x + id_sleeve - th_capsule, y), 
             (x + id_sleeve - th_capsule, y - th_lid), 
             (x + th_capsule, y - th_lid), 
             (0., 0.)]
lid_codes = [Path.MOVETO] + ([Path.LINETO] * 7) + [Path.CLOSEPOLY]
lid_path = Path(lid_verts, lid_codes)
style_capsule['label'] = 'copper'
lid = patches.PathPatch(lid_path, **style_capsule)

ax.add_patch(pressure_medium)
ax.add_patch(graphite_button)
ax.add_patch(graphite_cylinder)
ax.add_patch(the_guts)
ax.add_patch(MgO_base)
ax.add_patch(sleeve)
ax.add_patch(buffer_inside)
ax.add_patch(MgO_wafer)
ax.add_patch(MgO_top)
ax.add_patch(thermocouple)
ax.add_patch(capsule)
#ax.set_title('SC1-7')
ax.add_patch(lid)

ax.legend(bbox_to_anchor=(0.95, 0.9), frameon=False)

print('finished')

fig.savefig(thisfolder+'Fig1_experiments.jpg', dpi=200, format='jpg')