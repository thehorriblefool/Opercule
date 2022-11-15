#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from datetime import datetime 

print(dir(csv))


# In[2]:


path = "C:\data\LOG_2022_2_0_2022_02_06.CSV"


# In[3]:


file = open(path, newline= '')


# In[4]:


reader = csv.reader(file)


# In[8]:


header = next(reader) #the first line in the header
data = []
    for row in reader:
        #
        
#row = [date, open, high, low, close, volume, adj.close]
    
#opercule rows = ['No.,Date,Time,LT101 ,Unit,LT102 ,Unit,LT103 ,Unit,pH101 ,Unit,Temp101 ,Unit,ORP101 ,Unit,CO2101 ,Unit,DO101_L ,Unit,DO101_ER ,Unit,DO102_ER ,Unit,DO101_IR ,Unit,DO102_IR ,Unit,DO101_AR ,Unit,DO102_AR ,Unit,DO103_AR ,Unit,ADMIN ,Unit,USER01 ,Unit,USER02 ,Unit,USER03 ,Unit,USER04 ,Unit,USER05 ,Unit,USER06 ,Unit,USER07 ,Unit,USER08 ,Unit,USER09 ,Unit,USER10 ,Unit']
    
    
#coder
    #no
    #date
    #time
    #Temp101

#pour la date:
#date = datetime.strptime(row[0], '%m/%d/%Y')

#pour l'heure: current. not for this immediate project.
#from datetime import datetime
#currentDateAndTime = datetime.now()
#print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2022-03-19 10:05:39.482383

#time: for this current project. opercule data. Date = none. (date dans le titre de fichier)
#time format: 00:00:00, 00:03:00, 00:06:00. then. Step : 00:03:00. Prise de donnees aux 3 minutes.

#hour
#datetime.hour
#In range(24).

#minutes
#datetime.minute¶
#In range(60).

#seconds
#datetime.second
#In range(60).

#microseconds
#datetime.microsecond
#In range(1000000).

#timedelta?
    

#int    No.
    
#date    Date
#time    Time
#float   LT101
#str     Unit
#float   LT102
#str     Unit
#float   LT103
#str     Unit
#float   pH101
#str     Unit
#float   Temp101 *****
#str     Unit
#float   O1RP101
#str    Unit
#float    CO2101
#str    Unit
#float    DO101_L
#str    Unit
#float    DO101_ER
#str    Unit,
#float    DO102_ER
#str    Unit
#float    DO101_IR
#str    Unit
#float    DO102_IR
#str    Unit
#float    DO101_AR
#str    Unit,
#float    DO102_AR
#str    Unit
#float    DO103_AR
#str    Unit

#users
    #ADMIN
    #Unit
    #USER01
    #Unit
    #USER02
    #Unit
    #USER03
    #Unit
    #USER04
    #Unit
    #USER05
    #Unit
    #USER06
    #Unit
    #USER07
    #Unit
    #USER08
    #Unit
    #USER09
    #Unit
    #USER10
    #Unit

#54 colonnes(variable, unit)
#still strings. convert each string into the appropriate data type. 


# In[ ]:




