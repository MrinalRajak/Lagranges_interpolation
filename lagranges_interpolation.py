

#Lagranges interpolation

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def L(x):
    n=len(xs)
    m=np.empty_like(xs)
    for i in range(n):
        xi=xs[i]
        x_i=np.hstack((xs[: i],xs[i+1 :]))
        m[i]=np.product((x-x_i)/(xi-x_i))
    return np.sum(ys*m)
LL=np.vectorize(L)

# For discrete data points
'''
xs=np.array([0,1,3,4],dtype=float)
ys=np.array([5,6,50,105],dtype=float)
xx=np.linspace(5,11,7)
yy=LL(xx)
print(LL(2))
print(yy)
'''

# For many data points
xs=np.arange(-4,4.1,0.45)
ys=np.cos(xs)
xx=np.linspace(-4,4,100)
yy=LL(xx)
'''
plt.plot(xx,yy)
plt.scatter(xs,ys,c='r')
plt.show()
'''
# scipy scripts
t=np.linspace(-4,4.1,len(xs))
pxlagrange=lagrange(t,xs)
pylagrange=lagrange(t,ys)
fig,(ax0,ax1)=plt.subplots(nrows=2)
ax0.plot(xs,ys,'o',c='g')
ax0.plot(xx,yy,c='r')
ax0.set_title("Lagrange interpolation algorithm plot")
ax1.plot(xs,ys,'o',c='r')
ax1.plot(pxlagrange(t),pylagrange(t),c='blue')
ax1.set_title("Lagrange interpolation scipy module plot")
fig.subplots_adjust(hspace=0.4)
plt.show()

































