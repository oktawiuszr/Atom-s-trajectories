#https://www.researchgate.net/publication/11612067_Kinetic_model_for_nitrogen-limited_wine_fermentations
#! /usr/bin/python3
#x y dy/dx
#0 1 1
#1 2 2
#2 4 4
#3 8 8

#Starting concentrations
nitrogen=0.15
cells=0.1
sugar=250

# coe

umax=0.16 #1/h
KN=0.01 # N/L
YXN=31 #gbiomas/g nitro
Bmax=0.3 #etanol/gsugar
KS=10 
YES=0.47 #g etanol/gsugar
kd0=0.0001 #l/g etaon h


# Xv - cell concentration
# E-etanol concentration
E=0
nitrogen1=[]
cells1=[]
sugar1=[]
ethanol1=[]
time=[]

for i in range(0,300):
    i=i/2
    u=((umax*nitrogen)/(KN+nitrogen))
    b=((Bmax*sugar)/(KS+sugar))

    dS=-(b*cells)/(YES)
    dS=dS/2
    dE=b*cells
    dE=dE/2
    dN=-(u*cells)/(YXN)
    dN=dN/2
    kd=kd0*E
    dcells=((u*cells)-(kd*cells))
    dcells=dcells/2
    nitrogen=nitrogen+dN
    sugar=sugar+dS
    E=E+dE
    cells=cells+dcells
    
    nitrogen1.append(nitrogen*1000)
    cells1.append(cells)
    sugar1.append(sugar)
    ethanol1.append(E)
    time.append(i)
    

print(nitrogen1)
print(cells1)
print(sugar1)
print(ethanol1)
print(time)
import pylab
pylab.plot(time,sugar1,"y.",time,nitrogen1,"g.",time,cells1,"b.",time,ethanol1,"r.")
pylab.show()
    


