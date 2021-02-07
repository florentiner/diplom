#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 23:07:49 2021

@author: danilezov
"""

from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import Birch
from matplotlib import pyplot as plt


import numpy as np

from matplotlib import pyplot

from sklearn.cluster import MeanShift


import hdbscan

import xlsxwriter

from numpy import where

import copy

from sklearn.cluster import DBSCAN

from sklearn.mixture import GaussianMixture



count = 999


lab_ar = []

'''

for file_n in range(1,3):
    
    
    data = np.loadtxt('test'+str(file_n)+'.txt', dtype=float)
    
    
    ar_x = []
    ar_y = []
        
        
    for i in range(len(data)):
        ar_x.append(data[i][0])
        ar_y.append(data[i][1])
    
            
    
            
    clustering = MeanShift(bandwidth=10).fit(data)
    lab = clustering.labels_
    plt.scatter(ar_x,ar_y,c=lab,cmap='rainbow')
            
    plt.pause(0.005)
    lab_ar.append(lab)
'''




data = np.loadtxt('a.txt', dtype=float)


clusterer = hdbscan.HDBSCAN(min_cluster_size=20,min_samples=1)
            
clusterer.fit(data)
            
lab = clusterer.labels_
            
print(lab)




#1 3 5 7 14

#1 5 7

'''

for file_n in range(1,3):
        
    data = np.loadtxt('test'+str(file_n) +'.txt', dtype=float)
    
    
    for ni in range(1,15):
        if ni in [1, 7]:
            print(ni)
            
            ar_x = []
            ar_y = []
            
            
            for i in range(len(data)):
                ar_x.append(data[i][0])
                ar_y.append(data[i][1])
            #8
            
                            
            clusterer = hdbscan.HDBSCAN(min_cluster_size=20,min_samples=ni)
                            
            clusterer.fit(data)
                            
            lab = clusterer.labels_
            
            lab1 = []
            
            ar_c = 'gist_ncar'
            
                            
            plt.scatter(ar_x,ar_y,c=lab,cmap=ar_c)
                        
            plt.pause(0.005)
            
            print(max(lab))
                    
                        
            lab_ar.append(lab)
            
'''  
'''

end_of_prog = lab_ar
workbook = xlsxwriter.Workbook('segmentation 2 mounths orig (HDBSCAN).xlsx')
# создаем там "лист"
worksheet = workbook.add_worksheet()
# в ячейку A1 пишем текст
worksheet.write('A1', 'ID')

for i in range(1,count+1):
    worksheet.write(i, 0, 'ID_' +str(i))

for i in range(len(end_of_prog)):
    for j in range(len(end_of_prog[i])):
        worksheet.write(j+1, 1+i ,end_of_prog[i][j] )
   
workbook.close()


'''





'''
data = np.loadtxt('a.txt', dtype=float)



#8


        
clusterer = hdbscan.HDBSCAN(min_cluster_size=2)
    
clusterer.fit(data)
    
lab = clusterer.labels_
    
print(lab)

'''