import math
import numpy as np
import matplotlib.pyplot as plt
a=9.8
h0=int(input('Plz enter the heightof the object from the ground befor projection: '))
v0=int(input('Plz enter the initial velocity in m/s: '))
theta_deg=int(input('Plz enter the angle of projection in degrees: ' ))
theta=theta_deg*math.pi/180
v0x=v0*math.cos(theta)
v0y=v0*math.sin(theta)
range=(2* (v0)**2 * math.sin(theta) * math.cos(theta))/a
max_height=((v0)**2 * math.sin(theta)**2)/(a*2)
t_of_flight=int(((v0)**2 * math.sin(theta)**2)/(a*2))

#y = (v0y/v0x )*x – gx2/2(v0cosθ0)2
#eqn
def proj(x):
    eqn= math.tan(theta)*x-(1*9.8*(x**2))/(2*((v0x)**2))
    return eqn
xlist=np.linspace(0,range,num=100)
ylist=proj(xlist)

plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist)
plt.show()