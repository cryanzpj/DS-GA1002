"""
"""
import os.path
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as knn
from data_tools import *

plt.close("all")
plt.rcParams['xtick.major.pad']='8'
plt.rcParams['ytick.major.pad']='8'

### CHANGE PATH TO WHEREVER YOU SAVE THE DATA FILES ### 
dataset = np.loadtxt("seeds_dataset.txt")
raw_data_T = dataset[:,:-1]
labels = dataset[:,-1]

def ind_x_eq_val(x, val):
    return np.where(x==val)[0]

# Center the columns 
centered_data_T = raw_data_T - raw_data_T.mean(axis=0)
# Normalize each column (divide by maximum value)
data_T = centered_data_T  / np.abs(centered_data_T).max(axis=0)
data = np.transpose(data_T)

# Project onto two first principal components
u,s,v = np.linalg.svd(data)
s_v = u[:,0:2]
projections_1 = np.transpose(np.dot(data_T[ind_x_eq_val(labels,1),:] , s_v))
projections_2 = np.transpose(np.dot(data_T[ind_x_eq_val(labels,2),:] , s_v))
projections_3 = np.transpose(np.dot(data_T[ind_x_eq_val(labels,3),:] , s_v))



plt.figure(figsize=(12, 9))  
plt.scatter(projections_1[0,:], projections_1[1,:], s=80, c="blue", marker='+')
plt.scatter(projections_2[0,:], projections_2[1,:], s=80, c="red", marker='x')
plt.scatter(projections_3[0,:], projections_3[1,:], s=80, c="green", marker='o')


# Project onto two last principal components

s_v_2 = u[:,5:7]
projections_1_last = np.transpose(np.dot(data_T[ind_x_eq_val(labels,1),:] , s_v_2))
projections_2_last = np.transpose(np.dot(data_T[ind_x_eq_val(labels,2),:] , s_v_2))
projections_3_last = np.transpose(np.dot(data_T[ind_x_eq_val(labels,3),:] , s_v_2))



plt.figure(figsize=(12, 9))  
plt.scatter(projections_1_last[0,:], projections_1_last[1,:], s=80, c="blue", marker='+')
plt.scatter(projections_2_last[0,:], projections_2_last[1,:], s=80, c="red", marker='x')
plt.scatter(projections_3_last[0,:], projections_3_last[1,:], s=80, c="green", marker='o')
  

neigh = knn(n_neighbors=15)
neigh.fit(np.dot(data_T, s_v),labels)
Decision_Surface(np.dot(data_T, s_v), labels, neigh, cell_size=.05, surface=True, points=False)