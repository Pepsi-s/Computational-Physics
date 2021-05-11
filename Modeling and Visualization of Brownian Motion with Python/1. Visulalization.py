# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:07:50 2021

@author: pepsi-s
"""

from __future__ import division, print_function
from numpy import arange
from vpython import *
import random as rnd

'''
Modeling and visulization of Brownian Motion [1/3]
visulalization of Brownian motion using vpython
'''

# Set up the square grid
L = 101 #Side length of the square grid

# Set the initial position of the particle (as a sphere object)
i = 50  # x-axis
j = 50  # y-axis

grid = canvas(title="Brownian Motion", 
              width=200, height=200, 
              center=vector(50,50,0), 
              background=color.black)

particle = sphere(pos=vec(i, j, 0), radius=0.3, color=color.red, make_trail=True)

tpoints = arange(0, 1, 1)
for t in tpoints:
    rate(5000) #Set the max animation rate
    # Use randint to generate random output
    go = rnd.randrange(4) 
    if go==0: 
        if i==L: continue
        i+=1  #Go right
    elif go==1:
        if i==0: continue
        i-=1  #Go left
    elif go==2:
        if j==L: continue
        j+=1  #Go up
    elif go==3:
        if j==0: continue
        j-=1  #Go down
    particle.pos=vec(i,j,0)
