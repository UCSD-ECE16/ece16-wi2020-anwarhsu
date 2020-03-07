# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:09:30 2020

@author: Anwar
"""
import glob
import numpy as np

all_files = glob.glob(r'C:\Users\Anwar\Documents\ECE16\ece16-wi2020-anwarhsu\Lab-code\src\Python\directory\traning_set\*.csv')

unique_ids = []

for index in range(len(all_files)):
    ind_file = (all_files[index].split("\\"))
    split = ind_file[-1].split("_")
    if split[0] not in unique_ids: 
        unique_ids.append(split[0])
    

list_data = []
list_sub = []
list_ref = []



for sub_id in unique_ids: 
    
    sub_files  = glob.glob(r'C:\Users\Anwar\Documents\ECE16\ece16-wi2020-anwarhsu\Lab-code\src\Python\directory\traning_set\%s?*.csv' % sub_id)
    
    for file in sub_files:
        
        temp_file = (file.split("\\") )
        data_array = np.genfromtxt(directory\traning_set\temp_file[-1], delimiter=',')
        
        
        #hr_data = #get the ppg signal from data using slicing
        #preprocess your hr_data:removing baseline, smooth your signal using a low pass filter and normalize. 
        #append the preprocessed data to list_data
        #append the subject id to list_sub
        #retrieve the reference heart rate from the filename.
        #append the reference heart rate to list_ref
