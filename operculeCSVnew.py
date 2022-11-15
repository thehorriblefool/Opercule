#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import csv
import datetime
from datetime import date, datetime, timedelta
from dateutil import parser
import matplotlib as mpl
from matplotlib import pyplot as plt
import plotly
import pendulum

import numpy as np

import pandas as pd
#import arrow
import pendulum

import pyarrow
from pyarrow import csv
import array as arr #try.

#import re
#import cycler
#import re
#import io

pyarrow



# In[2]:


pyarrow.csv.read_csv(r"C:\Users\davet\OneDrive\Bureau\Data & Python Files -  Opercule - My project\LOG_2022_2_0_2022_02_06.CSV")


# In[ ]:





# In[87]:


n = []
date = []
time = []
temp = []
pH = []


def readMyFile(file):

    with open(file) as csvDataFile:
        csvReader = pd.read_csv(csvDataFile)
        #csv.reader(csvDataFile)
        i = 0
        for col in csvReader:
            #if (i > 0):
            n.append(col[0])
            date.append(col[1])
            time.append(col[2])
            temp.append(col[3])
            pH.append(col[4])
            
            print(col[1] + "-" + col[2])
            print (col [0])
            print (col[3])
            print (col [4])
            
            return n, date, time, temp, pH
        
        print (readMyFile('LOG_2022_2_0_2022_02_06.CSV'))

            
            #(datetime.datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S"))
                
            #if (i<6):
            #    print(row[1] + "-" + row[2])
            #    #(datetime.datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S"))
            #    print (temp)
            #    print (pH)

            #else:
            #    row = header
            #    print("Skipping headers because i = 0")
            #i = i + 1
            
            
            
            #print (temp)
            #print (pH)
          


# In[ ]:


x = []
y = []
    
with open(file) as csvDataFile:
    plot = pd.read_csv(csvDataFile, delimiter=',')
for row in plot :
    x.append(row[2])
    y.append(row[11])

plt.plot(x,y)
plt.title("water temperature in time")
plt.xlabel("time")
plt.ylabel("watertemp")

plt.show(my_plot)


# In[ ]:


def readMyFile(file):

    with open(file) as csvDataFile:
        csvReader = pd.read_csv(csvDataFile)
        #csv.reader(csvDataFile)
        i = 0
        for row in csvReader:
            if (i > 0):
                n.append(row[0])
                d.append(row[1])
                t.append(row[2])
                #temp101.append(row[11])
                #pH.append(row[9])
                
                if (i<6):
                    print(datetime.datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S"))
                    print (temp101)
                    print (pH)

            else:
                row = header
                print("Skipping headers because i = 0")
            i = i + 1
        return No, Date, Time, Temp101, pH101  
print (readMyFile('LOG_2022_2_0_2022_02_06.CSV'))


x = []
y = []
    
with open(file) as csvDataFile:
    plot = pd.read_csv(csvDataFile, delimiter=',')
for row in plot :
    x.append(row[2])
    y.append(row[11])

plt.plot(x,y)
plt.title("water temperature in time")
plt.xlabel("time")
plt.ylabel("watertemp")

plt.show(my_plot)


# In[ ]:


#try something like this:

import time
import datetime
import calendar

for k, line in enumerate(lines):
                if k > (int(header_line)):
                    data_pre = line.strip().split(',')
                    stDate = data_pre[0].replace("\"", "")
                    print stDate  # got 1998-04-18 16:48:36.76


                    dat_time = datetime.datetime.strptime(stDate,
                                                       '%Y-%m-%d %H:%M:%S.%f')
                    mic_sec = dat_time.microsecond
                    timcon = calendar.timegm(dat_time.timetuple())*1000000 + mic_sec
                    strDate = "\"" + strDate + "\""
                    print stDate # got "1998-04-18 16:48:36.76"




#df['date_int'] = df.date.astype(np.int32)



#t1 = pa.int32()

#t2 = pa.string()

#t3 = pa.binary()

#t4 = pa.binary(10)

#t5 = pa.timestamp('ms')

#t1
#Out[7]: DataType(int32)

#print(t1)
#int32

#print(t4)
#fixed_size_binary[10]

#print(t5)
#timestamp[ms]





#pd.to_datetime(pd.Series(d), format='%y-%m-%d-%H:%m :%S%z')
#"%Y-%m-%d-%H:%M:%S"
#type(t)
#type(d)

#dataset = '2022-06-02T10:00:00Z'
#date = parser.parse(d,t)

#pandas.read_csv(file)
#data_frame = pandas.read_csv(file)
#df = data_frame
#df.iloc[:, [0, 1, 2, 11]]

#print(type(df))

#array = df.to_numpy()
#print (array)
#print(df.head)

#from datetime import datetime
#datetime.strptime("00:00:00", "%H:%M:%S")

#pd.Series
#t.date(year, month, day)
#d.time(hour, minute, second)

#pd.DataFrame(dict) | 
# From a dict, keys for columns names, values for data as lists ## 
# Exporting Data

#df.to_csv(filename) | 
# Write to a CSV file

#pd.Series(my_list) |
# Create a series from an iterable my_list 

# df.index = pd.date_range('1900/1/30', periods=df.shape[0]) | Add a date index ## Viewing/Inspecting Data

#df.head(n) | 
# First n rows of the DataFrame

#df.shape | 
# Number of rows and columns df.info() 

#df.describe()
#Index, Datatype and Memory information df.describe() | 
# Summary statistics for numerical columns s.value_counts(dropna=False) |
# View unique values and counts df.apply(pd.Series.value_counts) |
# Unique values and counts for all columns ## Selection

#import numpy as np
 
#arr = np.array([[1, 13, 6], [9, 4, 7], [19, 16, 2]])
 
# Access the ith column of a 2D NumPy array
#col = [row[1] for row in arr]
 
# printing the column
#print(col)


#import numpy as np
 
# defining array
#array = [[1, 13, 6], [9, 4, 7], [19, 16, 2]]
 
# converting to numpy array
#arr = np.array(array)
 
#print('selecting 0th column')
#print(arr[..., 0])
 
#print('selecting 1st row')
#print(arr[1, ...])


#import csv
#p = csv.parser()
#file = open("afile.csv")
#while 1:
#   line = file.readline()
#    if not line:
#        break
#    fields = p.parse(line)
#    if not fields:
#        # multi-line record
#        continue
    # process the fields
#path = r"C:\Users\davet\OneDrive\Bureau\Data & Python Files -  Opercule - My project\LOG_2022_2_0_2022_02_06.CSV"
#file = open(path, newline='')
#
#header = next(reader)
#data = [row for row in reader]
#print(header)

#dataset = (data[0:479])
#print (dataset)

#
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




#NewOpercule

#import csv
#from datetime import datetime,timedelta

#filename = ['LOG_2022_2_0_2022_02_06.CSV','deuxieme','troisieme']
#filename = 'LOG_2022_2_0_2022_02_06.CSV'


#Output
#
# Skipping headers because i = 0
# 2022-02-06 00:00:00
# ['12.84']
# ['7.51']

#2022-02-06 00:03:00
#['12.84', '12.84']
#['7.51', '7.50']

#2022-02-06 00:06:00
#['12.84', '12.84', '12.84']
#['7.51', '7.50', '7.50']

#2022-02-06 00:09:00
#['12.84', '12.84', '12.84', '12.84']

#['7.51', '7.50', '7.50', '7.50']
#([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
#14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, etc.

#--


#peps comments
# Debugging information to confirm concatenation
# la prochaine ligne reste à finaliser!!!
#print(timedelta.total_seconds(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S")))
# on pourrait faire: Time.append(datetime.strptime(row[1] + row[2], "%Y:%m:%d%H:%M:%S")

#No, Date, Time, Temp101 = readMyFile('LOG_2022_2_0_2022_02_06.CSV')

#print (No[1:6])
#print (Date[1:6])
#print(Time[1:6]) 
#print(Temp101[1:6])

#try for loop instead. "Counter". i = 0. i = i + 1. how and where? i= 0 before loop. i = i+1 ?

#datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S"))
  
#(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-	%H:%M:%S"))

#            else:
#                myfileheader = row
#                i = i + 1
#        return No, Date, Time, Temp101, pH101, LT101, LT102, LT103, ORP101, CO2101, DO101L, 	DO101_ER, DO102_ER, DO101_IR, DO102_IR, DO101_AR, DO102_AR, DO103_AR

#print (readMyFile('LOG_2022_2_0_2022_02_06.CSV'))


                    #print(Time)
                    #print(datetime.date(int(row[1])), "%Y-%m-%d")

                    # on pourrait faire: Time.append(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-	%H:%M:%S"))
                    #print(timedelta.total_seconds(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d	-%H:%M:%S")))
                    # Debugging information to confirm concatenation
 

#df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
#df.set_index('time', inplace=True)

# plotting
#df.plot()

#r"C:\Users\davet\OneDrive\Bureau\Data & Python Files -  Opercule - My project\LOG_2022_2_0_2022_02_06.CSV"))
    
#for row in reader:
#    time = datetime.strptime(row[2], format= %H:%M:%S)
#    water_temp = float(row[11])

#def convertTime(s):
#    tm = time.strptime(s, "%H:%M:%S")
#    return datetime.datetime.strptime(tm.tm_hour, tm.tm_min, tm.tm_sec)


#AttributeError: 'method_descriptor' object has no attribute 'strptime'

#df.loc[] and df[iloc]
#first index selects rows, second index columns.
#df.at[]. df.iat. to acces a single value by row and column


#trouver la suite pour parler a array comme il faut
#arr = df.to_numpy()
#print (arr)
#trying to get -s. ('a', 1)('b', 2)('c', 3)
#type(array)

