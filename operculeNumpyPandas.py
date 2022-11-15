#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
#dir (csv)
#help(csv)
import numpy as np
#dir(np)
#help(np)
import pandas as pd
#dir(pd)
#help(pd)
import matplotlib as mpl
#dir(mpl)
#help(mpl)
from matplotlib import pyplot as plt
#dir(plt)
#help(plt)
from datetime import datetime as dt
#dir(dt)
#help(dt)
import collections
#dir(collections)
#help(collections)
import array
#dir(array)
#help (array)


# In[3]:


# essayer avec DictReader. Numpy. #headers = fieldnames = fnames. writer.writerow({temp101: ' '}) or dictreader.
#fnames = ['first name', 'last name']
#iterator. list. iter() function. --> iterator object. keeps track of which item is next to be used in a loop.
#generator. 'yield' keyword. next(name_of_the generator) 
#def fancy_generator():
# my_list = [No, Date, Time, Temp101]
# for i in my_list:
# yield i +1  
# for i in fancy_generator():
# print(i)
#yield? marche pas plus.


# In[1]:


#import csv

#def readMyFile(filename):
#    No = []
#    Date = []
#    Time = []
#    Temp101 = []
#
#    with open(filename) as csvDataFile:
#        csvReader = csv.reader(csvDataFile) 
#        for row in csvReader:
#            No.append(row[0])
#            Date.append(row[1])
#            Time.append(row[2])
#            Temp101.append(row[11])
#        return No, Date, Time, Temp101  

#No, Date, Time, Temp101 = readMyFile('LOG_2022_2_0_2022_02_06.CSV')

#print (No[1:6])
#print (Date[1:6])
#print(Time[1:6]) 
#print(Temp101[1:6])

#try "counter" i = 0. i = i + 1. how and where? i= 0 before loop. i = i+1 ?


# In[ ]:


#panda as pd
#numpy as np
#code de reference
#dictReader
#col[]
#import csv


# In[5]:


def readMyFile(filename):
    No = []
    Date = []
    Time = []
    Temp101 = []

    with open(filename) as csvDataFile:
        csvReader = csv.DictReader(csvDataFile) 
        for col in csvReader:
            No.append(col[0])
            Date.append(col[1])
            Time.append(col[2])
            Temp101.append(col[11])
        return No, Date, Time, Temp101

#No, Date, Time, Temp101 = readMyFile('LOG_2022_2_0_2022_02_06.CSV')

print (No[1:6])
print (Date[1:6])
print(Time[1:6]) 
print(Temp101[1:6])

#try "counter" i = 0. i = i + 1. how and where? i= 0 before loop. i = i+1 ?
#print (headers). header(next). 


# In[86]:


#import pandas as pd
from pandas import DataFrame


pd.read_csv('LOG_2022_2_0_2022_02_06.CSV')
data_frame = pd.read_csv('LOG_2022_2_0_2022_02_06.CSV')
df = data_frame
#print(type(data_frame))
#print(data_frame.head)

#df.loc[] and df[iloc]
#first index selects rows, second index columns. df.at[]. df.iat. to acces a single value by row and column
df.iloc[:, [0, 1, 2, 11]]

array = df.to_numpy()
print (array)

#arr = df.to_numpy()
#print (arr)
#trying to get tuples. ('a', 1)('b', 2)('c', 3)


# In[ ]:


#import array as arr
 
# creating an array with integer type
#a = arr.array('i', [1, 2, 3])


# printing original array

#print ("The new created array is : ", end =" ")
#for i in range (0, 3):
#    print (a[i], end =" ")
#print()

# creating an array with double type

#b = arr.array('d', [2.5, 3.2, 3.3])
 
# printing original array

#print ("The new created array is : ", end =" ")
#for i in range (0, 3):
#    print (b[i], end =" ")


# In[ ]:




