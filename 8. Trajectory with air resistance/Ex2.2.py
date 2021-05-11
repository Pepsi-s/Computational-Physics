# -*- coding: utf-8 -*-
"""
@author: JH_Song
"""
from scipy import array, arange, pi, sin, cos, sqrt
from pylab import plot, show, xlabel, ylabel


# Set constants
g = 9.81 # Gravitational acceleration
m = 1 # Mass of the ball
radius = 0.08 # Radius of the ball
angle = 30 * pi / 180 # Shot angle in radians
v0 = 100 # Initial velocity
density = 1.22 # Density of air
drag = 0.47 # Drag coefficient

# Set values
t_0 = 0
t_drop = 6.6
h = (t_drop - t_0) / 1000 # step size


# Calculate the total constant
c = pi * radius ** 2 * density * drag / 2
constant = c / m

def f(r, t):
    vx = r[1]
    vy = r[3]
    v = sqrt(vx ** 2 + vy ** 2)
    return array([vx, - constant * vx * v, vy, - g - constant * vy * v], float)


xpoints = []
ypoints = []
r = array([0, v0 * cos(angle), 0, v0 * sin(angle)], float)
for t in arange(t_0, t_drop, h):
    xpoints.append(r[0])
    ypoints.append(r[2])
    
    # Apply RK4 method
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Plot the output
plot(xpoints, ypoints)

# Set the axis name
xlabel('x (m)')
ylabel('y (m)')
show()