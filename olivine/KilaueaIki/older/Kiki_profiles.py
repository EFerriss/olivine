#-*- coding: utf-8 -*-
"""
Created on Fri Dec 09 14:24:39 2016

@author: Ferriss

Make and save Kilauea Iki olivine baselines
"""

from __future__ import division, print_function
from olivine.KilaueaIki import Kiki_spectra as kiki
from matplotlib.backends.backend_pdf import PdfPages
from pynams import dlib, styles
import numpy as np

# diffusivities
slow = dlib.KM98_slow.whatIsD(1000, printout=False)[0:3]
fast = dlib.KM98_fast.whatIsD(1000, printout=False)[0:3]

wb_list = [kiki.wb_Kiki_init, kiki.wb_Kiki_1hr, kiki.wb_Kiki_8hr,
           kiki.wb_Kiki_1000C_3hr, kiki.wb_Kiki_1000C_6hr,
           kiki.wb_Kiki_1000C_7hr, kiki.wb_Kiki_ox]

thisfolder = kiki.thisfolder

for idx, wb in enumerate(wb_list):
    wb.get_baselines(folder=kiki.FTIR_file_location)

#%%

#%%
pp = PdfPages(''.join((kiki.thisfolder, '//Kiki_profiles.pdf')))

mixture = 96.

Dmix = [dlib.mix_olivine_mechanisms(mixture, wb.celsius) for wb in wb_list]


Dy = [0.15, 0.15, 0.15, 0.15, 1.15, 1.15, 1.15]

# bulk H baselines
for idx, wb in enumerate(wb_list):
     fig, axes = wb.plot_diffusion(log10D_m2s=Dmix[idx],
                                  labelDy=Dy[idx],
#                                  labelD=False,
                                  wholeblock=True,
                                  show_line_at_init=True
                                    )
     axes[1].set_title(''.join((wb.name, ' bulk H')))
#    axes[0].set_title('')
#    axes[2].set_title('')
     fig.set_size_inches(6, 3)
     for ax in axes:
        ax.set_ylim(0, 1.3)
     fig.savefig(pp, format='pdf')
#
## [Ti]    
#for wb in wb_list:
#    wb.get_baselines(folder=kiki.FTIR_file_location,
#                     baseline_ending='-baseline-Ti.CSV')
#    fig, axes = wb.plot_areas_3panels()
#    axes[1].set_title(''.join((wb.name, ' [Ti]')))
#    fig.set_size_inches(6, 3)
#    for ax in axes:
#        ax.set_ylim(0, 1.8)
#    fig.savefig(pp, format='pdf')
#
## [tri]
#for wb in wb_list:
#    wb.get_baselines(folder=kiki.FTIR_file_location,
#                     baseline_ending='-baseline-tri.CSV')
#    fig, axes = wb.plot_areas_3panels()
#    axes[1].set_title(''.join((wb.name, ' [tri]')))
#    fig.set_size_inches(6, 3)
#    for ax in axes:
#        ax.set_ylim(0, 1.3)
#    fig.savefig(pp, format='pdf')
#
pp.close()

