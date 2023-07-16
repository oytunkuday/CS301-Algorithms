import time

import numpy as np
import matplotlib as plt

start_time = time.time()

def lcsm(X,Y,i,j):
    
    if c[i][j] >= 0:
        return c[i][j]
    if (i == 0 or j == 0):
        c[i][j] = 0
    elif X[i-1] == Y[j-1]:
        c[i][j] = 1 + lcsm(X,Y,i-1,j-1)
    else:
        c[i][j] = max(lcsm(X,Y,i,j-1),lcsm(X,Y,i-1,j))
    return c[i][j]


def lcs(X,Y,i,j):
    if (i == 0 or j == 0):
        return 0
    elif X[i-1] == Y[j-1]:
        return 1 + lcs(X,Y,i-1,j-1)
    else:
        return max(lcs(X,Y,i,j-1),lcs(X,Y,i-1,j))


X = ["aaaaaaaaaaaaaaaaaaaa"]

Y= ["bbbbbbbbbbbbbbb"]

strlengths=[4,8,12,16,20]
worstnaive=[0.0002,0.08,1.17,295.18,51847]
worstmemo=[0.007,0.009,0.001,0.001,0.0011]
avgnaive=[0.000066,0.00276,0.0394,2.95,41.11]
avgmemo=[0.0000333,0.0000335,0.000034,0.000033,0.000034]
stdnaive=[0.00024,0.00223,0.0214,2.016,36.69]
stdmemo=[0.00017,0.00017,0.00018,0.00017,0.000182]

#plt.plot(strlengths,worstnaive)
#plt.show()

Z = []
lX = len(X[0])
lY = len(X[0])
denemesayisi=1
start_time = time.time_ns() 
#c = [[-1 for k in range(lY+1)] for l in range(lX+1)]
for _ in range(denemesayisi):
    
    print("ortak  ",lcs(X[0],Y[0],lX,lY)) #lcs
    finished_time=time.time_ns()
    total_time = (finished_time-start_time) / (10 ** 9)
    print("nanosaniye:", finished_time-start_time)
    print(_+1," inci deneme kac sn surdu: ", total_time)
    Z.append(total_time)
#


#print ("std dev is ", np.std(Z))
#print("mean is ", np.average(Z))
#print ("list is ", Z)
