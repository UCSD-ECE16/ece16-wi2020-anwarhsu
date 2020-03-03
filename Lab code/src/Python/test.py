# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:03:57 2020

@author: Anwar
"""


import numpy as np
import matplotlib.pyplot as plt

data_array = np.genfromtxt('appendix_a.csv', delimiter=',')#get data from Appendix A and save as .csv.


x = data_array[:,1]


ma = np.zeros(x.size) 
for i in np.arange(0,len(x)):
    ma[i] = np.mean(x[i:i+50])#mean of s from index i to i+n_avg
detrend_x = x - ma

    


t = data_array[:,0]#get the time array



plt.subplot(211)
Pxx, Freqs = plt.psd(x, NFFT=len(t), Fs=50)
print(np.argmax(Pxx))

plt.subplot(212)
plt.psd(x, NFFT=len(t), Fs=50)





plt.show()
