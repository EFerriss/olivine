# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:21:12 2016

@author: Ferriss
"""

import olivine_spectra as ol
from pynams import styles as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

plt.style.use('paper')
folder = 'C:\\Users\\Ferriss\\Documents\\olivine\\figures\\'

WN_LOW = 3400.
WN_HIGH = 3660.
WN_LOW_KIKI = 3280.


#%% 17 Mar 2016 Kilauea Iki Kiki1 sample scoping out doubly polished piece
styles = [
          {'linestyle' : '-', 'color' : 'k', 'marker' : None, 'linewidth' : 1},
          {'linestyle' : '-', 'color' : 'purple', 'marker' : None, 'linewidth' : 1},
          {'linestyle' : '-', 'color' : 'blue', 'marker' : None, 'linewidth' : 1},
          {'linestyle' : '-', 'color' : 'green', 'marker' : None, 'linewidth' : 1},
          {'linestyle' : '-', 'color' : 'orangered', 'marker' : None, 'linewidth' : 1},
         ]

spec_list = [ol.Kiki1_scope_unpol,
             ol.Kiki1_scope_135deg,
             ol.Kiki1_scope_140deg,
             ol.Kiki1_scope_150deg]

fig, ax = ol.Kiki1_scope_unpol.plot_spectrum_outline()
fig_nobase, ax_nobase = ol.Kiki1_scope_unpol.plot_spectrum_outline()

for idx, spec in enumerate(spec_list):
    spec.make_baseline(linetype='quadratic', show_plot=False, shiftline=0.03)
    area = spec.area_under_curve(show_plot=False, printout=True)
    lab = ''.join((spec.fname, ': ' '{:.1f}'.format(area), ' cm2'))
    spec.plot_spectrum(figaxis=ax, style=styles[idx], label=spec.fname)   
    spec.plot_subtractbaseline(figaxis=ax_nobase, style=styles[idx], label=lab)


fig.set_size_inches(6,5)
fig_nobase.set_size_inches(6,5)    

#%% 31 Mar 2016 orienting polished Kilauea Iki sample Kiki1
styles = [
          {'linestyle' : '-', 'color' : 'k', 'marker' : None, 'linewidth' : 1},
          {'linestyle' : '-', 'color' : 'purple', 'marker' : None, 'linewidth' : 1},
          {'linestyle' : '-', 'color' : 'blue', 'marker' : None, 'linewidth' : 1},
          {'linestyle' : '-', 'color' : 'green', 'marker' : None, 'linewidth' : 1},
          {'linestyle' : '-', 'color' : 'orangered', 'marker' : None, 'linewidth' : 1},
         ]

spec_list = [
             ol.Kiki1_init_Ea_1,
             ol.Kiki1_init_Ea_2,
             ol.Kiki1_init_Eb_1,
             ol.Kiki1_init_Eb_2,
             ol.Kiki1_init_Ec
             ]

fig, ax = ol.Kiki1_scope_unpol.plot_spectrum_outline()

for idx, spec in enumerate(spec_list):
    lab = ''.join(('polarized || ', spec.polar, ', ray path || ', spec.raypath))
    spec.plot_spectrum(figaxis=ax, style=styles[idx], label=lab)   

fig.set_size_inches(5, 5)
ax.set_ylim(0, 1.)
ax.legend(loc=2)
ax.set_title('Kilauea Iki Kiki1 polarized spectra')

fig.savefig(folder+'Kiki1_orienting.png', dpi=150)
print 'Finished'

#%% Comparison to Fig. 10 in Miller et al. 1987 for San Carlos and Kilauea Iki
fig, ax = ol.SC1_2_hyd_da_unpol.plot_spectrum_outline(size_inches=(6.5, 5))

ol.SC1_2_hyd_Ea.plot_spectrum(figaxis=ax, style=st.style_1, 
                              label='E || a hydrated SC1-2', offset=0.6) 
ol.SC1_2_hyd_Eb.plot_spectrum(figaxis=ax, style=st.style_2, 
                              label='E || b hydrated SC1-2', offset=0.4)
ol.SC1_2_hyd_Ec.plot_spectrum(figaxis=ax, style=st.style_3, 
                              label='E || c hydrated SC1-2', offset=0.)

ol.Kiki1_init_Ea_1.plot_spectrum(figaxis=ax, style=st.style_1a, 
                                 label='E || ~a Kiki1', offset=0.6)
ol.Kiki1_init_Eb_1.plot_spectrum(figaxis=ax, style=st.style_2a, 
                                 label='E || ~b Kiki1', offset=0.4)
ol.Kiki1_init_Ec.plot_spectrum(figaxis=ax, style=st.style_3a, 
                                 label='E || ~c Kiki1', offset=0.)
                          
ax.legend()
ax.set_title('hydrated San Carlos olivine (SC1-2) and Kilauea Iki olivine (Kiki1)')
ax.set_xlim(3700, 3200)
ax.set_ylim(0, 1.6)

ynumber = ax.get_ylim()[1] - 0.05
peak_list = [3598, 3573, 3542, 3525, 3489]
peak_labels = ['[?]'] * len(peak_list)
for idx, peak in enumerate(peak_list):
    label = str(peak)
    ax.plot([peak, peak], ax.get_ylim(), '-k', linewidth=1, color='purple')
    ax.text(peak, ynumber, label, rotation=90., backgroundcolor='w', 
            ha='center', va='top')

fig.subplots_adjust(left=0.12, bottom=0.17)
fig.savefig(folder + 'Kiki1-SC-peaks.png', dpi=150)
print 'Finished'

#%% Kilauea Iki Kiki1 peak distribution
fig, ax = ol.SC1_2_hyd_da_unpol.plot_spectrum_outline(size_inches=(6.5, 5))

ol.Kiki1_init_Ea_1.plot_spectrum(figaxis=ax, style=st.style_1a, 
                                 label='E || ~a Kiki1', offset=0.6)
ol.Kiki1_init_Eb_1.plot_spectrum(figaxis=ax, style=st.style_2a, 
                                 label='E || ~b Kiki1', offset=0.4)
ol.Kiki1_init_Ec.plot_spectrum(figaxis=ax, style=st.style_3a, 
                                 label='E || ~c Kiki1', offset=0.)
ax.text(3210, 0.95, 'E || [100]', ha='right', backgroundcolor='w')
ax.text(3210, 0.55, 'E || [010]', ha='right', backgroundcolor='w')
ax.text(3210, 0.2, 'E || [001]', ha='right', backgroundcolor='w')
                          
ax.set_title('Kilauea Iki olivine (Kiki1) polarized FTIR spectra')
ax.set_xlim(3700, 3200)
ax.set_ylim(0, 1.6)

ynumber = ax.get_ylim()[1] - 0.05
peak_list = [3598, 3573, 3542, 3525, 3489, 3358, 3330]
peak_labels = ['[?]'] * len(peak_list)
for idx, peak in enumerate(peak_list):
    label = str(peak)
    ax.plot([peak, peak], ax.get_ylim(), '-k', linewidth=1, color='purple')
    ax.text(peak, ynumber, label, rotation=90., backgroundcolor='w', 
            ha='center', va='top')

fig.subplots_adjust(left=0.12, bottom=0.17)
fig.savefig(folder + 'Kiki1-peaks.png', dpi=150)
print 'Finished'

#%% estimated water in Kiki1
olivines = [ol.Kiki1_init_Ea_1, ol.Kiki1_init_Eb_1, ol.Kiki1_init_Ec]

waters = [1, 1, 1]
for idx, olivine in enumerate(olivines):
    olivine.make_baseline(linetype='quadratic', shiftline=0.04, 
                          show_plot=False, wn_low=WN_LOW_KIKI,
                          wn_high=WN_HIGH)
    area, waters[idx] = olivine.water(phase_name='olivine', 
                                calibration="Bell", show_plot=False)
    fig, ax = olivine.plot_showbaseline()
    ax.set_xlim(4000., 3000.)

water = np.mean(waters)
print
print 'estimated water in ppm H2O in Kilauea Iki sample Kiki1:', water

#%% 13 Apr 2016 initial profiles for Kilauea Iki sample Kiki1
WN_HIGH = 3650. # The move to 3650 shows clear drops on the edges.
WN_LOW = 3400. # was 3440

reload(ol)
wb = ol.wb_Kiki_init

wb.make_baselines(show_plot=False, wn_high=WN_HIGH, wn_low=WN_LOW)
style = st.style_points2
style['label'] = 'peaks > 3440 cm$^{-1}$'
fig, ax3 = wb.plot_areas_3panels(styles3=[style]*3, 
                                 show_line_at_1=False, 
                                 get_saved_baseline=False)

reload(ol)
wb = ol.wb_Kiki_init

wb.make_baselines(show_plot=False, wn_high=WN_HIGH, wn_low=WN_LOW_KIKI,)
style = st.style_points4
style['label'] = 'all peaks'
wb.plot_areas_3panels(fig_ax3=ax3, styles3=[style]*3, get_saved_baseline=False,
                      show_line_at_1=True, show_spectra=False)

ax3[1].set_title('Kilauea Iki olivine phenocryst Kiki initial profiles')
for ax in ax3:
    ax.set_ylim(0.7, 1.2)

ax3[2].legend(loc=4, fontsize=10, ncol=2)
fig.set_size_inches(5, 3)
fig.savefig(folder + 'Kiki1-initial-profiles.png', dpi=150)

#%% 16 May 2016: linear baselines + peakfitting in Matlab
reload(ol)
wb = ol.wb_Kiki_init
wb.make_baselines(show_plot=False, wn_high=WN_HIGH, wn_low=WN_LOW_KIKI, 
                  linetype='line')
wb.save_baselines(initial_too=False)                  
wb.matlab()

#%% Initial peakfit attempt with linear baselines
pp = PdfPages('KilaueaIki_peakfits_initialpass.pdf')
wb = ol.wb_Kiki_init
wb.get_baselines()
wb.get_peakfit()

tops = [70, 4, 10, 10, 5, 12, 16, 5, 4]
tops_h = [0.2, 0.6, 0.5, 0.4, 0.4, 0.3, 0.3, 0.2]


for profile in ol.wb_Kiki_init.profiles:
    for idx, spectrum in enumerate(profile.spectra_list):
        fig, ax = spectrum.plot_peakfit_and_baseline(legloc=2)
        fig.set_size_inches(6, 6)
        ax.set_ylim(0, 1.0)
        ax.set_xlim(3800, 3200)
        title = ''.join((profile.profile_name, '\n ', 
                         '{:.1f}'.format(profile.positions_microns[idx]),
                         ' $\mu$m || ', profile.direction, ', ray path || ',
                         profile.raypath))
        top = ax.get_ylim()[1]
        ax.set_ylim(-0.1, top)                             
        ax.set_title(title)                         
        pp.savefig()
        fig.clf()
        
for idx, peak_idx in enumerate([None] + range(len(wb.profiles[0].peakpos))):
    fig, ax = wb.plot_areas_3panels(peak_idx=peak_idx, wholeblock=False,
                                    top=tops[idx], show_line_at_1=False)
    plt.subplots_adjust(bottom=0.35)
    pp.savefig()

for idx, peak_idx in enumerate(range(len(wb.profiles[0].peakpos))):
    fig, ax = wb.plot_areas_3panels(peak_idx=peak_idx, wholeblock=False,
                                    top=tops_h[idx], show_line_at_1=False,
                                    heights_instead=True)
    plt.subplots_adjust(bottom=0.35)
    pp.savefig()

# show alternate, shorter baseline
reload(ol)
wb.make_baselines(show_plot=False, wn_high=3650., wn_low=WN_LOW_KIKI, 
                  linetype='line')
for profile in ol.wb_Kiki_init.profiles:
    for idx, spectrum in enumerate(profile.spectra_list):
        fig, ax = spectrum.plot_showbaseline()
        fig.set_size_inches(6, 6)
        ax.set_xlim(3800, 3200)
        title = ''.join((profile.profile_name, 'prev. baseline\n ', 
                         '{:.1f}'.format(profile.positions_microns[idx]),
                         ' $\mu$m || ', profile.direction, ', ray path || ',
                         profile.raypath))
        top = ax.get_ylim()[1]
        ax.set_ylim(-0.1, top)                             
        ax.set_title(title)                         
        pp.savefig()
        fig.clf()

pp.close()        

#%% 2nd attempt at peakfitting - now using quadratic baselines
pp = PdfPages('KilaueaIki_peakfits_quadraticbaselines.pdf')

wb = ol.wb_Kiki_init
wb.get_baselines()
wb.get_peakfit()

for profile in wb.profiles:
    for idx, spectrum in enumerate(profile.spectra_list):
        ### making baseline
        WN_MID = spectrum.find_lowest_wn_over_given_range(relative=True)
#        spectrum.plot_spectrum()
        spectrum.make_baseline(show_plot=False, linetype='quadratic', 
                               wn_high=WN_HIGH, wn_mid=WN_MID, 
                               wn_low=WN_LOW_KIKI, show_fit_values=True)
##        spectrum.save_baseline()
#
#        fig, ax = spectrum.plot_peakfit_and_baseline()
#        fig.set_size_inches(6, 6)
#        ax.set_xlim(4000, 3000)
#        top = ax.get_ylim()[1]
#        ax.set_ylim(-0.1, top)                             
#
#        title = ''.join((profile.profile_name, ' quadratic baseline\n ', 
#                         '{:.1f}'.format(profile.positions_microns[idx]),
#                         ' $\mu$m || ', profile.direction, ', ray path || ',
#                         profile.raypath))
#        ax.set_title(title)                         
#
##        ax.plot([WN_MID, WN_MID], ax.get_ylim(), '-r', zorder=0)
#
#        pp.savefig()
#        fig.clf()
#

tops = [70, 4, 10, 10, 5, 12, 16, 5, 4]
tops_h = [0.2, 0.6, 0.5, 0.4, 0.4, 0.3, 0.3, 0.2]

for idx, peak_idx in enumerate([None] + range(len(wb.profiles[0].peakpos))):
    fig, ax = wb.plot_areas_3panels(peak_idx=peak_idx, wholeblock=False,
                                    top=tops[idx], show_line_at_1=False)
    plt.subplots_adjust(bottom=0.35)
    pp.savefig()

for idx, peak_idx in enumerate([None] + range(len(wb.profiles[0].peakpos))):
    fig, ax = wb.plot_areas_3panels(peak_idx=peak_idx, wholeblock=True,
                                    top=1.2, show_line_at_1=False)
    plt.subplots_adjust(bottom=0.35)
    pp.savefig()

for idx, peak_idx in enumerate(range(len(wb.profiles[0].peakpos))):
    fig, ax = wb.plot_areas_3panels(peak_idx=peak_idx, wholeblock=False,
                                    top=tops_h[idx], show_line_at_1=False,
                                    heights_instead=True)
    plt.subplots_adjust(bottom=0.35)
    pp.savefig()

for idx, peak_idx in enumerate(range(len(wb.profiles[0].peakpos))):
    fig, ax = wb.plot_areas_3panels(peak_idx=peak_idx, wholeblock=True,
                                    top=1.2, show_line_at_1=False,
                                    heights_instead=True)
    plt.subplots_adjust(bottom=0.35)
    pp.savefig()

pp.close()
#

