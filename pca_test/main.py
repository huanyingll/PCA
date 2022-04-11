import math
import numpy as np
from pca.pca_test.batch_createVirtualSpines import batch_createVirtualSpines
from pca.pca_test.dataOperate import *

if __name__ == "__main__":
    #参考标记点数据集
    referencedatasets=[]
    for i in range(21):
        referencedatasets.append("/Users/zhaoyifei/Documents/pythonDeepLearning/pca/datasets/spines_points/"+str(i+1)+".txt")
    referencedatasets=np.array(referencedatasets)
    """
    #变形参数集
    count = 100
    min_c = -2
    max_c = 2
    components=3
    t=int(math.pow(count,1/components))+1
    pace=(max_c-min_c)/t
    deformparameters = []
    c=0
    for j in range(t):
        for k in range(t):
            for l in range(t):
                d = []
                d.append(min_c + j * pace)
                d.append(min_c + k * pace)
                d.append(min_c + l * pace)
                d = np.array(d)
                deformparameters.append(d)
                c += 1
                if c == count:
                    break
            if c == count:
                break
        if c == count:
            break
            """
    count = 2
    deformparameters=[[0,0,0,0,20],[0,0,0,0,-20]]
    deformparameters=np.array(deformparameters)

    #标准数据集
    undeformdata="/Users/zhaoyifei/Documents/pythonDeepLearning/pca/datasets/pointCloudData/1L.txt"

    #工作目录
    workplace="workplace/"

    #输出stl文件
    outputstlfiles = []
    for i in range(count):
        outputstlfiles.append("/Users/zhaoyifei/Desktop/virtualspines/L_"+arrayToStr(np.array(deformparameters[i]))+".stl")
    #outputstlfiles = ["out.stl"]
    outputstlfiles=np.array(outputstlfiles)

    batch_createVirtualSpines(referencedatasets, deformparameters, undeformdata, workplace,outputstlfiles)