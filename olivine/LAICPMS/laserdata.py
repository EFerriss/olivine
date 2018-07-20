# -*- coding: utf-8 -*-
"""
Making figures to explore LA-ICP-MS data 
from Ferriss et al. GCA paper on H transport 
in olivine
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

olivine = pd.read_csv('laserdata.csv')
elements = olivine.columns[4:]

samples = ['Kiki', 'Kikin', 'SC1-2', 'SC1-7']
colors = ['purple', 'blue', 'green', 'orange']
traverses = ['a-axis', 'c-axis']

fig = plt.figure()

for i, element in enumerate(elements):
    for sample, color in zip(samples, colors):
        data = olivine[olivine.name == sample]   
        avg = data[element].mean()
        std = data[element].std()
        plt.plot(i, avg, '.', color=color)
        plt.errorbar(i, avg, std, color=color)
        
ax = plt.gca()
ax.set_xticks(range(len(elements)))
ax.set_xticklabels(elements)
ax.set_ylabel('check table for units')
ax.grid()

plt.savefig('zoomed_out.png', dpi=200)
ax.set_ylim(0, 175)
plt.savefig('zoomed_in.png', dpi=200)

#for sample in samples:
#    data = olivine[olivine.name == sample]
#    
#    for trav in traverses:
#        travdata = data[data.traverse == trav]   
#        if len(travdata) == 0:
#            continue
#        
#        x = travdata.microns
#
#        for element in elements:
#            y = np.array(travdata[element])
#            
#            if np.isnan(y[0]):
#                continue
#
#            plt.plot(x, y, 'o')
#            plt.title(' '.join((sample, trav, element)))
#            plt.xlabel('microns')
#            plt.ylabel('check supplement for units')
#            plt.savefig(''.join((element, '-', sample, '-', trav, '.png')), 
#                        dpi=200)
#            plt.close()
#        
#    
    