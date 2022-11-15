#!/usr/bin/env python
# coding: utf-8

# In[108]:


import csv
from datetime import datetime
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
from cycler import cycler


# In[116]:


path = r"C:\Users\Administrateur\OneDrive\Bureau\Opercule_data\LOG_2022_2_0_2022_02_06.CSV"
file = open(path, newline='')
reader = csv.reader(file)


# In[117]:


header = next(reader)


# In[118]:


data = [row for row in reader]


# In[119]:


print(header)


# In[120]:


print(data[0])


# In[115]:


time = 


# In[102]:


time


# In[95]:


time


# In[94]:


data = []
for row in reader:
    time = datetime.strptime(row[2], format= %H:%M:%S)
    water_temp = float(row[11])


# In[28]:


data.append([Time, water_temp])


# In[ ]:




