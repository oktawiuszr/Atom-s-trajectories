#! /usr/bin/python

x1=int(input("intert initial x"))
a = int(input ("isert a parameter"))
b = int(input("insert b parameter"))
m = int(input("insert m parameter"))
rand=[x1,]
for i in range (m):
    x1=(a*x1 + b)%m
    rand.append(x1)

print(rand)
period=[]

period=[k for l, k in enumerate(rand) if k not in rand[:l]]
print(period)
           
import matplotlib.pyplot as plt
plt.plot(period, ".",)
plt.xlabel('No. of number in period')
plt.ylabel('Value of random number')
plt.show()

plt.hist(period,bins=4)
plt.xlabel('Number of bins')
plt.ylabel('Number of values in bin')

plt.show()


