from astroML.datasets import fetch_LINEAR_sample

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from astropy.time import Time

import os,sys

'''
Analysis for the LINEAR data. 
LINEAR sample data contains time series data of 7010 stars, all having brigness magnitudes for 257 time points, in MJD format.
'''

LINEAR_data = fetch_LINEAR_sample()
print('List of IDs:-', LINEAR_data.ids)

star_id = 10040133
t, mag, dmag = LINEAR_data.get_light_curve(star_id).T

t_diff = [t[n]-t[n-1] for n in range(1,len(t))]
#print(t_diff)

fig = plt.figure(figsize=(12, 8))
ax = plt.gca()

plt.plot(t,mag,color='gray', marker='o', linestyle='dashed', linewidth=2, markersize=5)
plt.grid()
ax.set(xlabel='Observation time (days)', ylabel='Observed Magnitude', title='LINEAR object {0}'.format(star_id))

# Auto correlation function
from astroML.time_series import ACF

acf,asso_t = ACF.ACF_scargle(t, mag, dmag)
acf = acf[1024:]
asso_t = asso_t[1024:]
print('Values of ACF:- ', acf, '\n times:-', asso_t)
fig = plt.figure(figsize=(12, 8))
ax = plt.gca()

plt.plot(asso_t,acf)
ax.set(xlabel='Associated Time Differences', ylabel='Auto correlation function (ACF)')
plt.grid()

# Lomb-Scargle Periodogram
from astropy.stats import LombScargle

#n = len(t)
#fc = [(i/n) for i in range(1,n)]
frequency, power = LombScargle(t, mag, dmag).autopower()
print('Maximum power: {}, occured at time period : {} '.format(max(power),1. / frequency[np.argmax(power)]))

fig, ax = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Lomb-Scargle Periodogram for LINEAR object {0}'.format(star_id))
fig.subplots_adjust(bottom=0.12, left=0.07, right=0.95)

# plot the raw data
ax[0].plot(frequency, power)
ax[0].set(xlabel='Frequency',ylabel='Lomb-Scargle Power')

# plot the periodogram
ax[1].plot(1. / frequency, power)
ax[1].set(xlim=(0,100),xlabel='period (days)',ylabel='Lomb-Scargle Power')

# conversion to datetime from MJD, in a dataframe
data = {'time':t,'values':mag}
df = pd.DataFrame(data)
df = df.set_index('time')

tf = Time(df.index,format = 'mjd')
tf.format = 'datetime'
df.index = tf.value
df.index = pd.to_datetime(df.index)

# Seasonality and trends in time series data
import statsmodels.api as sm
from pylab import rcParams
rcParams['figure.figsize'] = 12, 5
decomposition = sm.tsa.seasonal_decompose(df, model='multiplicative', freq = 52)
#decomposition.plot()

plt.show()

