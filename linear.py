from astroML.datasets import fetch_LINEAR_sample

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from astropy.time import Time

import os,sys

class LINEAR():

    def __init__(self, id = 10040133):
        self.LINEAR_data = fetch_LINEAR_sample()
        self.id = id
        self.t, self.mag, self.dmag = self.LINEAR_data.get_light_curve(self.id).T
    
    def plot_light_curve(self):
        fig = plt.figure(figsize=(12, 8))
        ax = plt.gca()

        plt.plot(self.t,self.mag,
                color='gray', 
                marker='o', 
                linestyle='dashed', 
                linewidth=2, 
                markersize=5)
        
        plt.grid()
        
        ax.set(xlabel='Observation time (days)', 
                ylabel='Observed Magnitude', 
                title='LINEAR object {0}'.format(self.id))
        return fig, ax
        # plt.show(block=False)
    
    def plot_atocorrelation_function(self):
        from astroML.time_series import ACF

        acf, asso_t = ACF.ACF_scargle(self.t, self.mag, self.dmag)
        acf = acf[1024:]
        asso_t = asso_t[1024:]
        
        print('Values of ACF:- ', acf, '\n times:-', asso_t)
        
        fig = plt.figure(figsize=(12, 8))
        ax = plt.gca()

        plt.plot(asso_t,acf)
        
        ax.set(xlabel='Associated Time Differences', 
                ylabel='Auto correlation function (ACF)')
        plt.grid()
        return fig, ax
        # plt.show(block=False)
    
    def plot_lomb_scargle(self):
        from astropy.stats import LombScargle

        ls = LombScargle(self.t, self.mag, self.dmag)
        frequency, power = ls.autopower()
        print('Maximum power: {}, occured at time period : {} '.format(max(power),1. / frequency[np.argmax(power)]))

        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('Lomb-Scargle Periodogram for LINEAR object {0}'.format(self.id))
        fig.subplots_adjust(bottom=0.12, left=0.07, right=0.95)

        # plot the raw data
        ax[0].plot(frequency, power)
        ax[0].set(xlabel='Frequency',ylabel='Lomb-Scargle Power')

        # plot the periodogram
        ax[1].plot(1. / frequency, power)
        ax[1].set(xlim=(0,100),xlabel='period (days)',ylabel='Lomb-Scargle Power')
        return fig, ax
        # plt.show(block=False)
    
    def plot_seasonality_trends(self):
        # conversion to datetime from MJD, in a dataframe
        data = {'time':self.t,'values':self.mag}
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
        decomposition.plot()

        plt.show(block=False)
    
def get_linear_id_list():
    data = fetch_LINEAR_sample()
    return data.ids

if __name__=='__main__':
    linear = LINEAR()
    linear.plot_light_curve()
    linear.plot_atocorrelation_function()
    linear.plot_lomb_scargle()

    plt.show()
            


