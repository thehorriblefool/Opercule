#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
from datetime import datetime,timedelta


# In[10]:


#filename = ['LOG_2022_2_0_2022_02_06.CSV','deuxieme','troisieme']
filename = 'LOG_2022_2_0_2022_02_06.CSV'

No = []
Date = []
Time = []
Temp101 = []
pH101 = []


def readMyFile(filename):

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        i = 0
        for row in csvReader:
            if (i > 0):
                No.append(int(row[0]))
                Date.append(row[1])
                Time.append(row[2])
                Temp101.append(row[11])
                pH101.append(row[9])

                # Debugging information to confirm concatenation
                if (i<5):
                    print(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S"))
                    print (Temp101)
                    print (pH101)

                    # la prochaine ligne reste à finaliser!!!
                    #print(timedelta.total_seconds(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S")))
                # on pourrait faire: Time.append(datetime.strptime(row[1] + row[2], "%Y:%m:%d%H:%M:%S")
            else:
                myfileheader = row
                print("Skipping headers because i = 0")
            i = i + 1
        return No, Date, Time, Temp101  

print (readMyFile('LOG_2022_2_0_2022_02_06.CSV'))

#No, Date, Time, Temp101 = readMyFile('LOG_2022_2_0_2022_02_06.CSV')

#print (No[1:6])
#print (Date[1:6])
#print(Time[1:6]) 
#print(Temp101[1:6])

#try for loop instead. "Counter". i = 0. i = i + 1. how and where? i= 0 before loop. i = i+1 ?


# In[5]:


#import pandas as pd
from pandas import DataFrame


pd.read_csv('LOG_2022_2_0_2022_02_06.CSV')
data_frame = pd.read_csv('LOG_2022_2_0_2022_02_06.CSV')
df = data_frame
#print(type(data_frame))
print(data_frame.head)

#df.loc[] and df[iloc]
#first index selects rows, second index columns.
#df.at[]. df.iat. to acces a single value by row and column
df.iloc[:, [0, 1, 2, 11]]

#array = df.to_numpy()
#print (array)

#trouver la suite pour parler a array comme il faut


#arr = df.to_numpy()
#print (arr)
#trying to get tuples. ('a', 1)('b', 2)('c', 3)
#type(array)

from datetime import datetime

datetime.strptime("00:00:00", "%H:%M:%S")



# In[ ]:


x = []
y = []

with open(filename) as csvDataFile:
    plots = csv.reader(csvDataFile, delimiter=',')
    for row in plots :
        x.append(row[2])
        y.append(row[11])

plt.plot(x,y)
plt.title("water temperature in time")
plt.xlabel("time")
plt.ylabel("watertemp")
plt.show()


# In[ ]:


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
#import csv
#from matplotlib import pyplot as plt
#ceci donne un graphique..

#x=[]
#y=[]

#with open('LOG_2022_2_0_2022_02_06.CSV') as csvfile :
#    plots = csv.reader(csvfile, delimiter=',')
#    for row in plots :
#        x.append(row[2])
#        y.append(row[11])

#plt.plot(x,y)
#plt.title("water temperature in time")
#plt.xlabel("time")
#plt.ylabel("watertemp")
#plt.show()
#with open(filename) as csvDataFile:
#    csvReader = csv.reader(csvDataFile) 
#    for row in csvReader:
#        No.append(row[0])
#        Date.append(row[1])
#        Time.append(row[2])
#        Temp101.append(row[11])
#    return No, Date, Time, Temp101  
#with open(filename) as csvDataFile:
#    csvReader = csv.reader(csvDataFile) 
#    for row in csvReader:
#        No.append(row[0])
#        Date.append(row[1])
#        Time.append(row[2])
#        Temp101.append(row[11])
#    return No, Date, Time, Temp101  

