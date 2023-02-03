
def asd():
    import numpy as np
    from random import random,randint
    #board=np.zeros([20,20,20])
    #print(board)
    #initial coordinatels and velocities
    coordinates=[]
    nop=randint(1,10)
    print(nop)
    #every matrix in the parti matrix are the spatial coordinates(x,y,z) for generated points
    parti=np.zeros([nop,3]) #p1x,p1y, 
    velo=np.zeros([nop,3])
    # setting up the random velocities for points from maatrix parti
    print("Parti", parti, "Velo", velo)
    for i in range(nop):
        for j in range (3):
            z=random()
            z=z*20
            parti[i][j]=z
            v=random()
            v=(v*4)-2
            velo[i][j]=v
            
        
    print("Parti", parti)
    print("Velo", velo)
    trjfile=open("traj.xyz","w")
    # step new position
    #changing and writing down the positions of points in dependency of initial velocities
    for k in range(1000):
        print(nop,file=trjfile)
        print("Some comment",file=trjfile)
        for m in range(nop):
            print("Atom",parti[m][0],parti[m][1],parti[m][2],file=trjfile)

            for n in range(3):
                
                
                parti[m][n]=parti[m][n]+velo[m][n]
                if parti[m][n] >= 20:
                    parti[m][n]=parti[m][n]-20
                if parti[m][n] <= 0:
                    parti[m][n]=parti[m][n]+20
                
        print("Parti", parti)

        
        
        
    trjfile.close()
    
asd()

#vmd > pbc set {20 20 20} -all
#vmd > pbc box_draw


