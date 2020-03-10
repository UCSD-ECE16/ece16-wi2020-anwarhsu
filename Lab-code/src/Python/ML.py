# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:09:30 2020

@author: Anwar
"""
import glob
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture as GMM
from scipy.stats import pearsonr



# all_files = glob.glob(r'C:\Users\Anwar\Documents\ECE16\ece16-wi2020-anwarhsu\Lab-code\src\Python\directory\traning_set\*.csv')
all_files = glob.glob('traning_set\*.csv')

unique_ids = []


def signal_diff(s):
        s_diff = np.diff(s,1,0)
        s_diff = np.append(s_diff, 0) #np.diff returns one shorter, so need to add a 0
        return s_diff
    


fs = 50
filter_order = 3
filter_cutoff = 5 / (fs / 2) 




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
        
        print(temp_file[-1])
        data_array = np.genfromtxt(temp_file[-1], delimiter=',')
        
        HR = data_array[:,4] #get the ppg signal from data using slicing
        HR = HR[0:500]
        
        t = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
        t = t[0:500]
        #preprocess your hr_data:removing baseline, smooth your signal using a low pass filter and normalize. 
        s_diff = signal_diff(-HR) #remove baseline
        
        
        fc = 5  # Cut-off frequency of the filter
        w = fc / (fs / 2) # Normalize the frequency
        b, a = signal.butter(5, w, 'low')
        output = signal.filtfilt(b, a, s_diff)
       
        norm_signal = (output - np.min(output))/(np.max(output)-np.min(output)) #normalize signal
        
        list_data.append(norm_signal)#append the preprocessed data to list_data
        
        list_sub.append(sub_id) #append the subject id to list_sub
        
        #retrieve the reference heart rate from the filename.
        hr_file = temp_file[-1]
        reference_HR = hr_file[6:9]
        
        
        #append the reference heart rate to list_ref
        list_ref.append(int(reference_HR))
        
        

train_data = np.empty(0)#make empty numpy array of size 0

hold_out_data = np.empty(0)#make empty numpy array of size 0

list_data = np.array(list_data)

hold_out_subject = list_sub[0] #for now we’ll hold out the first training subject


for ind, sub_id in enumerate(list_sub, start = 0):#enumerate the list_sub starting at 0. Look up enumerate function
  
    if(sub_id != hold_out_subject):#sub_id is not the same as hold_out_subject) 
        if(train_data.shape[0] == 0):
            train_data = list_data[ind]
        else:
            train_data = np.vstack((train_data,list_data[ind]))#concatenate numpy array train_data with the list_data at ind
    
    else:
        if(hold_out_data.shape[0] == 0):
            hold_out_data = list_data[ind]  
        else:
            hold_out_data = np.vstack((hold_out_data,list_data[ind]))#concatenate numpy array hold_out_data with list_data at ind

gmm_data = np.empty(0)

for i in range(0,10):


    gmm = GMM(n_components = 2).fit(train_data.reshape(-1,1))        
    test_pred = gmm.predict(hold_out_data[i].reshape(-1,1))
    
    
    if (gmm_data.shape[0] == 0):
        gmm_data = np.array(test_pred)
    else:
        gmm_data = np.vstack((gmm_data,np.array(test_pred)))

"""gmm = GMM(n_components = 2).fit(train_data.reshape(-1,1))        
test_pred = gmm.predict(hold_out_data[4].reshape(-1,1))

plt.plot(test_pred)
plt.plot(hold_out_data[4])"""

print(list_ref[0:10])
heartrate = []

state = 0
for i in gmm_data:
    count = 0

    for j in i:
        if j == 1 and state == 0:
            count += 1
            state = 1
        if state == 1 and j == 0:
            state = 0
    heartrate.append((count -1) * 6)


#np.savetxt('heart.csv', heartrate, delimiter = ',')



    
    
    
    