#! /usr/bin/python3
x= [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5,]
y=[8.04, 6.95,7.58, 8.81, 8.33,9.96, 7.24, 4.26,10.84,4.82,5.68,]
y1=[9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]
y2=[7.46,6.77,12.72,7.11,7.81,8.84,6.08, 5.39,8.15,6.42,5.73]

def m_co(x,y): 
    n= len(x)
    s1=0
    s2=0
    s3=0
    s4=0
    for i in range(len(x)):
        s1=s1+x[i]*y[i]
        s2=s2+x[i]
        s3=s3+y[i]
        s4=s4+(x[i]**2)
    m=((n*s1)-(s2*s3))/((n*s4)-(s2**2))
    print(m)
    return m



def b_co(x,y,m):
    s1=0
    s2=0
    for i in range(len(x)):
        s1=s1+y[i]
        s2=s2+x[i]
        b=(s1- m*s2)/len(x)
    print(b)
    return b 

def trend(mx,bx):
	x_n=[]
	y_n=[]
	for f in range (0,100):
        
		p=f/4
		x_n.append(p)
		y_i=mx*(p)+bx
		y_n.append(y_i)
	return x_n, y_n

m=m_co(x,y)
b=b_co(x,y,m)


m1=m_co(x,y1)
b1=b_co(x,y1,m1)

m2=m_co(x,y2)
b2=b_co(x,y2,m2)



	
x_n, y_n = trend(m,b)
x_n1, y_n1 = trend(m1,b1)
x_n2, y_n2 = trend(m2,b2)
 
        
        
    
    



import pylab

title0="Trend line eq.: y= "+ str(round(m,3))+"x +"+str(round(b,3))


pylab.plot(x,y,"bo",x_n,y_n,"b-")
pylab.title(title0)
pylab.show()


title1="Trend line eq.: y= "+ str(round(m1,3))+"x +"+str(round(b1,3))
pylab.plot(x,y1,"bo",x_n1,y_n1,"b-")
pylab.title(title1)
pylab.show()


title2="Trend line eq.: y= "+ str(round(m2,3))+"x +"+str(round(b2,3))
pylab.plot(x,y2,"bo",x_n2,y_n2,"b-")
pylab.title(title2)
pylab.show()



    
    
