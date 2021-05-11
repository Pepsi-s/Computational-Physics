""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2018. 
    Please respect copyright & acknowledge our work."""

# PredatorPrey.py:     Lotka-Volterra models

from vpython import *
import numpy as np

from rk4Algor import rk4Algor
Tmin = 0.0;  Tmax = 500.0; Ntimes = 1000
y = np.zeros( (2), float)

y[0] = 2.0;  y[1] = 1.3   
h = (Tmax - Tmin)/Ntimes 
t = Tmin

def f( t, y):           #  Modify function for your problem
        F=np.zeros((2),float)
        F[0] = 0.2*y[0]*(1 - (y[0]/(20.0) )) - 0.1*y[0]*y[1]  
        F[1]  = - 0.1*y[1] + 0.1*y[0]*y[1];    
        return F    

f(0,y)           
   
graph1 = graph(width = 300, height = 300,
      title = 'Prey p & predator P vs time',xtitle = 't',
     ytitle = 'P, p',xmin=0,xmax=500,ymin=0,ymax=3.5)
funct1 = gcurve(color = color.magenta)
funct2 = gcurve(color = color.green)
graph2 = graph( width = 300, height = 300,
            title = 'Predator P vs prey p', xtitle = 'P',
            ytitle = 'p',xmin=0,xmax=2.5,ymin=0,ymax=3.5)
funct3 = gcurve(color = color.red)

for t in arange(Tmin, Tmax + 1, h):
    funct1.plot(pos = (t, y[0]) )
    funct2.plot(pos = (t, y[1]) )
    funct3.plot(pos = (y[0], y[1]) )
    rate(60) 
    y = rk4Algor(t,h,2,y,f)
