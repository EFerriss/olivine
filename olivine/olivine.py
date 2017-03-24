# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:33:19 2017

@author: Ferriss

Some olivine peak-specific functions and labels
"""
from __future__ import print_function, division
from pynams import styles
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from olivine.SanCarlos import SanCarlos_spectra as SC

whole_block_label_list = SC.whole_block_label_list
FTIR_file_location = SC.FTIR_file_location
whole_block_list = SC.whole_block_list

#%%
# peak identifications according to Padron-Navarta et al. 2014 Table 1
# and Berry et al. 2005 Figure 1
olivine_peak_id = dict()
olivine_peak_id['[Ti]'] = [3572, 3525]
olivine_peak_id['[triv]'] = [3355, 3350, 3325]
olivine_peak_id['[Mg]'] = [3220, 3160]
olivine_peak_id['[Si]'] = [3613, 3612, 3600, 3580, 3566, 3555, 3542, 3477, 
                           3460, 3453, 3428]

# peaks positions used to resolve all peaks in this study
likely_Si = [3275., 3405., 3480., 3542., 3566., 3600., 3613.]
likely_triv = [3350.]
likely_Ti = [3572., 3525]
peaks = likely_triv + likely_Si + likely_Ti
        
def plot_peaks(ax, loc=2, Ti=True, triv=False, Mg=True, Si=False, 
               other_peaks=[], likely_Si=likely_Si, likely_tri=likely_triv):
    """Plots color-coded peak location lines on axis"""
    # make legend
    if (Si is True) or (len(likely_Si)>0):
        ax.plot([0, 0], [0, 0], '-y', linewidth=1, label='[Si]')
    if Ti is True:
        ax.plot([0, 0], [0, 0], '-k', linewidth=1, label='[Ti]')
    if triv is True or len(likely_tri)>0:
        ax.plot([0, 0], [0, 0], '-', linewidth=0.5, label='[triv]', color='purple')
    if Mg is True:
        ax.plot([0, 0], [0, 0], '-', color='grey', label='[Mg]')
    if len(other_peaks) > 0:
        ax.plot([0, 0], [0, 0], '-r', linewidth=1, label='[?]')
    ax.legend(loc=loc, fontsize=8, ncol=1)

    if Ti is True:
        for peak in olivine_peak_id['[Ti]']:
            ax.plot([peak, peak], ax.get_ylim(), '-k', linewidth=1, 
                    label='[Ti]')
        
    if triv is True:
        for peak in olivine_peak_id['[triv]']:
            ax.plot([peak, peak], ax.get_ylim(), '-', linewidth=0.5, 
                    label='[triv]', color='purple')
            
    if Mg is True:
        for peak in olivine_peak_id['[Mg]']:
            ax.plot([peak, peak], ax.get_ylim(), '-', color='grey', label='[Mg]')
            
    if Si is True:
        for peak in olivine_peak_id['[Si]']:
            ax.plot([peak, peak], ax.get_ylim(), '-y', linewidth=1, 
                    label='[Si]')
            
    for peak in likely_Si:
        ax.plot([peak, peak], ax.get_ylim(), '-y', linewidth=1, label='[Si]')

    for peak in likely_tri:
        ax.plot([peak, peak], ax.get_ylim(), '-', linewidth=0.5, label='[tri]',
                color='purple')

    for peak in other_peaks:
        ax.plot([peak, peak], ax.get_ylim(), '-r', linewidth=1, label='[?]')

def plot_timeseries_outline():
    fig, ax = plt.subplots(1)
    fig.set_size_inches(6, 6)
    x = range(len(whole_block_label_list))
    plt.xticks(x, whole_block_label_list, rotation=20)
    fig.autofmt_xdate()
    ax.set_xlim(x[0]-1, x[-1]+1)
    ax.set_xlabel('hydration and dehydration at 800$\degree$C, NNO')
    return fig, ax, x

def get_low_stuff(wblist):
    for idx, wb in enumerate(wblist):
        wb.label = whole_block_label_list[idx]
        wb.style = styles.style_list_points[idx]
        wb.get_baselines(folder=FTIR_file_location,
                         baseline_ending='-baseline-low.CSV')
    
    # set up all peakfit and baseline information
    for idx, wb in enumerate(whole_block_list):
        for prof in wb.profiles:
            for spec in prof.spectra:
                spec.get_baseline(baseline_ending='-baseline-low.CSV')
                spec.get_peakfit(peak_ending='-peakfit-low.CSV', 
                                 baseline_ending='-baseline-low.CSV')
                 
                # getting rid of peak at 3613 if accidentally included
                if len(spec.peakpos) > 6:
                    spec.peakpos = np.delete(spec.peakpos, [6])
                    spec.peak_heights = np.delete(spec.peak_heights, [6])
                    spec.peak_widths = np.delete(spec.peak_widths, [6])
                    spec.peak_areas = np.delete(spec.peak_areas, [6])
    
        wb.make_composite_peak([1, 4]) # [Ti] is peak_idx 6
        wb.make_composite_peak([0, 2, 3, 5]) # all [Si] is peak_idx 7
        wb.make_composite_peak([0, 2, 3]) # low-wn [Si] is peak_idx 8
        for prof in wb.profiles:
            prof.get_peak_info()
        
    # get the diffusivities 
    fname = ''.join((savefolder, 'diffusivities.xlsx'))
    xl_workbook = xlrd.open_workbook(fname)
    xl_sheet = xl_workbook.sheet_by_index(0)
    idx_Dx = 13
    idx_Dy = 15
    idx_Dz = 17
    idx_row = 2

    for wb in wblist[2:]:
        peakpos = wb.profiles[0].peakpos
        wb.peakpos = peakpos

        for idx_peak, peak in enumerate([None] + list(peakpos)):
            row = xl_sheet.row(idx_row)
            D3 = [row[idx_Dx].value, row[idx_Dy].value, row[idx_Dz].value]
            D3e = [row[idx_Dx+1].value, row[idx_Dy+1].value, row[idx_Dz+1].value]
            if peak is not None:
                wb.peak_diffusivities.append(D3) # peak-specific
                wb.peak_diffusivities_errors.append(D3e)
            else:
                wb.D_area_wb = D3 # bulk H
                wb.D_area_wb_error = D3e
            idx_row = idx_row + 1        