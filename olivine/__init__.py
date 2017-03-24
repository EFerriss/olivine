# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:44:01 2015

@author: Ferriss
"""
from __future__ import absolute_import
import os
import matplotlib
from . import FTIR

FTIR_file_location = ''.join((os.path.dirname(FTIR.__file__), '\\'))
thisfolder = ''.join((FTIR_file_location, '..\\'))

matplotlib.rcParams.update({'font.size': 8})

high_ending = '-high-baseline.CSV'
low_ending = '-low-baseline.CSV'