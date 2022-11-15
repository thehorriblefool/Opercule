#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
import matplotlib as mpl
from matplotlib import pyplot as plt
import datetime
from datetime import datetime


# In[10]:


path = r'C:\Users\Administrateur\OneDrive\Bureau\Opercule_data\LOG_2022_2_0_2022_02_06.CSV'
with open(path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print (line)

print ()

#with open(path, 'w') as new_file:
#    fieldnames = ['Time', 'Temp101']
#    csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter= '\t')

#    for line in csv_reader:
#        csv_writer.writerow(line)

    
#    csv_writer.writeheader()   
#    for line in csv_reader:
#       csv_writer.writerow(line)       
#for line in csv_reader:          
# next(csv_reader)     
#for line in csv_reader:
#print(line)


# In[ ]:




