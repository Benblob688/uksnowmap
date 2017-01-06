
# coding: utf-8

# In[2]:

import csv
import numpy as np


# In[10]:

# loop over each MO file
for fnum in range(12,15):
    input_file = str(fnum) + '.txt'
    # read in MO file
    rawdata = open(input_file).read().splitlines()
    for i in range(0,len(rawdata)):
        rawdata[i] = rawdata[i].split()
    # sort out data from MO file
    sortdata = np.zeros([len(rawdata),9])
    for row in range(0,len(rawdata)):
        for col in [0, 1, 2, 3, 4, 5, 6, 7, 10]:        
            if col==10:
                scol==8
            else:
                scol=col
            sortdata[row,scol] = rawdata[row][col]
    # simplify weather codes to 1/0 for yes/no snow
    for row in range(0,len(sortdata)):
        if 2<=sortdata[row,7]<=4 or sortdata[row,7]==6 or sortdata[row,7]==24 or sortdata[row,7]==146 or sortdata[row,7]==16 or sortdata[row,7]==134 or sortdata[row,7]==14 or sortdata[row,7]==12 or sortdata[row,7]==2346 or sortdata[row,7]==12346 or sortdata[row,7]==1234 or sortdata[row,7]==234:
            sortdata[row,7]=1
        else:
            sortdata[row,7]=0
    # write output sorted data for each MO file
    np.savetxt('Out'+str(fnum)+'.txt',sortdata,fmt='%10.0f',delimiter=',')



