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
import numpy as np

file = os.path.join(olivine.__path__[0], 'Fig8modified_check_linear.tif')
dfile = os.path.join(olivine.__path__[0], 'mydata.csv')

olivine = pd.read_csv(dfile)
olivine = olivine[olivine.Celsius == 800]
olivine.loc[olivine["name"] == 'SC1-2', "color"] = '#2ca02c'

pp = dlib.pp
pv = dlib.pv
pnav = dlib.pnav_Ti

SC2_data_all = olivine[olivine.name == 'SC1-2']
SC2_data_all = SC2_data_all[SC2_data_all.hours != 17.4] # remove hydration data

# measured data that aren't minimum vals
SC2_data = SC2_data_all[SC2_data_all.maximum_val == False]

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

#%%

fig = plt.figure()
fig.set_size_inches(6.5, 4)

x = 0.1
y = 0.19
w = 0.18
h = 0.31
wspace = 0.04
hspace = 0.12
ylim = 0.65
ylimSC = ylim
ytext = 0.6

ax1 = fig.add_axes([x, y+hspace+h, w, h])

