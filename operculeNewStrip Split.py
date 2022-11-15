#!/usr/bin/env python
# coding: utf-8

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

