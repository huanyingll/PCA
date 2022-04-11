import math

import numpy as np

def reshapedata(data):
    rd=[]
    for i in range(data.shape[2]):
        for k in range(data.shape[0]):
            d = []
            for j in range(data.shape[1]):
                d.append(data[k, j, i])
            rd.append(d)
    """
    for i in range(data.shape[2]):
        for j in range(data.shape[0]):
            d=[]
            for k in range(data.shape[1]):
                d.append(data[j,k,i])
            rd.append(d)
    """
    rd=np.array(rd)
    return rd
def averagedata(data):
    ad=[]
    for i in range(3):
        a=[]
        for j in range(data.shape[1]):
            sum = 0
            for k in range(int(data.shape[0]/3)):
                sum+=data[int(i*data.shape[0]/3+k)][j]
            sum /= data.shape[0]/3
            a.append(sum)
        ad.append(a)
    ad=np.array(ad)
    return ad
def arrayToStr(thearray):
    s=""
    for i in range(thearray.shape[0]):
        s+=str(thearray[i])
        if i <thearray.shape[0]-1:
            s+="_"
    return s