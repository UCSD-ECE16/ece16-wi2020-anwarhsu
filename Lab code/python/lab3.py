# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:38:06 2020

@author: Anwar
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:38:41 2020
@author: Anwar
"""
import numpy as np
import serial
import matplotlib.pyplot as plt


string_buffer = []
data_array = np.array([])
sample_number = 0


def setup_serial():
    serial_name = 'COM5'
    ser = serial.Serial(serial_name, 9600 )  # open serial port
    print(ser.name)         # check which port was really used
    return ser

def receive_data(ser):
    global sample_number# your code
    
# Send start data
    while sample_number < 100:
        try:
            receive_sample(ser)
        except(KeyboardInterrupt):
            # Send stop data 
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
    # Send stop data 
    send_serial_stop(ser)

    # at end of code:
    return data_array

def receive_sample(ser):
    global string_buffer
    global data_array
    global sample_number

    s = ser.read(1).decode('utf-8')# read a byte from serial (remember to decode)
    if( s == '\n'):
        data_string = ''.join(string_buffer) #JOIN buffer 
        print(data_string)
        temp_data_array = np.fromstring(data_string, dtype = int, sep = ',')#string to np array
        if(data_array.size == 0): 
            data_array = temp_data_array
        else:
            data_array = np.vstack((data_array,temp_data_array))#vstack temp_data_array to end of data_array
        sample_number += 1
        string_buffer = [] # reset string_buffer to []
    else:
        string_buffer.append(s) # append the new char to string_buffer


def calc_sampling_rate(data_array):
    #code to calculate sampling rate from data_array
    dff = np.diff(data_array, n =1, axis =0)
    mean = np.mean(dff, axis = 0)
    return (1000000 / mean[0]) 


def send_serial(ser):

 

    S_List = ['start',' data','\n']


    for S in S_List:
        ser.write(S.encode('utf-8'))
        
def send_serial_stop(ser):

 

    S_List = ['stop',' data','\n']


    for S in S_List:
        ser.write(S.encode('utf-8'))
        
def moving_average(s,n_avg):
    
    ma = np.zeros(s.size) #previously np.array(s.size) that was incorrect, sorry
    for i in np.arange(0,len(s)):
        ma[i] = np.mean(s[i:i+n_avg])#mean of s from index i to i+n_avg
    return ma

    
def detrend(s,n_avg): #remove the moving average from the signal
    ma = moving_average(s,n_avg)
    return s - ma#s minus the moving_average

def plot_data(data_array):
    
    time = data_array[:,0]
    x = data_array[:,1]
    y = data_array[:,2]
    z = data_array[:,3]
    IR = data_array[:,4]

    x = detrend(x,20)
    y = detrend(y,20)
    z = detrend(z,20)
    IR = detrend(IR,20)


    plt.clf()
    plt.subplot(411)
    plt.title('Example Data plot', fontsize=10)#plt.subplot(311)
    plt.plot(time,x) #fill in ax and ay
    plt.ylabel("x Amplitude")

    plt.subplot(412)
    plt.plot(time,y) #fill in bx and by
    plt.ylabel("y Amplitude")
    
    plt.subplot(413)
    plt.plot(time,z)
    plt.ylabel("z Amplitude")
    
    plt.subplot(414)
    plt.plot(time,IR)
    plt.ylabel("IR Amplitude")
    plt.xlabel(u'Time(${\mu}s$)')
    


def main():
    
    ser = setup_serial()
    send_serial(ser)
    data_array = receive_data(ser)
    print("sampling rate:", calc_sampling_rate(data_array))
    np.savetxt("data_file.csv", data_array, delimiter=",")
    data_array1 = np.genfromtxt('data_file.csv', delimiter=',')
    
    
    plot_data(data_array1)
    

       
    ser.close()

    
if __name__== "__main__":
    main()