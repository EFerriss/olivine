# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 10:33:39 2017

@author: Ferriss

Arrenius diagram with all data for H diffusion in olivine
"""
from __future__ import print_function
from pynams.diffusion import arrhenius
from pynams.diffusion.arrhenius import Diffusivities
from pynams import dlib
import pandas as pd
from olivine import FTIR_file_location

# import my data from file
filename = ''.join((FTIR_file_location, '..\\Table2_Diffusivities.csv'))
s = pd.read_csv(filename)


wb = s[s.Sample=='SC1-7']
Da = [D for D in wb['log10Da'][:]]
C_all = [1000.]*len(Da)

#wb7 = Diffusivities(description='SC1-7',
#                    celsius_all=[1000.], logDx=[-12.8])

#%% set plotting styles
st = {'linestyle':'none'}
st_a = {'marker':'o'}
st_b = {'marker':'s'}
st_c = {'marker':'^'}
st_u = {'marker':'*'}
st_wb2 = {'color':'#2ca02c'}
st_wb7 = {'color':'#ff7f0e'}
st_kiki = {'color':'darkmagenta'}
st_Fo = {'color':'none', 'markeredgecolor':'k'}
st_pp = {'color':'k'}
st_nat = {'color':'brown'}
st_pv = {'color':'grey', 'markeredgecolor':'k'}

def merge_styles(basestyle, *args):
    """ Merge multiple style dictionaries."""
    z = basestyle.copy()
    for arg in args:
        z.update(arg)
    return z

st_wb7a = merge_styles(st, st_wb7, st_a)
st_wb7b = merge_styles(st, st_wb7, st_b)
st_wb7c = merge_styles(st, st_wb7, st_c)
st_wb2a = merge_styles(st, st_wb2, st_a)
st_wb2b = merge_styles(st, st_wb2, st_b)
st_wb2c = merge_styles(st, st_wb2, st_c)
st_ppa = merge_styles(st, st_pp, st_a)
st_ppb = merge_styles(st, st_pp, st_b)
st_ppc = merge_styles(st, st_pp, st_c)
st_pva = merge_styles(st, st_pv, st_a)
st_pvb = merge_styles(st, st_pv, st_b)
st_pvc = merge_styles(st, st_pv, st_c)
st_Foa = merge_styles(st, st_Fo, st_a)
st_Fob = merge_styles(st, st_Fo, st_b)
st_Foc = merge_styles(st, st_Fo, st_c)
st_PN = merge_styles(st, st_Fo, st_u)
st_natu = merge_styles(st, st_nat, st_u)

##%%
fig, ax, legend_handle = arrhenius.Arrhenius_outline(xlow=6, xhigh=9.5,
                                                     ybottom=-16, ytop=-8)
fig.set_size_inches(8, 8)

pltline = False
dlib.KM98_fast.plotD(ax, orient='a', plotline=pltline, extrapolate_line=True, style=st_ppa)
dlib.KM98_fast.plotD(ax, orient='b', plotline=pltline, extrapolate_line=True, style=st_ppb)
dlib.KM98_fast.plotD(ax, orient='c', plotline=pltline, extrapolate_line=True, style=st_ppc)
dlib.KM98_slow.plotD(ax, orient='a', plotline=pltline, extrapolate_line=True, style=st_pva)
dlib.KM98_slow.plotD(ax, orient='b', plotline=pltline, extrapolate_line=True, style=st_pvb)
dlib.KM98_slow.plotD(ax, orient='c', plotline=pltline, extrapolate_line=True, style=st_pvc)
dlib.DM06_fast.plotD(ax, orient='a', plotline=False, style=st_ppa)
dlib.DM06_fast.plotD(ax, orient='b', plotline=False, style=st_ppb)
dlib.DM06_fast.plotD(ax, orient='c', plotline=False, style=st_ppc)
dlib.DM06_slow.plotD(ax, orient='a', plotline=False, style=st_pva)
dlib.DM06_slow.plotD(ax, orient='b', plotline=False, style=st_pvb)
dlib.DM06_slow.plotD(ax, orient='c', plotline=False, style=st_pvc)

dlib.DM03.plotD(ax, orient='a', plotline=False, style=st_Foa)
dlib.DM03.plotD(ax, orient='b', plotline=False, style=st_Fob)
dlib.DM03.plotD(ax, orient='c', plotline=False, style=st_Foc)
dlib.pnav_Mg.plotD(ax, plotline=False, style=st_PN)
dlib.pnav_Si.plotD(ax, plotline=False, style=st_PN)
dlib.pnav_SiTi.plotD(ax, plotline=False, style=st_PN)
dlib.pnav_Ti.plotD(ax, plotline=False, style=st_PN)

dlib.Hauri02.plotD(ax, plotline=False, style=st_natu)
dlib.Portnyagin08.plotD(ax, plotline=False, style=st_natu)
dlib.Chen11.plotD(ax, plotline=False, style=st_natu)
dlib.Gaetani12.plotD(ax, plotline=False, style=st_natu)

wb7.plotD(ax, orient='a', plotline=False, style=st_wb7a)

