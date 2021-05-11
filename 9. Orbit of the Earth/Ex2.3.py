# -*- coding: utf-8 -*-
"""
@author: JH_Song
"""
from scipy import array, arange, sqrt
from matplotlib import pyplot as plt

# Set constants and initial conditions
x_0 = 1.4710E+11
vx_0 = 0
y_0 = 0
vy_0 = 3.0287 * 10 ** 4 * 365 * 24 * 60 * 60  # velocity at perihelion in m/yearr
t_0 = 0
t_f = 5  # total time in years
h = 1 / 8760  # Step size (1 hour) in years
G = 6.6738E-11 * ( 365 * 24 * 60 * 60) ** 2
M = 1.9891E+30  # The mass of the Sun
m = 5.9722E+24  # The mass of the Earth


def f(r):
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    distance = sqrt(x ** 2 + y ** 2)
    return array([ vx, -G * M * x / distance ** 3, vy, -G * M * y / distance ** 3 ], float)

xpoints = []
ypoints = []
r = array([x_0, vx_0, y_0, vy_0], float)
mid = 0.5 * h * f(r)
vxmid = r[1] + mid[1]
vymid = r[3] + mid[3]
for t in arange(t_0, t_f, h):
    xpoints.append(r[0])
    ypoints.append(r[2])
    r[0] += h * vxmid
    r[2] += h * vymid
    k = h * f(r)
    vxmid += k[1]
    vymid += k[3]

#Plot orbit
plt.plot(xpoints, ypoints)
# plt.gca().set_aspect('equal', adjustable='box')
plt.plot(xpoints, ypoints)
plt.xlabel('x (m)')
plt.ylabel('y (m)') 
plt.show()



