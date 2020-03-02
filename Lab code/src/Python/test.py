# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:03:57 2020

@author: Anwar
"""


import numpy as np
import matplotlib.pyplot as plt

data_array = np.genfromtxt('appendix_a.csv', delimiter=',')#get data from Appendix A and save as .csv.

#caculations for sampling rate in Hz
dff = np.diff(data_array, n =1, axis =0)
mean = np.mean(dff, axis = 0)
mean[0] = 1000000 / mean[0]
IR = data_array[:,3]


ma = np.zeros(IR.size) 
for i in np.arange(0,len(IR)):
    ma[i] = np.mean(IR[i:i+50])#mean of s from index i to i+n_avg
s = IR - ma

    


fs = mean[0]#sampling rate in Hz
t = data_array[:,0]#get the time array
s = data_array[:,1] #get the x-acceleration array


plt.subplot(211)
plt.plot(t, s)
plt.subplot(212)
Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs)

np.argmax(Pxx)



plt.show()
