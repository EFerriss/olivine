# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:08:02 2017

@author: Elizabeth
"""

from olivine.SanCarlos import SanCarlos_spectra as SC
from pynams import styles
import olivine

high_ending = olivine.high_ending
low_ending = olivine.low_ending

#%% Range of 3 baselines for initial concentration estimates from SC1-1
spec = SC.SC_untreated_Ea
spec.make_baseline(curvature=0.04)
fig, ax = spec.plot_showbaseline()
fig.set_size_inches(14, 14)
spec.save_baseline()
spec.make_baseline(curvature=0.06)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=low_ending)
spec.make_baseline(curvature=-0.01, wn_low=3500, wn_high=3650)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=high_ending)

#%%
spec = SC.SC_untreated_Eb
spec.make_baseline(curvature=0.025, abs_smear_high=10)
fig, ax = spec.plot_showbaseline()
fig.set_size_inches(14, 14)
spec.save_baseline()
spec.make_baseline(force_through_wn=3350, abs_smear_high=10)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=high_ending)
spec.make_baseline(curvature=0.04, abs_smear_high=10)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=low_ending)

#%%
spec = SC.SC_untreated_Ec
spec.make_baseline(curvature=0.075, abs_smear_high=10, wn_high=3750)
fig, ax = spec.plot_showbaseline()
fig.set_size_inches(14, 14)
spec.save_baseline()
spec.make_baseline(curvature=0.09, abs_smear_high=10, wn_high=3800)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=low_ending)
spec.make_baseline(curvature=0.05, abs_smear_high=10)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=high_ending)

#%% final - SC1-2 after dehydration
spec = SC.SC_final_averaged
spec.make_baseline(curvature=0.04)
fig, ax = spec.plot_showbaseline()
fig.set_size_inches(14, 14)
spec.save_baseline()
spec.make_baseline(curvature=0.06)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=low_ending)
spec.make_baseline(force_through_wn=3550, wn_low=3350, wn_high=3650)
spec.plot_showbaseline(axes=ax, style_base=styles.style_3)
spec.save_baseline(baseline_ending=high_ending)

#%% SC1-7 hydrated
wb = SC.wb_1000C_SC1_7
spec7 = SC.spec7
init = SC.SC_untreated_Ea
fig, ax = init.plot_spectrum(style={'color':'r', 'linewidth':3}, offset=0.04)

baseline1 = {'abs_smear_low':10, 'abs_smear_high':10, 'wn_low':3100, 
             'curvature':0.075}
spec7.make_baseline(**baseline1)
spec7.save_baseline(folder=SC.FTIR_file_location)
spec7.plot_showbaseline(axes=ax)

baseline2 = {'abs_smear_low':10, 'abs_smear_high':10, 'wn_low':3100, 
             'curvature':0.09}
spec7.make_baseline(**baseline2)
spec7.save_baseline(baseline_ending=low_ending, folder=SC.FTIR_file_location)
spec7.plot_showbaseline(axes=ax)

#baseline3 = {'abs_smear_low':10, 'abs_smear_high':10, 'wn_low':3100, 
#             'curvature':0.05}
baseline3 = {'abs_smear_low':10, 'abs_smear_high':10, 'wn_low':3200}
spec7.make_baseline(**baseline3)
spec7.save_baseline(baseline_ending=high_ending, folder=SC.FTIR_file_location)
spec7.plot_showbaseline(axes=ax)

wb.make_baselines(**baseline1)
wb.save_baselines()
wb.make_baselines(**baseline2)
wb.save_baselines(baseline_ending=low_ending)
wb.make_baselines(**baseline3)
wb.save_baselines(baseline_ending=high_ending)

#%% SC1-2 hydrated
wb = SC.wb_800C_hyd
spec2 = SC.spec2
init = SC.SC_untreated_Ea
fig, ax = init.plot_spectrum(style={'color':'r', 'linewidth':3}, offset=-0.03)

baseline = {'abs_smear_high':10, 'wn_low':3200, 'curvature':0.05}
spec2.make_baseline(**baseline)
spec2.save_baseline()
wb.make_baselines(**baseline)
wb.save_baselines()
spec2.plot_showbaseline(axes=ax)

baseline2 = {'wn_low':3400}
spec2.make_baseline(**baseline2)
spec2.save_baseline(baseline_ending=high_ending)
spec2.plot_showbaseline(axes=ax)
wb.make_baselines(**baseline2)
wb.save_baselines(baseline_ending=high_ending)

baseline3 = {'abs_smear_high':10, 'wn_low':3200, 'curvature':0.07}
spec2.make_baseline(**baseline3)
spec2.save_baseline(baseline_ending=low_ending)
wb.make_baselines(**baseline3)
wb.save_baselines(baseline_ending=low_ending)
spec2.plot_showbaseline(axes=ax)