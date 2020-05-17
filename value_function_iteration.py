#This is a Python implementation of value function iteration.
#
#William Polley
#
#

#sets the working directory
import os
os.chdir('C:\\Users\\Bill Polley\\AppData\\Local\\Programs\\Python\\Python38-32\\projects\\Research\\value_function_iteration')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n=1
tolerance=.0001
alpha=.5
beta=.9
gridstep=.05
gridpoints=25
gridmin=gridstep
gridmax=gridpoints*gridstep
grid=np.linspace(gridmin,gridmax,num=gridpoints,endpoint=True)
kapital=grid
invest=grid
v=np.ones(gridpoints)

def value(k,old_v):
    count=0
    vprime=-999999*np.ones(gridpoints)
    for i in grid:
        if k**alpha-i>0:
            vprime[count]=np.log(k**alpha-i)+beta*old_v[count]
        count=count+1
    maxpoint=np.argmax(vprime)
    return(vprime[maxpoint])

while n>tolerance:
    next_v=np.ones(gridpoints)
    for j in range(gridpoints):
        next_v[j]=value(kapital[j],v)
    n=np.max(np.abs(next_v-v))
    v=next_v
print(v)
data = {'capital': grid, 'value function': v}
df = pd.DataFrame(data=data)
df.plot(x='capital',y='value function')
plt.savefig('plot.png')
