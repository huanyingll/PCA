import math
import numpy as np
from sklearn.decomposition import PCA
from pca.pca_test.dataOperate import *
from pca.pca_test.GPA import GPA
from pca.pca_test.fileOperate import *
def createVirtualSpines(exampleData,components,c):
    data = np.array(exampleData)
    gpa= GPA(data)
    data=gpa.fix()
    rdata=reshapedata(data)
    ave_data=averagedata(rdata)
    pca = PCA(n_components=components)  # 选取前10个主成分
    x_train = pca.fit_transform(rdata)  # 变化特征值
    #print("特征向量", pca.components_.shape)
    #print("explained variance: %s" % pca.explained_variance_)  # 输出前10个主成分特征值
    #print("explained variance ratio: %s" % pca.explained_variance_ratio_)  # 输出前10个主成分的各自贡献率
    #print('pca:accumulated rate: %s' % sum(pca.explained_variance_ratio_))  # 输出前10个主成分的累计贡献率
    virtual_data=ave_data.copy()
    for i in range(virtual_data.shape[0]):
        for j in range(virtual_data.shape[1]):
            for k in range(components):
                virtual_data[i][j] += c[k] * math.sqrt(pca.explained_variance_[k]) * pca.components_[k][j]
    new_ave_data=[]
    for i in range(ave_data.shape[1]):
        d=[]
        d.append(ave_data[0][i])
        d.append(ave_data[1][i])
        d.append(ave_data[2][i])
        new_ave_data.append(d)
    new_ave_data=np.array(new_ave_data)
    new_virtual_data = []
    for i in range(ave_data.shape[1]):
        d = []
        d.append(virtual_data[0][i])
        d.append(virtual_data[1][i])
        d.append(virtual_data[2][i])
        new_virtual_data.append(d)
    new_virtual_data = np.array(new_virtual_data)

    #print('pca:accumulated rate: %s' % sum(pca.explained_variance_ratio_),end="")  # 输出前10个主成分的累计贡献率
    #print("explained variance ratio: %s" % pca.explained_variance_ratio_)  # 输出前10个主成分的各自贡献率
    return new_ave_data,new_virtual_data
