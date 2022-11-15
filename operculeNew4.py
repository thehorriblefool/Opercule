import csv
import datetime as dt
from datetime import datetime, date, time, timedelta
from sqlite3 import Row
import numpy as np
import pandas
import matplotlib as mpl
from matplotlib import pyplot
from cycler import cycler
import sys
import itertools



path = r'C:\Users\davet\OneDrive\Documents\GitHub\Opercule-2\LOG_2022_2_0_2022_02_06.CSV'
file = open(path, newline='')
reader = pandas.read_csv(file)
data = [row for row in reader]
    print (file)

dataset = 



#header = next(reader)
#print (header)


#s = pandas.Series
#s.iloc(len)

#df = pandas.DataFrame (data, index, colums)
#df.iloc(0,0)
#df.head(data)


#pandas.DataFrame.columns
#for col in file.columns:
#   print (col)


#csv.DictReader(file)
#file = pd.read_csv(path)
