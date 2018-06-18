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
traverses = ['a-axis', 'c-axis']

for sample in samples:
    data = olivine[olivine.name == sample]
    
    for trav in traverses:
        travdata = data[data.traverse == trav]   
        if len(travdata) == 0:
            continue
        
        x = travdata.microns

        for element in elements:
            y = np.array(travdata[element])
            
            if np.isnan(y[0]):
                continue

            plt.plot(x, y, 'o')
            plt.title(' '.join((sample, trav, element)))
            plt.xlabel('microns')
            plt.ylabel('check supplement for units')
            plt.savefig(''.join((sample, '-', trav, '-', element, '.png')), 
                        dpi=200)
            plt.close()
        
    
    