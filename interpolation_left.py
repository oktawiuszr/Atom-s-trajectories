#! /usr/bin/python3
import math

import numpy

#function takes points described by list of coordinates(x,y), takes given x wh
def extrapol(v,x,y):

    yp=0
    for z in range(len(x)):
        p=1
        for i in range(len(x)):
                    
                    if z!=i:
                        p=p*((v-x[i])/(x[z]-x[i]))
        yp=yp+p*y[z]
        
        return yp

#set of initial data
x=[4,8,12,16]
y=[8,0,8,4]

x1=[]
y1=[]
for v in numpy.arange(4,16,0.1):
    x1.append(v)
    d=extrapol(v,x,y)
    y1.append(d)


print(x1)
print(y1)
import pylab
pylab.plot(x1,y1,"bo",x,y,"r.")
pylab.show() 
