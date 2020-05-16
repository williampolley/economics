#This is a Python implementation of the HP Filter.
#It takes a .csv file as input.  By default, the data is assumed to NOT
#already be logged.  If the input data is in logs, simply change the code
#as indicated below.
#
#William Polley
#
#

#sets the working directory
import os
os.chdir('C:\\Users\\Bill Polley\\AppData\\Local\\Programs\\Python\\Python38-32\\projects\\Research\\hp_filter')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('Note: If your data is already in logs, you should modify the code so that the program does not take logs.')
print('Enter the name of a .csv file with data that you would like to detrend.')
fname=input('As a default, press \'enter\' to use the filename \'data.csv\': ')
if (len(fname) < 1): fname = 'data.csv'
data=pd.read_csv(fname)
labels=data.columns

#if you have already logged the data, change the 'x' to 'y' in the line below
#and comment out the line y=np.log(x)
x=data.iloc[:,1]
y=np.log(x)

#no meaningful trend if it is a small dataset
mdim=len(y)
if mdim<6:
    print('Are you sure there is a trend? (Small dataset)')
print('HP filtering the data...')

# Hodrick and Prescott recommend w=1600 for quarterly data.  Modify if necessary
w=1600

#set up the matrix
m=np.zeros((mdim,mdim))
mask=[w,-4*w,6*w+1,-4*w,w]
m[0,0]=w+1
m[0,1]=-2*w
m[0,2]=w
m[1,0]=-2*w
m[1,1]=5*w+1
m[1,2]=-4*w
m[1,3]=w
m[mdim-2,mdim-4]=w
m[mdim-2,mdim-3]=-4*w
m[mdim-2,mdim-2]=5*w+1
m[mdim-2,mdim-1]=-2*w
m[mdim-1,mdim-3]=w
m[mdim-1,mdim-2]=-2*w
m[mdim-1,mdim-1]=w+1
for i in range(mdim-4):
    m[i+2]=np.pad(mask,(i,mdim-5-i))
#calculate the trend, append the logged data, trend, and the detrended data
trend=np.dot(np.linalg.inv(m),y)
detrended=y-trend
#comment out the next line if data was already logged
data['Log of '+labels[1]]=y
data['Trend']=trend
data['Detrended '+labels[1]]=detrended
#write a .csv file with the detrended data and save a chart
data.to_csv('detrended_'+labels[1]+'.csv')
data.plot(x=data.columns[0], y=data.columns[4])
plt.savefig('detrended_'+labels[1]+'.png')
print('Output is in: '+'detrended_'+labels[1]+'.csv and '+'detrended_'+labels[1]+'.png')
