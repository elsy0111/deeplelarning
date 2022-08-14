import numpy as np
import matplotlib.pyplot as plt

limx = -5
minx = limx
maxx = 5

def f(x):
    y = (x-1)**2

    return y
def lim(x):
    h = 1e-4
    lim = (f(x + h) - f(x - h))/(2*h)
    return lim

def b(x):
    b = f(x) - (lim(x) * x)
    return b

def line(x,limx):   
    y = lim(limx) * x + b(limx)
    return y

x = np.arange(minx,maxx,0.01)
y = f(x)

while(limx < maxx):

    limx += 0.1
    y1 = line(x,limx)

    plt.xlim(minx,maxx)
    plt.ylim(-5,20)

    plt.plot(x,y1)
    plt.plot(x,y)

    plt.pause(0.01)
    plt.clf()