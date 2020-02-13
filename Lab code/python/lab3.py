# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:38:41 2020

@author: Anwar
"""
import numpy as np
import serial


string_buffer = []
data_array = np.array([])
sample_number = 0


def setup_serial():
    serial_name = 'COM5'
    ser = serial.Serial(serial_name, 460800 )  # open serial port
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
    return (mean[0]) 


def send_serial(ser):

 

    S_List = ['start',' data','\n']


    for S in S_List:
        ser.write(S.encode('utf-8'))
        
def send_serial_stop(ser):

 

    S_List = ['stop',' data','\n']


    for S in S_List:
        ser.write(S.encode('utf-8'))

def main():
    ser = setup_serial()
    send_serial(ser)
    data_array = receive_data(ser)

    print("sampling rate:", calc_sampling_rate(data_array))
    ser.close()
    
if __name__== "__main__":
    main()

