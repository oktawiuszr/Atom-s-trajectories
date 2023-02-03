#! /usr/bin/python
import numpy as np
# for sin(x)
import math
import time 
def integral(a,b,h):
    for i in np.arange(a,b,h):
        inte=0
        if i==b:
            break
        inte=inte+((np.sin(i)+(np.sin(i+1))*h/2))
    exact=-np.cos(b)-(-np.cos(a))
    print(exact)
    print(inte)
    blad=abs((exact-inte)/exact)

    return blad

nstep=[]
errors=[]
time1=[]
h=0.1
for j in range (10):
	start = time.time()
	nstep.append(h)
	errors.append(integral(0,0.5*math.pi,h)*100)
	h=h/2
	end = time.time()
	time1.append(end-start)
	
print(nstep, errors)
import pylab
pylab.plot(nstep,errors,"r.")
pylab.title("Relative error [%]")
pylab.xlabel("step size")
pylab.ylabel("Value of error [%]")
pylab.show()
pylab.plot(nstep,time1,"b.")
pylab.title("Time[s]")
pylab.xlabel("step size")
pylab.ylabel("Time[s]")
pylab.show()


def integral2(a,b,h):
    for i in np.arange(a,b,h):
        inte=0
        if i==b:
            break
        inte=inte+((np.exp(i)+(np.exp(i+1))*h/2))
    exact=np.exp(b)-(np.exp(a))
    print(exact)
    print(inte)
    blad=abs((exact-inte)/exact)

    return blad

nstep2=[]
errors2=[]
time2=[]
h=0.1
for j in range (10):
	start2 = time.time()
	nstep2.append(h)
	errors2.append(integral2(0,10,h)*100)
	h=h/2
	end2 = time.time()
	time2.append(end2-start2)
print(nstep2, errors2)



pylab.plot(nstep2,errors2,"r.")
pylab.title("Relative error [%]")
pylab.xlabel("step size")
pylab.ylabel("Value of error [%]")
pylab.show()
pylab.plot(nstep,time2,"b.")
pylab.title("Time[s]")
pylab.xlabel("step size")
pylab.ylabel("Time[s]")
pylab.show()
