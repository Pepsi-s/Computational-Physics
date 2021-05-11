# -*- coding: utf-8 -*-
"""
@author: pepsi-s
"""

from __future__ import division, print_function
from numpy import arange, zeros
import random as rnd
import matplotlib.pyplot as plt

'''
Modeling and visulization of Brownian Motion [3/3]
Direction probility verification
'''

# Use numpy arrays to hold displacement data 
countr = zeros((1,20), dtype=int)
countl = zeros((1,20), dtype=int)
countu = zeros((1,20), dtype=int)
countd = zeros((1,20), dtype=int)
value = zeros((1,20), dtype=float)
for i in range(1,21,1):
    value[0,i-1] = i

def randomwalk(right, left, up, down):
    for t in arange(0, 40, 1):
        # Use ranint to pick random integers
        go = rnd.randint(1,4) 
        if go==1: 
            right += 1
        elif go==2:
            left += 1
        elif go==3:
            up += 1
        elif go==4:
            down += 1
    return right, left, up, down

def decider(num):
    for n in range(20):
        if num <= (n + 1):
            countr[0,n] = countr[0,n] + 1
            break
        else:
            continue
        
def decidel(num):
    for n in range(20):
        if num <= (n + 1):
            countl[0,n] = countl[0,n] + 1
            break
        else:
            continue
        
def decideu(num):
    for n in range(20):
        if num <= (n + 1):
            countu[0,n] = countu[0,n] + 1
            break
        else:
            continue
        
def decided(num):
    for n in range(20):
        if num <= (n + 1):
            countd[0,n] = countd[0,n] + 1
            break
        else:
            continue

for iter in arange(0, 10000):
    a,b,c,d = randomwalk(0,0,0,0)
    decider(a)
    decidel(b)
    decideu(c)
    decided(d)

plt.plot(value, countr, 'ro'
         ,value, countl, 'bo'
         ,value, countu, 'y^'
         ,value, countd, 'g^')
plt.xlabel('n')
plt.ylabel('P(x)')
plt.show()
