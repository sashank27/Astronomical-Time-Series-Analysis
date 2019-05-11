import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import fftpack
from matplotlib import mlab

from astroML.datasets import fetch_LIGO_large

class LIGO():

    def __init__(self):
        # Fetch the LIGO hanford data
        self.data, self.dt = fetch_LIGO_large()
        
        # subset of the data to plot
        t0 = 646
        T = 2
        self.tplot = self.dt * np.arange(T * 4096)
        self.dplot = self.data[4096 * t0: 4096 * (t0 + T)]

        #print(len(tplot))   #8192
        #print(len(dplot))   #8192

        self.tplot = self.tplot[::10]
        self.dplot = self.dplot[::10]

        #print(len(tplot))   #820
        #print(len(dplot))   #820

    def plot_data(self):
        # plot data
        fig = plt.figure(figsize=(12, 8))
        ax = plt.gca()
        ax.plot(self.tplot, self.dplot, '-k')
        ax.set_xlabel('time (s)')
        ax.set_ylabel('$h(t)$')

        ax.set_ylim(-1.2E-18, 1.2E-18)
        plt.grid()
        return fig, ax
        # plt.show(block=False)
    
    def plot_FFT(self, fmin = 40, fmax = 2060):
        # compute PSD using simple FFT
        
        N = len(self.data)
        df = 1. / (N * self.dt)
        PSD = abs(self.dt * fftpack.fft(self.data)[:(int)(N / 2)]) ** 2
        f = df * np.arange(N / 2)

        cutoff = ((f >= fmin) & (f <= fmax))
        f = f[cutoff]
        PSD = PSD[cutoff]
        f = f[::100]
        PSD = PSD[::100]

        print('Maximum power: {}, occured at time period : {} '
                .format(max(PSD),1. / f[np.argmax(PSD)]))

        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('FFT Periodogram')
        fig.subplots_adjust(bottom=0.12, left=0.07, right=0.95)

        # plot the raw data
        ax[0].loglog(f, PSD, '-')
        ax[0].set(xlabel='Frequency',ylabel='PSD')
        ax[0].set_xlim(40, 2060)
        ax[0].set_ylim(1E-46, 1E-36)
        ax[0].yaxis.set_major_locator(plt.LogLocator(base=100))

        # plot the periodogram
        ax[1].loglog(1. / f, PSD, '-')
        ax[1].set(xlabel='period (days)',ylabel='PSD')
        return fig, ax
        # plt.show(block=False)

    
    def plot_Welch_Periodogram(self, fmin = 40, fmax = 2060):
        PSDW2, fW2 = mlab.psd(self.data, NFFT=4096, Fs=1. / self.dt,
                    window=mlab.window_hanning, noverlap=2048)

        dfW2 = fW2[1] - fW2[0]

        cutoff = (fW2 >= fmin) & (fW2 <= fmax)
        fW2 = fW2[cutoff]
        PSDW2 = PSDW2[cutoff]
        print('Maximum power: {}, occured at time period : {} '
                .format(max(PSDW2),1. / fW2[np.argmax(PSDW2)]))
        
        # plot data
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('Welch-Method Periodogram')
        fig.subplots_adjust(bottom=0.12, left=0.07, right=0.95)

        # plot the raw data
        ax[0].loglog(fW2, PSDW2, '-')
        ax[0].set(xlabel='Frequency',ylabel='PSD')
        ax[0].set_xlim(40, 2060)
        ax[0].set_ylim(1E-46, 1E-36)
        ax[0].yaxis.set_major_locator(plt.LogLocator(base=100))

        # plot the periodogram
        ax[1].loglog(1. / fW2, PSDW2, '-')
        ax[1].set(xlabel='period (days)',ylabel='PSD')
        return fig, ax
        # plt.show(block=False)

    def plot_Lomb_Scargle_Periodogram(self):
        from astropy.stats import LombScargle

        ls = LombScargle(self.tplot, self.dplot)
        frequency, power = ls.autopower()
        print('Maximum power: {}, occured at time period : {} '
                .format(max(power),1. / frequency[np.argmax(power)]))
        
        # Lomb -Seargle Periodgram
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('Lomb-Scargle Periodogram')
        fig.subplots_adjust(bottom=0.12, left=0.07, right=0.95)

        # plot the raw data
        ax[0].plot(frequency, power)
        ax[0].set(xlabel='Frequency',ylabel='Lomb-Scargle Power')

        # plot the periodogram
        ax[1].plot(1. / frequency, power)
        ax[1].set(xlabel='period (days)',ylabel='Lomb-Scargle Power')
        return fig, ax
        # plt.show(block=False)
    
    def calculate_ACF(self, lags = None):
        from statsmodels.tsa.stattools import acf
        from statsmodels.graphics.tsaplots import plot_acf

        acf = acf(self.dplot)
        # print(acf)
        # print(len(acf))
        
        fig = plt.figure(figsize=(12, 8))
        ax=plt.gca()
        if lags is None:
            plot_acf(self.dplot, ax=plt.gca())
        else:
            plot_acf(self.dplot, ax=plt.gca(), lags = lags)
        
        return fig, ax
        # plt.show(block=False)
        # return acf
    
    def calculate_PACF(self, lags = None):
        from statsmodels.tsa.stattools import pacf
        from statsmodels.graphics.tsaplots import plot_pacf

        pacf = pacf(self.dplot)
        ax=plt.gca()
        # print(pacf)
        # print(len(pacf))
        
        fig = plt.figure(figsize=(12, 8))
        if lags is None:
            plot_pacf(self.dplot, ax=plt.gca())
        else:
            plot_pacf(self.dplot, ax=plt.gca(), lags = lags)
        
        return fig, ax
        # plt.show(block=False)
        # return pacf
    
    def arima(self,p = 0, d = 0, q = 0):
        from statsmodels.tsa.arima_model import ARIMA
       
        # fit model
        model = ARIMA(self.dplot, order=(p,d,q))
        model_fit = model.fit(disp=0)
        print(model_fit.summary())
        # plot residual errors
        fig = plt.figure(figsize=(12, 8))
        residuals = pd.DataFrame(model_fit.resid)
        ax=plt.gca()
        residuals.plot(ax = plt.gca())
        return fig, ax
        # plt.show()
        # residuals.plot(kind='kde')
        # plt.show()
        # print(residuals.describe())

    def arima_kde(self,p = 0, d = 0, q = 0):
        from statsmodels.tsa.arima_model import ARIMA
       
        # fit model
        model = ARIMA(self.dplot, order=(p,d,q))
        model_fit = model.fit(disp=0)
        print(model_fit.summary())
        # plot residual errors
        fig = plt.figure(figsize=(12, 8))
        residuals = pd.DataFrame(model_fit.resid)
        ax=plt.gca()
        residuals.plot(kind='kde', ax=plt.gca())
        return fig, ax
    
    def plot_seasonality_trends(self):
        # conversion to datetime from MJD, in a dataframe
        import pandas as pd
        from astropy.time import Time

        data = {'time':self.tplot,'values':self.dplot}
        df = pd.DataFrame(data)
        df = df.set_index('time')

        # Seasonality and trends in time series data
        import statsmodels.api as sm
        from pylab import rcParams
        fig = plt.figure(figsize=(12, 5))
        rcParams['figure.figsize'] = 12, 5
        decomposition = sm.tsa.seasonal_decompose(df, model='additive', freq = 1)
        ax=plt.gca()
        decomposition.plot(ax=plt.gca())
        return fig, ax
        # plt.show(block=False)
    

if __name__=='__main__':
    ligo = LIGO()
    ligo.plot_data()
    ligo.plot_FFT()
    ligo.plot_Welch_Periodogram()
    ligo.plot_Lomb_Scargle_Periodogram()
    ligo.calculate_ACF()
    ligo.calculate_PACF()
    ligo.arima(10,0,0)
    ligo.plot_seasonality_trends()
    
    plt.show()
            






