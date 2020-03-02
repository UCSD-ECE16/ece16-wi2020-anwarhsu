# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 20:59:35 2020

@author: Anwar
"""
from Libraries.Connection import Connection
from Libraries.Visualize import Visualize
from Libraries.Data import Data
from Libraries.Heartrate import Heartrate
import numpy as np



class Wearable:
    def __init__(self, serial_name, baud_rate):
        self.data = Data()
        self.connection = Connection('COM4', 115200)
        self.serial_name = serial_name
        self.baud_rate = baud_rate
       
        
        
    
            
    def collect_data(self, num_samples):
        #first make sure data sending is stopped by ending streaming
        self.connection.start_streaming()#start sending data
        while  self.connection.data.get_num_samples()< num_samples: #collect x samples
            try:
                self.connection.receive_data()#receive data
            except(KeyboardInterrupt):
                self.connection.close_connection #we'll use ctrl+c to stop the program
                print("Exiting program due to KeyboardInterrupt")
                break
        self.connection.end_streaming()#end streaming
    
    def main(self):
        self.collect_data(2250)
        
        
        data_array1 = np.genfromtxt('Data_10_069.csv', delimiter=',')
        
      
       
        data_temp = data_array1[:,4]
        data_temp = Heartrate.moving_average(self,s = data_temp,n_avg = 20)
        data_temp = Heartrate.normalize_signal(self,data_temp)
        data_array1[:,4] = data_temp
        
        print("Heart rate:",Heartrate.calc_heart_rate_time(self,signal = data_temp))

        Visualize.plotHr(data_array1)

              
        
        self.connection.close_connection()
            

def main():
    wearable = Wearable('COM4',115200)
    wearable.main()


if __name__== "__main__":
    main()


