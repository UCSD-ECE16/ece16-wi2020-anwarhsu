# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:59:00 2020

@author: Anwar
"""
import numpy as np

def moving_average(s,n_avg):
    
    ma = np.zeros(s.size) #previously np.array(s.size) that was incorrect, sorry
    for i in np.arange(0,len(s)):
        ma[i] = np.mean(s[i:i+n_avg])#mean of s from index i to i+n_avg
    return ma

    
def detrend(s,n_avg): #remove the moving average from the signal
    ma = moving_average(s,n_avg)
    return s - ma#s minus the moving_average

def calc_heart_rate_time(signal,fs):
    count = 0
    state = 0 # add states to avoid multiple counts
    signal = detrend(signal,fs)#filter the signal to remove baseline drifting
    #filter the signal to remove high frequency noise
    norm_signal = normalize_signal(signal)#Normalize the signal between 0 and 1
    

        
    for i in norm_signal:
        
      
       
        if (state == 0): #if state = 0, it checks if threshold is reached
            if i >= 1:
                count += 1
                state = 1
        
        if i < 1: # if value is below threshold reset the state 
            state = 0
    
    
    return count * 6 #Calculate the beats per minute. 

def normalize_signal(signal):
    min = -800#find min of signal
    signal = signal - min#subtract the minimum so the minimum of the signal is zero
    max =1100#find the new maximum of the signal
    norm_signal = signal / max#divide the signal by the new maximum so the maximum becomes 1
    return norm_signal 

def main():
    
    signal = np.genfromtxt('Data_10_069.csv', delimiter=',')
    print("Heartrate:",calc_heart_rate_time(signal,10))
    
    
if __name__== "__main__":
    main()