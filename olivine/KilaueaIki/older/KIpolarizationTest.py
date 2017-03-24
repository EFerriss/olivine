# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:16:58 2016

@author: Ferriss
"""

from pynams import pynams
import numpy as np
from pynams import styles
reload(pynams) 

FTIR_file_location = 'C:\\Users\\Ferriss\\Documents\\FTIR\\'

prof_fnames = ['FuegoOl14_core', 'Fuegool14a1'
               ]
prof_pos = np.arange(50, 50. + 100.*len(prof_fnames), 100.)
prof = pynams.Profile(profile_name = '',
                             fname_list = prof_fnames,
                             positions_microns = prof_pos,
                             set_thickness=True, folder=FTIR_file_location
                             )
prof.length_microns = max(prof_pos) + 50.

#%%
prof.plot_thicknesses()

#%%
prof.make_baselines(show_plot=True)

#%%
prof.plot_area_profile(calibration='Withers')

#%%
fig, ax = prof.spectra_list[0].plot_spectrum(size_inches=(6,6))
prof.spectra_list[-1].plot_spectrum(figaxis=ax, style=styles.style_2)
ax.legend(loc=2)

#%%
fig, ax = prof.spectra_list[0].plot_subtractbaseline(size_inches=(6,6))
prof.spectra_list[-1].plot_subtractbaseline(figaxis=ax, style=styles.style_2)
ax.legend(loc=1)
ax.set_ylim(0, 0.7)
