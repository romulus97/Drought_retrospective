# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:41:34 2019

@author: jkern
"""

from __future__ import division
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

years = range(2007,2019)

for y in years: 
    
    y_index = years.index(y)    
    sheet = 'year ' + str(y)
    df_data = pd.read_excel('hydro_07_18_DAILY.xlsx',header=0,sheet_name=sheet)
    hydro = df_data.loc[:,'hydro']
    
    if y_index<1:
        combined = hydro
    else:
        combined = combined.append(hydro)

combined.to_excel('historic_hydro.xlsx')
