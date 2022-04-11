"""
模型对齐，
参考论文"A Brief Introduction to Statistical Shape Analysis"，
输入为n个具有相同标记点个数的xyz坐标集
"""

import math
import numpy as np

class GPA:
    def __init__(self,datasets):
        self.datasets=datasets
    # 进行对齐
    def fix(self):
      #平方点距离
      def getSquaredProcrustesDistance(standard,data):
          Pd=0
          for i in range(standard.shape[0]):
              p=0
              for j in range(standard.shape[1]):
                  p+=(standard[i][j]-data[i][j])*(standard[i][j]-data[i][j])
              Pd+=p
          return Pd
      #得到质心
      def getCentroid(data):
          c=[]
          for j in range(data.shape[1]):
              k=0
              for i in range(data.shape[0]):
                  k+=data[i][j]
              k=k/data.shape[0]
              c.append(k)
          c=np.array(c)
          return c
      #得到形状尺寸度量
      def getShapeSizeMetric(data,centroid):
          #Frobenius norm
          Sx=0
          for i in range(data.shape[0]):
              x=0
              for j in range(data.shape[1]):
                  x+=(data[i][j]-centroid[j])*(data[i][j]-centroid[j])
              Sx+=x
          Sx=math.sqrt(Sx)
          return Sx
      #对齐模型形状
      def getEqualSize(standard,data):
          centroid1 = getCentroid(standard)
          centroid2 = getCentroid(data)
          shapesizemetric1 = getShapeSizeMetric(standard,centroid1)
          shapesizemetric2 = getShapeSizeMetric(data,centroid2)
          shapesizemetric_diff=shapesizemetric2/shapesizemetric1
          data2=[]
          for i in range(data.shape[0]):
              d=[]
              for j in range(data.shape[1]):
                  f=float(float((data[i][j]-centroid2[j]))/shapesizemetric_diff+centroid2[j])
                  d.append(f)
              data2.append(d)
          data=np.array(data2)
          return data
      #对齐模型质心
      def getEqualCentroid(standard,data):
          centroid1 = getCentroid(standard)
          centroid2 = getCentroid(data)
          centroid_diff=[]
          for i in range(centroid1.shape[0]):
              centroid_diff.append(centroid2[i]-centroid1[i])
          centroid_diff=np.array(centroid_diff)
          for i in range(data.shape[0]):
              for j in range(data.shape[1]):
                  data[i][j]=data[i][j]-centroid_diff[j]
          data=np.array(data)
          return data
      #将矩阵旋转对齐
      def getEqualRoatate(standard,data):
          c1=getCentroid(standard)
          c2=getCentroid(data)
          b=standard.copy()
          a=data.copy()
          for i in range(b.shape[0]):
              for j in range(b.shape[1]):
                  b[i][j]=b[i][j]-c1[j]
                  a[i][j]=a[i][j]-c2[j]
          B = np.transpose(b)
          A = np.transpose(a)
          H=np.dot(B,np.transpose(A))
          U ,S ,VT=np.linalg.svd(H)
          R=np.dot(np.transpose(VT),np.transpose(U))
          #T=np.dot(-R,np.transpose(c1))+np.transpose(c2)
          data=np.dot(R,A)
          data=np.array(np.transpose(data))
          return data
      c=getCentroid(self.datasets[0])
      for i in range(self.datasets[0].shape[0]):
          for j in range(self.datasets[0].shape[1]):
              self.datasets[0][i][j]=self.datasets[0][i][j]-c[j]
      datas=[]
      #datas.append(self.datasets[0])
      for i in range(self.datasets.shape[0]-1):
          data=[]
          data = getEqualCentroid(self.datasets[0],self.datasets[i+1])
          data = getEqualSize(self.datasets[0],data)
          data = getEqualRoatate(self.datasets[0],data)
          datas.append(data)
      datas=np.array(datas)
      #print("cen:",getCentroid(datas[1]),getCentroid(datas[2]))
      #print("shape",getShapeSizeMetric(datas[1],getCentroid(datas[1])),getShapeSizeMetric(datas[2],getCentroid(datas[2])))
      #getEqualRoatate(datas[0],datas[1])
      return datas



