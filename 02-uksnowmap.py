# 02-uksnowmap.py
# take MO files (name e.g. 11.txt), extract data and simplify

import csv
import numpy as np

# loop over each MO file
for fnum in range(11,37):
    input_file = srt(fnum) + '.txt'
    # read in MO file
    rawdata = open(input_file).read().splitlines()
    for i in range(0,len(rawdata)):
        rawdata[i] = rawdata[i].split()
    # sort out data from MO file
    sortdata = np.zeros([len(rawdata),7])
    for row in range(0,len(rawdata)):
        for col in [0, 1, 2, 3, 5, 6, 10]:        
            if col==10:
                scol==7
            else:
                scol=col
            sortdata[row,scol] = rawdata[row][col]
    # simplify weather codes to 1/0 for yes/no snow
    for row in range(0,len(sortdata)):
        if 2<=sortdata[row,6]<=4 or sortdata[row,6]==6:
            sortdata[row,6]=1
        else:
            sortdata[row,6]=0
    # write output sorted data for each MO file
    np.savetxt(str(fnum)+'.txt',sortdata,fmt='%10.0f',delimiter=',')

