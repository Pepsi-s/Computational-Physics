# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:07:50 2021

@author: pepsi-s
"""

from numpy import arange
import random as rnd
from math import sqrt
import matplotlib.pyplot as plt

'''
Modeling and visulization of Brownian Motion [2/3]
Collect the displacement data for different steps
'''

x = []
y = []
def randomwalk(i, j):
    tpoints = arange(0, 400, 1)
    for t in tpoints:
        x.append(t)
        go = rnd.randint(1,4) # Use ranint to create random integers in {1, 2, 3, 4}
        if go==1: 
            i+=1  #Go right
        elif go==2:
            i-=1  #Go left
        elif go==3:
            j+=1  #Go up
        elif go==4:
            j-=1  #Go down
    displace = sqrt(i**2+j**2)
    y.append(displace)
    return displace

randomwalk(0,0)
print(x)
print(y)
plt.plot(x, y, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.show()