#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# data structure, arrays, hash tables, file manager
# keep track of the code and outputs, stored data, print (), memory location, indexes, debugger, 
# i = iteration. for loop. while loop. range. Counter. Breakpoint. python (search google). definite + indefinite iteration
# a = [ '...' , '...' , '...' ] . itr = iter(a) . itr2 = iter(a) . next(itr). generator function?
# import array as arr
# numpy, matplotlib, plot, matplotlib.dates
# dt = datetime
# weekdaylocator(),  DayLocator, Hour Locator. major locator? minor locator?  formatter. ticklabels. 
# rule = blahblahblah, loc = rrulelocator(rule). date tickers. autodatelocator. self.intervald = { [ ] }
# print(type(loc)) <type 'Locator'> print(loc())[1, 2, 3, 4]
# for i in range(len(day_load)):
# extract columns


# In[1]:


import csv

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

#try for loop instead. "Counter". i = 0. i = i + 1. how and where? i= 0 before loop. i = i+1 ?


# In[2]:


###to try####

#counter
#for loop. while loop. while i <= 4 or range (0,4)

#i =0 
#i + 1


#i = 0
#while i < 5:
#    print(i)
#    i = i + 1

#for i in range(4):
#print (i)
#break

#for i in range(4):
#print (i)
#break

# to try

