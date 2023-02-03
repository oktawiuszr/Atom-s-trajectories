#! /usr/bin/python3
import pylab
import numpy as np
x=[4,8,12,29]
y=[8,0,8,4]
xc=[]
yc=[]
for o in np.arange(min(x),max(x),0.1):
	sio=0
	xc.append(o)
	for s in range(len(y)):
		pio=1
		for q in range(len(x)):
			if s!=q:
				pio=pio*((o-x[q])/(x[s]-x[q]))		
		sio=sio+pio*y[s]
	yc.append(sio)
print(yc)
print(xc)
pylab.plot(x,y,"bo",xc,yc,"r.")
pylab.show()
