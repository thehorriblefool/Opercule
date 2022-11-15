#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
from matplotlib import pyplot as plt
#ceci donne un graphique..

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


# In[ ]:




