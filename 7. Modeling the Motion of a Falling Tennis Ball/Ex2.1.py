from math import sqrt
from numpy import arange, tanh, linspace
from matplotlib import pyplot as plt

# Set constants and initial condition
g = 9.8
D = 0.0245
vt = sqrt(g/D)

def fy(y,t1):
    return vt*tanh(-g*t1/vt)                                       #(1)
    
def fv(v,t2):
    return -g-D*(vt*tanh(-g*t2/vt))*abs((vt*tanh(-g*t2/vt)))       #(2)

# Set time range and step size
t_0 = 0.0  # Start of the interval
t_f = 10.0 # End of the interval
N = 1000   # Number of steps
h = (t_f - t_0) / N # Set step size

# Euler-Cromer method
euly = 2.0
eulv = 0.0
eula = -9.8
eult = 0.0
eultpoints = arange(t_0, t_f, h)
eulypoints = []
eulvpoints = []
eulapoints = []
for eult in eultpoints:
    eulapoints.append(eula)
    eula = -g-D*(eulv)*abs(eulv)
    
    eulypoints.append(euly)
    euly += h * fy(euly, eult)
    
    eulvpoints.append(eulv)
    eulv += h * fv(eulv, eult)
    
# Runge-Kutta 2nd order method
rk2y = 2.0
rk2v = 0.0
rk2a = -9.8
rk2t = 0.0
rk2tpoints = arange(t_0, t_f, h)
rk2ypoints = []
rk2vpoints = []
rk2apoints = []
for rk2t in rk2tpoints:
    rk2apoints.append(rk2a)
    rk2a = -g-D*(rk2v)*abs(rk2v)
    
    rk2ypoints.append(rk2y)
    rk_yt_k1 = h * fy(rk2y, rk2t)
    rk_yt_k2 = h * fy(rk2y + 0.5 * rk_yt_k1, rk2t + 0.5 * h)
    rk2y += rk_yt_k2
    
    rk2vpoints.append(rk2v)
    rk_vt_k1 = h * fv(rk2v, rk2t)
    rk_vt_k2 = h * fv(rk2v + 0.5 * rk_vt_k1, rk2t + 0.5 * h)
    rk2v += rk_vt_k2
    
#Leap-Frog method
leapy = 2.0
leapv = 0.0
leapa = -9.8
leapt = 0.0
leaptpoints = arange(t_0, t_f, h)
leapypoints = []
leapvpoints = []
leapapoints = []
for leapt in leaptpoints:
    leapapoints.append(leapa)
    leapa = -g-D*(leapv)*abs(leapv)
    
    leapypoints.append(leapy)
    leap_yt_k1 = h * fy(leapy, leapt)
    leap_yt_k2 = h * fy(leapy + 0.5 * leap_yt_k1, leapt + 0.5 * h)
    leap_yt_k3 = h * fy(leapv + leap_yt_k2, leapt + h)
    leapy += leap_yt_k3
  
    leapvpoints.append(leapv)
    leap_vt_k1 = h * fv(leapv, leapt)
    leap_vt_k2 = h * fv(leapv + 0.5 * leap_vt_k1, leapt + 0.5 * h)
    leap_vt_k3 = h * fv(leapv + leap_vt_k2, leapt + h)
    leapv += leap_vt_k3
    
#Analytical method
anay0 = 2.0
anav0 = 0.0
anat = linspace(0, t_f, N)
anav = vt*tanh(-g*anat/vt)
anaa = -g-D*anav*abs(anav)
anay = anay0 + 0.5*anaa*anat**2 + anav*anat

# Plots for Euler method
plt.subplot(3,1,1)
plt.plot(eultpoints, eulypoints)
plt.ylabel("y(t)")
plt.title("Plots for Euler method")
plt.subplot(3,1,2)
plt.plot(eultpoints, eulvpoints)
plt.ylabel("v(t)")
plt.subplot(3,1,3)
plt.plot(eultpoints, eulapoints)
plt.xlabel("t")
plt.ylabel("a(t)")
plt.show()

# Plots for RK2 method
plt.subplot(3,1,1)
plt.plot(rk2tpoints, rk2ypoints)
plt.ylabel("y(t)")
plt.title("Plots for RK2 method")
plt.subplot(3,1,2)
plt.plot(rk2tpoints, rk2vpoints)
plt.ylabel("v(t)")
plt.subplot(3,1,3)
plt.plot(rk2tpoints, rk2apoints)
plt.xlabel("t")
plt.ylabel("a(t)")
plt.show()

# Plots for Leap Frog method
plt.subplot(3,1,1)
plt.plot(leaptpoints, leapypoints)
plt.ylabel("y(t)")
plt.title("Plots for Leap Frog method")
plt.subplot(3,1,2)
plt.plot(leaptpoints, leapvpoints)
plt.ylabel("v(t)")
plt.subplot(3,1,3)
plt.plot(leaptpoints, leapapoints)
plt.xlabel("t")
plt.ylabel("a(t)")
plt.show()

# Plots for Analytical method
plt.subplot(3,1,1)
plt.plot(anat, anay)
plt.ylabel("y(t)")
plt.title("Plots for Analytical method")
plt.subplot(3,1,2)
plt.plot(anat, anav)
plt.ylabel("v(t)")
plt.subplot(3,1,3)
plt.plot(anat, anaa)
plt.xlabel("t")
plt.ylabel("a(t)")
plt.show()

# Comparsion of y(t)
plt.plot(eultpoints, eulypoints, label = 'Euler')
plt.plot(rk2tpoints, rk2ypoints, label = 'RK2')
plt.plot(leaptpoints, leapypoints, label = 'Leap Frog')
plt.plot(anat,anay, label = 'Analytical')
plt.title("Comparsion of y(t)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.show()

# Comparsion of v(t)
plt.plot(eultpoints, eulvpoints, label = 'Euler')
plt.plot(rk2tpoints, rk2vpoints, label = 'RK2')
plt.plot(leaptpoints, leapvpoints, label = 'Leap Frog')
plt.plot(anat, anav, label = 'Analytical')
plt.title("Comparsion of v(t)")
plt.xlabel("t")
plt.ylabel("v(t)")
plt.legend()
plt.show()

# Comparsion of a(t)
plt.plot(eultpoints, eulapoints, label = 'Euler')
plt.plot(rk2tpoints, rk2apoints, label = 'RK2')
plt.plot(leaptpoints, leapapoints, label = 'Leap Frog')
plt.plot(anat, anaa, label = 'Analytical')
plt.title("Comparsion of a(t)")
plt.xlabel("t")
plt.ylabel("a(t)")
plt.legend()
plt.show()






