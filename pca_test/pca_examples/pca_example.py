# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:29:57 2020

@author: YWT
"""

#导入数据包
import pandas as pd
import numpy as np

alldata=[]
for i in range(1,11):
    x= pd.read_csv('D:/spine_SSM/data/alignment/'+str(i)+'pointsdatas.csv', header=None)
    x = np.mat(x)
#    print('读入数据：\n',x)
    
    data_x1= x.reshape(99,1)
#    print('一维形状矩阵：\n',data_x1)
    alldata.append(data_x1)
#    
alldata = np.array(alldata)
#
alldata1 = alldata.reshape(10,99)

#print(alldata1)

mean_x =np.mean(alldata1, axis=0)
mean_x = mean_x.reshape(99,1)


# from sklearn import decomposition
from sklearn.decomposition import PCA

#数据的读取 
X= pd.read_csv('D:/spine_SSM/data/alignment/alldata.csv', header=None)  


# PCA降维度
pca = PCA(n_components='mle')  #降到三维 
pca.fit(X)#训练
newX = pca.transform(X)#降维后的数据
#返回原始数据
#X_1=pca.inverse_transform(newX)

#打印X看看结果
#print(X,'\n')
#print('原始数据:',X_1,'\n')
print('贡献率：',pca.explained_variance_ratio_)  #输出贡献率
#print('特征向量：\n',pca.explained_variance_)
#print('降维后的数据：',newX)

data1 = 0.01*newX[:,0]
data2 = newX[:,1]
data3 = newX[:,2]
#计算SSM:
SSM= pd.read_csv('D:/spine_SSM/data/alignment/SSM.csv', header=None)
SSM= np.mat(SSM)
SSM= SSM.reshape(33,3)  
with open("SSM.txt","a") as f:
    s = str(SSM).replace('[','').replace(']','')+'\n'
    s = s.replace(',','')
    f.write(s)

