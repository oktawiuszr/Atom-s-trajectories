#!/usr/bin/python3

x1=230
a=40
b=78
m=911
rand=[]
period=[]
rand=[x1,]
for i in range (1500):
    x1=(a*x1 + b)%m
    rand.append(x1)

print(rand)

period=[k for l, k in enumerate(rand) if k not in rand[:l]]
print(period)


        # border value
        #border=int(sum(mylist)/len(mylist))
border=int(m/4)
print("Border is n times:", border, "Perio",len(period))
        #Creating the array
    
import numpy as np
board=np.zeros([20,20])

        

w=9
s=9
board[w][s]=board[w][s]+1
print(board)
for i in period:
	if i < border:
		if w==19:
			w=0
		board[w+1][s]=board[w+1][s]+1
		w=w+1
	elif i< 2*border:
            if w==0:
            	w=19
            board[w-1][s]=board[w-1][s]+1
            w=w-1
	elif i< 3*border:
		if s==0:
			s=19
		board[w][s-1]=board[w][s-1]+1
		s=s-1
	else:
		if s==19:
			s=0
		board[w][s+1]=board[w][s+1]+1
		s=s+1

            #print(np.sum(board))
            #print("WWW",w)

print(board)
import pylab as pl
pl.imshow(board)
pl.show()



