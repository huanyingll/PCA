import numpy as np
import vtk

# Read from file

from pca.pca_test.fileOperate import *
def spinesToPoints(stlfiles):
    data1=[]
    data2=[]
    for i in range(stlfiles.shape[0]):
        stlreader = vtk.vtkSTLReader()
        stlreader.SetFileName(stlfiles[i])
        # 输出所有点坐标
        stlreader.Update()
        stlMapper = vtk.vtkPolyDataMapper()
        stlMapper.SetInputConnection(stlreader.GetOutputPort())
        p = [0, 0, 0]
        polydata = stlreader.GetOutput()
        data1.append(polydata.GetNumberOfPoints())
        # fp.write(str(polydata.GetNumberOfPoints())+"\r\n")
        for i in range(polydata.GetNumberOfPoints()):
            polydata.GetPoint(i, p)
            d = []
            d.append(p[0])
            d.append(p[1])
            d.append(p[2])
            data2.append(d)
    data1=np.array(data1)
    data2=np.array(data2)
    print("输出成功")
    del stlreader
    return data1, data2