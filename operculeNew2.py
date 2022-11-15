#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
from datetime import datetime,timedelta
import json


# In[ ]:


filename = 'LOG_2022_2_0_2022_02_06.CSV''LOG_2022_2_0_2022_02_07.CSV''LOG_2022_2_0_2022_02_08.CSV'

No = []
Date = []
Time = []
Temp101 = []
pH101 = []

C02101 = 
ORP101 = [] 

LT101 =  []
LT102 = []
LT103 = []
 
DO101L = []
DO101_ER = []
DO102_ER = [] 
DO101_IR = []
DO102_IR = []
DO101_AR = []
DO102_AR = []
DO103_AR = []

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

                LT101.append(row[3])
                LT102.append(row[5])
                LT103.append(row[7])

                ORP101.append(row[13])
                CO2101.append(row[15])

                DO101L.append(row[17])
                DO101_ER.append(row[19])
                DO102_ER.append(row[21])

                DO101_IR.append(row[23])
                DO102_IR.append(row[25])

                DO101_AR.append(row[27])
                DO102_AR.append(row[29])
                DO103_AR.append(row[31])

                
                if (i<5):

                    print(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S"))
                    print(row[11])
                    print(row[3])
                    print(row[5])
                    print(row[7])
                    print(row[9])
                    print(row[13])
                    print(row[15])
                    print(row[17])
                    print(row[19])
                    print(row[21])
                    print(row[23])
                    print(row[25])
                    print(row[27])
                    print(row[29])
                    print(row[31])

                    #print(Time)
                    #print(datetime.date(int(row[1])), "%Y-%m-%d")
                    # on pourrait faire: Time.append(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S"))
                    #print(timedelta.total_seconds(datetime.strptime(row[1] + "-" + row[2], "%Y-%m-%d-%H:%M:%S")))
                    # Debugging information to confirm concatenation
            else:
                myfileheader = row
                i = i + 1
        return No, Date, Time, Temp101, pH101, LT101, LT102, LT103, ORP101, CO2101, DO101L, DO101_ER, DO102_ER, DO101_IR, DO102_IR, DO101_AR, DO102_AR, DO103_AR

print (readMyFile('LOG_2022_2_0_2022_02_06.CSV'))


#tdelta = timedelta = ??? row[2][3]-row[2][2] ???
#zip()
#enumerate()


# In[ ]:




