#!/usr/bin/env python
# coding: utf-8

# In[9]:


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


# In[11]:


path = r"C:\Users\Administrateur\Data Opercule\LOG_2022_2_0_2022_02_06.CSV"
file = open(path, newline='')
reader = csv.reader(file)
headers = next(reader)
data = [row for row in reader]

print(headers)
#all separate strings with variables. take this one.
#ca marche
print(data)
#all separate strings with variables. take this one. 
#ca marche.



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


print (No[1:6])
print (Date[1:6])
print(Time[1:6]) 
print(Temp101[1:6])


#NameError                                 Traceback (most recent call last)
#c:\Users\Administrateur\OneDrive\Bureau\opercule56789.ipynb Cell 2 in <cell line: 29>()
#     25             Temp101.append(col[11])
#     26         return No, Date, Time, Temp101
#---> 29 print (No[1:6])
#     30 print (Date[1:6])
#     31 print(Time[1:6]) 

#NameError: name 'No' is not defined



#try "counter" i = 0. i = i + 1. how and where? i= 0 before loop. i = i+1 ?
#print (headers). header(next).
#No, Date, Time, Temp101 = readMyFile('LOG_2022_2_0_2022_02_06.CSV')
 

#ceci donne un graphique. 
x=[]
y=[]

with open(r"C:\Users\Administrateur\OneDrive\Bureau\Opercule_data\LOG_2022_2_0_2022_02_06.CSV",'r') as csvfile :
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots :
        x.append(row[2])
        y.append(row[11])

plt.plot(x,y)
plt.title("water temperature in time")
plt.xlabel("time")
plt.ylabel("watertemp")
plt.show()


#Extract the rows/records. ...

#loc and iloc




#column = {}
#for h in headers:
#    column[h] = []
#    print(h)

#row = row[2]
#for line in row:
#    print (row)





#######
#np random seed . rapport ou pas? pas. same results without
#np.random.seed(0)


# In[ ]:




