import numpy as np
import csv

stationcode = []
easting = []
northing = []
for x in range(12,37):
    with open(x+'.txt', 'r') as statfile:
        weatherstationread = csv.reader(statfile, delimiter = '    ')
        for row in weatherstationread:
            stemp = row[3]
            etemp = row[?]
            ntemp = row[?]
            stationcode.append(stemp)
            easting.append(etemp)
            northing.append(ntemp)