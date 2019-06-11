#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:31:28 2019

@author: loukj.lenssen
"""

import random
import pandas as pd
#import matplotlib.pyplot as plt
#
#x1 = 1
#x2 = 2
#x3 = 3
#x4 = 4
#
#np.random.rand(x1, x2, x3, x4)
#
#vector_values = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
#np.random.choice(vector_values, 4, p=[0.7, 0.1, 0.1, 0.1, 0, 0, 0, 0, 0, 0])
#
#
vector_values = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20']
#np.random.choice(vector_values, np.random.random_integers(10), p=[0.7, 0.1, 0.1, 0.1, 0, 0, 0, 0, 0, 0])
#
#
#test = np.random.random_integers(0, high=10, size=1)
#np.random.random_integers(10)
#
#number_of_ones = 0
#number_of_zeros = 0

'''
STEP ONE. Draw a sample of size m and label the examples according to f.
PROCEED ACCORDINGLY
'''

#ASSIGN LABELS TO EACH OF THE ATTRIBUTES. DO THIS N TIMES (Depending of the size of the sample).
#THEN STORE THESE LABELINGS IN A DATAFRAME 
#THEN PROCEED WITH THE ALGORITHM 
def all_same(items):
    return all(x == items[0] for x in items)

#Create a dataframe with 20 attributes. 
#df = pd.DataFrame(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10'])
returned_hyp_df = pd.DataFrame(data=0, 
                             index=range(1), 
                             columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20', 'Error', 'Equal'])
sample_size = 50
row = 0
x = 10000
true_error_list = list()

while x > 0:
    print(x)
    df = pd.DataFrame(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20'])
    #Fill in the values of the dataframe according to the distribution
    for i in range(sample_size):
        for value in vector_values:
            if (random.random() >= 0.5):
                #print("Label 1 to {}".format(value))
                #number_of_ones = number_of_ones + 1
                #df = df.append({value: 1}, ignore_index=True)
                df.at[i, value] = 1
            else:
                #print("Label 0 to {}".format(value))
                #number_of_zeros = number_of_zeros + 1
                #df = df.append({value: 0}, ignore_index=True)
                df.at[i, value] = 0
        #print("Hypothesis {}".format(i))
    
    #print("The number of ones is: {}".format(number_of_ones))
    #print("The number of zeros is: {}".format(number_of_zeros))
    #df
    
    #Make a labeling according to the true f. 
    df['label'] = -1
    df['labeltwo'] = -1
    df['labelthree'] = -1
    df['labelfour'] = -1
    
    labeltwo = df['labeltwo']
    labelthree = df['labelthree']
    labelfour = df['labelfour'] 
    
    label = df['label']
    x_two = df['x2']
    x_four = df['x4']
    x_six = df['x6']
    x_eight = df['x8']
    
    #If x2=1 AND x4=0 AND x6=1 AND x8=1, then the labeling is correct. 
    for value in range(sample_size):
        if x_two[value] == 1:
            label[value] = 1
        else:
            continue
        
    for value in range(sample_size):
        if label[value] == 1 and x_four[value] == 0:
            labeltwo[value] = 1
        else:
            continue  
        
    for value in range(sample_size):
        if labeltwo[value] == 1 and x_six[value] == 1:
            labelthree[value] = 1
        else:
            continue    
        
    for value in range(sample_size):
        if labelthree[value] == 1 and x_eight[value] == 1:
            labelfour[value] = 1
        else:
            continue    
    
    #Remove all the intermediate labels. 
    df['label'] = labelfour    
    df = df.drop(columns=['labeltwo', 'labelthree', 'labelfour'])
    
    '''
    STEP 2. Pass the positive examples to the learning algorithm. If there are 
    no positive examples, skip the sample, and don’t increase the counter for n.
    PROCEED ACCORDINGLY
    '''
    
    #Store the positive labelings in a new dataframe
    df_positive = df.loc[df['label'] == 1]
    hypothesis_error_list = list() 
    #Loop over the rows of df_positive as individual series
    if len(df_positive) > 1:
        df_positive = df_positive.reset_index(drop=True)
        #print('Test')
        df_positive = df_positive.drop(columns=['label'])
            
        index = 0
        returned_hyp_df.loc[row] = row
        
        for i in range(20):
            column = df_positive.iloc[:,i]
            #print(column)
            #print(all_same(column))
            if all_same(column) == True and df_positive.iloc[0,i] == 1:
                #print('Yes')
                returned_hyp_df.iloc[row,index] = 1
                hypothesis_error_list.append(1)
            if all_same(column) == True and df_positive.iloc[0,i] == 0:
                returned_hyp_df.iloc[row,index] = 0
                hypothesis_error_list.append(0)
            elif all_same(column) == False:
                returned_hyp_df.iloc[row,index] = '?'
                
            #print(hypothesis_error_list) 
            #print(len(hypothesis_error_list)) 
            index = index + 1
        #row = row + 1 
        x = x - 1 
        
        if len(hypothesis_error_list) == 4:
            returned_hyp_df.loc[row,'Equal'] = 1
        else:
            returned_hyp_df.loc[row,'Equal'] = 0
        
        
        true_error = (0.5**4) - (0.5**len(hypothesis_error_list))
        returned_hyp_df.loc[row,'Error'] = true_error
        print(true_error)
        true_error_list.append(true_error)
        
    
        row = row + 1 
        
    elif len(df_positive) == 0:
        print('test')
        pass


#Results from a run with sample size 50 and 1000 runs. 
results_fifty = returned_hyp_df            
results_fifty.to_csv('fifty.csv', header = True)     



csv = pd.read_csv('fifty.csv') 

csv.loc[csv['Equal'] == 1]

csv.loc[csv['Error'] < 0.05]

csv['Error'].sum()/10000




    
