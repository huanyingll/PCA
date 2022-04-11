import math

import numpy as np

from pca.pca_test.fileOperate import InputFile
class kriging:
    def __init__(self,undeformData,deformData,data):
        self.undeformData = undeformData
        self.deformData = deformData
        self.data=data
    def fix(self):
        def distance(point1,point2):
            d=0
            for i in range(point1.shape[0]):
                d+=(point1[i]-point2[i])*(point1[i]-point2[i])
            d=math.sqrt(d)
            return d
        def createA():
            m = []
            for i in range(self.undeformData.shape[0] + self.undeformData.shape[1] + 1):
                f=[]
                for j in range(self.undeformData.shape[0] + self.undeformData.shape[1] + 1):
                    if i < self.undeformData.shape[0] and j < self.undeformData.shape[0]:
                        f.append(distance(self.undeformData[i], self.undeformData[j]))
                    elif i < self.undeformData.shape[0] and j >= self.undeformData.shape[0]:
                        if j == self.undeformData.shape[0]:
                            f.append(1)
                        else:
                            f.append(self.undeformData[i][j - 1 - self.undeformData.shape[0]])
                    elif i >= self.undeformData.shape[0] and j < self.undeformData.shape[0]:
                        if i == self.undeformData.shape[0]:
                            f.append(1)
                        else:
                            f.append(self.undeformData[j][i - self.undeformData.shape[0]-1])
                    else:
                        f.append(0)
                m.append(f)
            m=np.array(m)
            return m
        def createB(k):
            b=[]
            for i in range(self.deformData.shape[0]+self.deformData.shape[1]+1):
                if i <self.undeformData.shape[0]:
                    b.append(self.deformData[i][k])
                else:
                    b.append(0)
            b=np.array(b)
            return b
        def getX(A,b):
            b=np.transpose(b)
            x = np.linalg.solve(A, b)
            x=np.array(np.transpose(x))
            return x
        deform=[]
        for i in range(self.data.shape[0]):
            d=[]
            for j in range(self.undeformData.shape[0]+self.data.shape[1]+1):
                if j==0:
                    d.append(1)
                elif j>0 and j<self.data.shape[1]+1:
                    d.append(self.data[i][j-1])
                else:
                    d.append(distance(self.data[i],self.undeformData[j-1-self.undeformData.shape[1]]))
            deform.append(d)
        deformM=[]
        A = createA()
        for i in range(self.undeformData.shape[1]):
            b=createB(i)
            x=getX(A,b)
            x2=[]
            for i in range(self.deformData.shape[0]+self.deformData.shape[1]+1):
                if i<self.deformData.shape[1]+1:
                    x2.append(x[i+self.deformData.shape[0]])
                else:
                    x2.append(x[i-self.deformData.shape[1]-1])
            deformM.append(x2)
        deformM=np.array(deformM)
        deform = np.array(deform)
        deformM = np.transpose(deformM)
        """
        for i in range(deformM.shape[0]):
            print(str(i)+":  ",end="")
            for j in range(deformM.shape[1]):
                print(str(deformM[i][j])+" ",end="")
            print("\n")  
        """
        d=np.dot(deform,deformM)
        return d

