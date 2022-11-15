#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from datetime import datetime
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np


# In[2]:


path = r"C:\Users\Administrateur\OneDrive\Bureau\Opercule_data\LOG_2022_2_0_2022_02_06.CSV"


# In[3]:


file = open (path)


# In[4]:


for line in file:
    print(line)
    
#all string, no variables


# In[5]:


lines = [line for line in open(path)]


# In[6]:


lines[0]


# In[7]:


lines[1]


# In[8]:


dataset = [line.strip().split(',') for line in open(path)]


# In[9]:


dataset[0]


# In[10]:


#header = nom des variables. extraires les colonnes 'time' et 'Temp101'
#convertir heure (string) en heure (datetime) (index [1]) 
#extraire colonnes 'Time' et 'Temp101'(index[11])
#produire le graphique (plot)


# In[ ]:




