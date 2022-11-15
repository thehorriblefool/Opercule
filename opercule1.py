#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from datetime import datetime
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


# In[4]:


path = r"C:\Users\Administrateur\OneDrive\Bureau\Opercule_data\LOG_2022_2_0_2022_02_06.CSV"
file = open(path, newline='')
reader = csv.reader(file)

data = [row for row in reader]
#all separate strings with variables. take this one.
print(data)
#all separate strings with variables. take this one. 

#headers = next(reader) #marche pas
#print(headers)

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

#sort un graphique, mais pas le bon. 

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




