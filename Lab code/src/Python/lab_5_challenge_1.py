# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:59:30 2020

@author: Anwar
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

data_array = np.genfromtxt('appendix_a.csv', delimiter=',')#get data from Appendix A and save as .csv.


plt.subplot(3,2,(1,2))

fs = 50
filter_order = 3
filter_cutoff =  5 / (fs / 2)

b,a = signal.butter(filter_order, filter_cutoff, btype='low')
w, h = signal.freqz(b,a)
plt.plot(w, 20 * np.log10(abs(h)))



plt.subplot(3,2,3)
plt.plot(data_array[:,0],data_array[:,4])

plt.subplot(3,2,4)
plt.psd(data_array[:,4], NFFT=len(data_array[:,0]), Fs=fs)
plt.show()


plt.subplot(3,2,3)

b,a = signal.butter(filter_order, filter_cutoff, btype='low')
plt.plot(b,a)