#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
from datetime import datetime 


# In[3]:


path = "C:\data\LOG_2022_2_0_2022_02_06.CSV"
file = open(path, newline= '')
reader = csv.reader(file)
header = next(reader) #the first line in the header
data = []
for row in reader:
    count_number = int(row[0])
    t_c = float(row[11])
    
#time in minutes? :3
#a suivre...

#date = [] pass   #time = [] pass
#For example, datetime.timedelta(seconds=6010) will return 1 hour 40 minutes 10 seconds. Timedelta. pass
#no.
count_number = int(row[0])

#time
time = int(row[1])

#Temp101
t_c = float(row[11])

#pour l'instant, je peux mettre en relation count_number et t_c.
#faire graphique.




# In[ ]:




