#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[71]:


def readMyFile(filename):
    No = []
    Date = []
    Time = []
    Temp101 = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile) 
        for row in csvReader:
            No.append(row[0])
            Date.append(row[1])
            Time.append(row[2])
            Temp101.append(row[11])
        return No, Date, Time, Temp101  

No, Date, Time, Temp101 = readMyFile('LOG_2022_2_0_2022_02_06.CSV')

print (No[1:6])
print (Date[1:6])
print(Time[1:6]) 
print(Temp101[1:6])

#try "counter" i = 0. i = i + 1. how and where? i= 0 before loop. i = i+1 ?


# In[ ]:




