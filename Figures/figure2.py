# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:21:06 2019

@author: sdenaro
"""
from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# plot data
A = .4
afont= {'fontname':'Arial', 'fontweight':'bold'}
plt.rcParams["font.family"] = "Arial"
label_size = 12
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['ytick.labelsize'] = label_size

#temperatures
df_temps_1953_2007 = pd.read_excel('../Stochastic_engine/Synthetic_streamflows/hist_temps_1953_2007.xlsx',header=0)

#pull out average temperatures, plot them in degrees C, in gray for each year
days = int(len(df_temps_1953_2007))
years = int(days/365)
avg_1953_2007 = np.zeros((days,1))
for i in range(0,days):
    avg_1953_2007[i] = (np.mean(df_temps_1953_2007.loc[i,'Salem':])-32)*5/9
    
plt.figure(0)
for i in range(0,years):
    plt.plot(avg_1953_2007[i*365:i*365+365],c='0.75')

#pull out average temperatures, plot them in degrees C, different color for each year
df_temps_2012_2016 = pd.read_csv('../Stochastic_engine/Synthetic_weather/synthetic_weather_data.csv',header=0)

sites = ['SALEM_T','EUGENE_T','SEATTLE_T','BOISE_T','PORTLAND_T','SPOKANE_T','FRESNO_T','LOS ANGELES_T','SAN DIEGO_T','SACRAMENTO_T','SAN JOSE_T','SAN FRANCISCO_T','TUCSON_T','PHOENIX_T','LAS VEGAS_T']
df_site_data = df_temps_2012_2016[sites]
days = int(len(df_temps_2012_2016))
years = int(days/365)
avg_2012_2016 = np.zeros((days,1))
for i in range(0,days):
    avg_2012_2016[i] = np.mean(df_site_data.loc[i,:])

colors = plt.cm.cool(np.linspace(0,1,years))
for i in range(0,years):
    plt.plot(avg_2012_2016[i*365:i*365+365],color=colors[i])

plt.ylabel('Temperature Degrees C',fontsize=14,**afont)
plt.xlabel('Day of Year',fontsize=14,**afont)

#wind
df_wind = pd.read_csv('../Stochastic_engine/Historical_weather_analysis/WIND_TEMP.csv',header=0)

