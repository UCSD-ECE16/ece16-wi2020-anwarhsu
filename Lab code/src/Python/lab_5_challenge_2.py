# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:33:42 2020

@author: Anwar
"""

import numpy as np
import matplotlib.pyplot as plt

data_array1 = np.genfromtxt('Data_01_075.csv', delimiter=',')
data_array2 = np.genfromtxt('Data_02_074.csv', delimiter=',')
data_array3 = np.genfromtxt('Data_03_073.csv', delimiter=',')
data_array4 = np.genfromtxt('Data_04_074.csv', delimiter=',')
data_array5 = np.genfromtxt('Data_05_080.csv', delimiter=',')
data_array6 = np.genfromtxt('Data_06_082.csv', delimiter=',')
data_array7 = np.genfromtxt('Data_07_087.csv', delimiter=',')
data_array8 = np.genfromtxt('Data_08_090.csv', delimiter=',')
data_array9 = np.genfromtxt('Data_09_98.csv', delimiter=',')
data_array10 = np.genfromtxt('Data_10_069.csv', delimiter=',')





plt.subplot(10,2,1)
plt.plot(data_array1[:,0],data_array1[:,4])

plt.subplot(10,2,2)
plt.psd(data_array1[:,4], NFFT=len(data_array1[:,0]), Fs=45) #plot the power spectral density


plt.subplot(10,2,3)
plt.plot(data_array2[:,0],data_array2[:,4])

plt.subplot(10,2,4)
plt.psd(data_array2[:,4], NFFT=len(data_array2[:,0]), Fs=45) #plot the power spectral density


plt.subplot(10,2,5)
plt.plot(data_array3[:,0],data_array3[:,4])

plt.subplot(10,2,6)
plt.psd(data_array3[:,4], NFFT=len(data_array3[:,0]), Fs=45) #plot the power spectral density


plt.subplot(10,2,7)
plt.plot(data_array4[:,0],data_array4[:,4])

plt.subplot(10,2,8)
plt.psd(data_array4[:,4], NFFT=len(data_array4[:,0]), Fs=45) #plot the power spectral density

plt.subplot(10,2,9)
plt.plot(data_array5[:,0],data_array5[:,4])

plt.subplot(10,2,10)
plt.psd(data_array5[:,4], NFFT=len(data_array5[:,0]), Fs=45) #plot the power spectral density

plt.subplot(10,2,11)
plt.plot(data_array6[:,0],data_array6[:,4])

plt.subplot(10,2,12)
plt.psd(data_array6[:,4], NFFT=len(data_array6[:,0]), Fs=45) #plot the power spectral density


plt.subplot(10,2,13)
plt.plot(data_array7[:,0],data_array7[:,4])

plt.subplot(10,2,14)
plt.psd(data_array7[:,4], NFFT=len(data_array7[:,0]), Fs=45) #plot the power spectral density


plt.subplot(10,2,15)
plt.plot(data_array8[:,0],data_array8[:,4])

plt.subplot(10,2,16)
plt.psd(data_array8[:,4], NFFT=len(data_array8[:,0]), Fs=45) #plot the power spectral density


plt.subplot(10,2,17)
plt.plot(data_array9[:,0],data_array9[:,4])

plt.subplot(10,2,18)
plt.psd(data_array9[:,4], NFFT=len(data_array9[:,0]), Fs=45) #plot the power spectral density

plt.subplot(10,2,19)
plt.plot(data_array10[:,0],data_array10[:,4])

plt.subplot(10,2,20)
plt.psd(data_array10[:,4], NFFT=len(data_array10[:,0]), Fs=45) #plot the power spectral density





plt.show()
