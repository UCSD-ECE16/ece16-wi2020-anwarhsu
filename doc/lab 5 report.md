# ECE 16 Lab 5 report 
By: Anwar Hsu A15443752

Date: 02/29/2020

## Tutorial 

### Tutorial Frequency Domain:

> Q. If your sampling rate was 120Hz, what would be your maximum frequency (the Nyquist frequency)?

> A. 60 because 1/2 of the sampling frequency(120hz) = 60hz(Nyquist frequency)

> Q. If your signal bandwidth is composed of 0-10Hz, what is your minimum sampling rate to capture this signal based on the Nyquist sampling theorem? What would be recommended in general practice however?

> A. In theory our minimum sampling rate would be 20Hz(2times the sampling rate). However, in pratice, the we doint have perfect ideal filters in the real world, thus causing noise so its best to sample 4 times the sampling rate which would be 40hz. 