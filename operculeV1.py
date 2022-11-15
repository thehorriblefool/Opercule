#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv


# In[ ]:


path = "C:\data\LOG_2022_2_0_2022_02_06.CSV"
file = open(path)
for line in file:
    print(line)

lines = [line for line in open(path)]
lines[0]
lines[1]
lines[0].strip().split(',')
lines[1].strip()
dataset = [line.strip().split (' , ' )for line in open(path)]
dataset[0]
dataset[1]


# In[ ]:


#CSV file = text file. (all as a string).
#Strings, dates and numbers

#store the data

#convert data into the appropriate datatype
# ,, missing values
# reading
# analyze the data
# write the results of our analysis to a CSV file

#coder variable température
#coder for loop range
#code if elif elif elif elif elif elif elif elif else
#voir les écarts de température
#pourquoi
#quand
#faire un graphique 2D avec les données de température
#Socratica
#LabView

#Traiter plusieurs fichiers en même temps

#header = nom des variables. extraires les colonnes 'time' et 'Temp101'
#convertir heure (string) en heure (datetime) (index [1]) 
#extraire colonnes 'Time' et 'Temp101'(index[11])
#produire le graphique (plot)

# "C:\data\LOG_2022_2_0_2022_02_06.CSV"

#int No.
#int date
#int time
#LT101 = float   
#Unit = str     
#LT102 = float
#Unit = str
#LT103 = float
#Unit = str
#pH101 = float
#Unit = str
#Temp101 = float
#Unit = str
#O1RP101 = float
#Unit = str
#CO2101 = float
#Unit = str
#DO101_L = float
#Unit = str
#DO101_ER = float
#Unit = str
#DO102_ER = float
#Unit = str
#DO101_IR = float
#str    Unit
#DO102_IR = float
#str    Unit
#DO101_AR = float
#Unit = str
#DO102_AR = float
#Unit = str
#DO103_AR = float
#Unit = str

