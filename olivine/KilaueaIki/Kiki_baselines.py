#-*- coding: utf-8 -*-
"""
Created on Fri Dec 09 14:24:39 2016

@author: Ferriss

Make and save Kilauea Iki olivine baselines
"""

from __future__ import division, print_function
from olivine.KilaueaIki import Kiki_spectra as kiki
#from matplotlib.backends.backend_pdf import PdfPages
from pynams import styles
import olivine

thisfolder = kiki.thisfolder

wb_list = [
           kiki.wb_Kiki_init, 
           kiki.wb_Kiki_1hr, 
           kiki.wb_Kiki_8hr,
           kiki.wb_Kiki_1000C_3hr, 
           kiki.wb_Kiki_1000C_6hr, 
           kiki.wb_Kiki_1000C_7hr,
           kiki.wb_Kiki_ox]

high_ending = olivine.high_ending
low_ending = olivine.low_ending

#%% Range of 3 baselines for initial concentration estimates
spec = kiki.Kiki_init_Ea

baselineKiki = {'curvature':0.05, 'abs_smear_high':10}
spec.make_baseline(**baselineKiki)
fig, ax = spec.plot_showbaseline()
fig.set_size_inches(14, 14)
spec.save_baseline()

spec.make_baseline(force_through_wn=3400, wn_low=3300, abs_smear_high=10)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=high_ending)

spec.make_baseline(curvature=0.1, abs_smear_high=10, wn_low=3100)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=low_ending)

spec = kiki.Kiki_init_Eb
spec.make_baseline(curvature=0.07, abs_smear_high=10, wn_low=3150)
fig, ax = spec.plot_showbaseline()
fig.set_size_inches(14, 14)
spec.save_baseline()
spec.make_baseline(force_through_wn=3400, wn_low=3150, abs_smear_high=10)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=high_ending)
spec.make_baseline(curvature=0.11, abs_smear_high=10, wn_low=3100)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=low_ending)

spec = kiki.Kiki_init_Ec
spec.make_baseline(curvature=0.05, abs_smear_high=10, wn_low=3150)
fig, ax = spec.plot_showbaseline()
fig.set_size_inches(14, 14)
spec.save_baseline()
spec.make_baseline(force_through_wn=3450, wn_low=3150, abs_smear_high=10)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=high_ending)
spec.make_baseline(curvature=0.08, abs_smear_high=10, wn_low=3100)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=low_ending)

#%% Averaged spectra before and after dehydration
spec = kiki.wb_Kiki_init_ave
spec.make_baseline(curvature=0.05, abs_smear_high=10, wn_low=3150)
spec.save_baseline()

spec = kiki.wb_Kiki_ox_ave
spec.make_baseline(curvature=0.05, abs_smear_high=10, wn_low=3150)
spec.save_baseline()

##%% Make all the baselines
##kiki.wb_Kiki_init.make_baselines(wn_low=3290, wn_high=3670, show_plot=False,
##                                 force_through_wn=3400)
#
##%% bulk H
#pp = PdfPages(''.join((kiki.thisfolder, '//Kiki_baselines.pdf')))
#
#for wb in wb_list:
#    wb.make_baselines(wn_low=3290, wn_high=3620, 
#                      abs_smear_high=10, abs_smear_low=10,
#                      show_plot=False,
#                      force_through_wn=3440)
#    wb.save_baselines()
#
##    wb.profiles[0].make_baselines(curvature=0.05, show_plot=False,
##                       wn_low=3290, wn_high=3670,
##                       abs_smear_high=10, abs_smear_low=10)               
##    wb.profiles[1].make_baselines(force_quadratic_through_wn=3400, 
##                   wn_low=3290, wn_high=3670,
##                   abs_smear_high=10, abs_smear_low=10)
##    wb.profiles[2].make_baselines(force_quadratic_through_wn=3400, 
##                   wn_low=3290, wn_high=3670,
##                   abs_smear_high=10, abs_smear_low=10)
#for wb in wb_list:
#    for prof in wb.profiles:
#        for idx, spec in enumerate(prof.spectra):
#            fig, ax = spec.plot_showbaseline()
#            fig.set_size_inches(6, 6)
#            ax.set_ylim(0, 1)
#            title = ''.join((prof.name, '\n',
#                             str(prof.positions_microns[idx]), 
#                             ' $\mu$m, index ', str(idx)))
#            ax.set_title(title)
#            fig.savefig(pp, format='pdf')
#            fig.clf()
#
##for wb in wb_list:  
##    for prof in wb.profiles:
##        for idx, spec in enumerate(prof.spectra):
##            fig, ax = spec.plot_subtractbaseline()
##            fig.set_size_inches(6, 6)
##            ax.set_ylim(0, 0.8)
##            title = ''.join((prof.name, '\n',
##                             str(prof.positions_microns[idx]), 
##                             ' $\mu$m, index ', str(idx)))
##            ax.set_title(title)
##            fig.savefig(pp, format='pdf')
##            fig.clf()
#            
##            spec.save_baseline(folder=kiki.FTIR_file_location)
#pp.close()            
#
###%%
##pp = PdfPages(''.join((kiki.thisfolder, '//Kiki_baselines_Ti.pdf')))
##
##for wb in wb_list:
##    wb.make_baselines(wn_high=3670, wn_low=3400, abs_smear_high=10,
##                      abs_smear_low=10)
##    for prof in wb.profiles:
##        for idx, spec in enumerate(prof.spectra):
##            fig, ax = spec.plot_showbaseline()
##            fig.set_size_inches(6, 6)
##            ax.set_ylim(0, 1.)
##            title = ''.join((prof.name, '\n',
##                             str(prof.positions_microns[idx]), ' $\mu$m'))
##            ax.set_title(title)
##            fig.savefig(pp, format='pdf')
##            fig.clf()
##            
##for wb in wb_list:
##    for prof in wb.profiles:
##        for idx, spec in enumerate(prof.spectra):
##            fig, ax = spec.plot_subtractbaseline()
##            fig.set_size_inches(6, 6)
##            ax.set_ylim(0, 0.7)
##            title = ''.join((prof.name, '\n',
##                             str(prof.positions_microns[idx]), ' $\mu$m'))
##            ax.set_title(title)
##            fig.savefig(pp, format='pdf')
##            fig.clf()
##            spec.save_baseline(folder=kiki.FTIR_file_location,
##                               baseline_ending='-baseline-Ti.CSV')
##pp.close()            
##
###%%
##pp = PdfPages(''.join((kiki.thisfolder, '//Kiki_baselines_tri.pdf')))
##
##for wb in wb_list:
##    wb.make_baselines(wn_high=3400, wn_low=3290, abs_smear_high=10,
##                      abs_smear_low=10)
##    for prof in wb.profiles:
##        for idx, spec in enumerate(prof.spectra):
##            fig, ax = spec.plot_showbaseline()
##            fig.set_size_inches(6, 6)
##            ax.set_ylim(0, 1)
##            title = ''.join((prof.name, '\n',
##                             str(prof.positions_microns[idx]), ' $\mu$m'))
##            ax.set_title(title)
##            fig.savefig(pp, format='pdf')
##            fig.clf()
##            
##for wb in wb_list:
##    for prof in wb.profiles:
##        for idx, spec in enumerate(prof.spectra):
##            fig, ax = spec.plot_subtractbaseline()
##            fig.set_size_inches(6, 6)
##            ax.set_ylim(0, 0.2)
##            title = ''.join((prof.name, '\n',
##                             str(prof.positions_microns[idx]), ' $\mu$m'))
##            ax.set_title(title)
##            fig.savefig(pp, format='pdf')
##            fig.clf()
##            spec.save_baseline(folder=kiki.FTIR_file_location,
##                               baseline_ending='-baseline-tri.CSV')
##pp.close()            
##
