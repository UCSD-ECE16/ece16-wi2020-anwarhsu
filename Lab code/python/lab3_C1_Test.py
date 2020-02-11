# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:58:21 2020

@author: Anwar
"""

import numpy as np

incoming_stream = b'1',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'2',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'3',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'4',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'5',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'6',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'7',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'8',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'9',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'1',b'0',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n'

string_buffer = []
data_array = np.array([])

def receive_data(incoming_stream):
    # Send start data
    while sample_number < 10:
        try:
            receive_sample(incoming_stream)
            sample_number += 1
        except(KeyboardInterrupt):
            # Send stop data 
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
            # Send stop data 
    return data_array

def calc_sampling_rate(data_array):
    diff = np.diff(data_array,axis = 0, n= 1)
    return np.mean(diff)

def receive_sample(incoming_stream):
    global string_buffer
    global data_array

    for incoming_byte in incoming_stream:
        s = incoming_btye.decode('utf-8')# read a byte from serial (remember to decode)
        if( s == '\n'):
            data_string = ''.join(string_buffer) #JOIN buffer 
            print(data_string)
            temp_data_array = np.fromstring(data_string, dtype = int, sep = ',')#string to np array
            if(data_array.size == 0): 
                data_array = temp_data_array
            else:
                data_array = np.vstack((data_array,temp_data_array))#vstack temp_data_array to end of data_array
        string_buffer = [] # reset string_buffer to []
        else:
            string_buffer.append(s) # append the new char to string_buffer

def main():
    ser = setup_serial(ser)
    data_array = receive_data(ser)
    calc_sampling_rate(data_array)
    ser.close()

