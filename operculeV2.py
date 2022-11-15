#mettre en relation time et temp101
import csv
from matplotlib import pyplot as plt

path = 'LOG_2022_2_0_2022_02_06.CSV'
file = open(path, newline= '')
reader = csv.reader(file)

header = next(reader)
#data = []

print(header)
#print(row)


#watertemps = []
#times = []
#for row in reader:
#watertemp = row[11]
#time = row[2]

#watertemps.append(watertemp)
#times.append (time)

#print (watertemps)
#print (times)

#plt.plot()
#plt.ylabel(["11", "12", "13"])
#plt.show 



#name for x axis (heures 0 a 24)
#name for y axis ( temperature de l'eau 10 11 12 13 14)
#title of the graph



#for row in reader:
#    print (watertemp)
#    print (time)


#header = next(reader)
#data = []


#with open(path, 'r') as csvfile:
#       readCSV = CSV.reader(csvfile, delimiter= ',')
#        watertemp = []
#        time = []
#        for row in reader:


#row =['No.', 'Date', 'Time', 'LT101 ', 'Unit', 'LT102 ', 'Unit', 'LT103 ', 'Unit', 'pH101 ', 'Unit', 'Temp101 ', 'Unit', 'ORP101 ', 'Unit', 'CO2101 ', 'Unit', 'DO101_L ', 'Unit', 'DO101_ER ', 'Unit', 'DO102_ER ', 'Unit', 'DO101_IR ', 'Unit', 'DO102_IR ', 'Unit', 'DO101_AR ', 'Unit', 'DO102_AR ', 'Unit', 'DO103_AR ', 'Unit', 'ADMIN ', 'Unit', 'USER01 ', 'Unit', 'USER02 ', 'Unit', 'USER03 ', 'Unit', 'USER04 ', 'Unit', 'USER05 ', 'Unit', 'USER06 ', 'Unit', 'USER07 ', 'Unit', 'USER08 ', 'Unit', 'USER09 ', 'Unit', 'USER10 ', 'Unit']

#time_x = [time]
#temp101_y = [temperature]

#ok jusque reader = csv.reader(file) . header ok . data = [] ??? pense que oui. csv reader etc. non. 
#toutes les variables sont des strings. 
#on veut time et temp101 en float et  datetime.

#import csv
#from matplotlib import pyplot as plt #repetition juste pour moi. supprimer apres . 
#for future considerations  #from datetime import datetime ... currentDateAndTime = datetime.now()

#from datetime import datetime
#convertir les str en float et datetime

#with open(path, 'r') as opercule:
#   csv_reader = reader(opercule)
#   for row in reader:
#       blahblahbla. c est quoi ????
# 
