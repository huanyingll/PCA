import os
import pymeshlab

def OutputFile(filename,data,headdata=[],kind="nohead"):
    fp=open(filename,"w")
    #无头数据
    if kind == "nohead":
        for i in range(data.shape[0]):
            fp.write(str(data[i][0]) + " "+str(data[i][1])+" "+str(data[i][2])+"\r\n")
    elif kind == "havehead":
        s=""
        for i in range(headdata.shape[0]):
            s+=str(headdata[i])
            if i < headdata.shape[0] - 1:
                s+=" "
        fp.write(s+"\r\n")
        for i in range(data.shape[0]):
            fp.write(str(data[i][0]) + " "+str(data[i][1])+" "+str(data[i][2])+"\r\n")
    fp.close()
def InputFile(filename,kind="nohead"):
    fp=open(filename)
    if kind == "nohead":
        data = []
        with open(filename, 'r') as file_to_read:
            lines = file_to_read.readline()
            while lines != "":
                lines = lines.strip('\n').split(" ")
                point = []
                point.append(float(lines[0]))
                point.append(float(lines[1]))
                point.append(float(lines[2]))
                data.append(point)
                lines = file_to_read.readline()
        data = np.array(data)
        return data
    if kind == "havehead":
        data = []
        with open(filename, 'r') as file_to_read:
            headdata = file_to_read.readline()
            lines = file_to_read.readline()
            while lines != "":
                lines = lines.strip('\n').split(" ")
                point = []
                point.append(float(lines[0]))
                point.append(float(lines[1]))
                point.append(float(lines[2]))
                data.append(point)
                lines = file_to_read.readline()
        data = np.array(data)
        headdata = headdata.strip('\n').split(" ")
        headdata=np.array(headdata)
        return headdata,data
    fp.close()
"""
???这是什么鬼东西，有可以改进的方式，直接改，目前用的这个太奇葩了
合并stl文件
"""
def mergeStl(plyFiles,outputFile):
    datas=[]
    for i in range(plyFiles.shape[0]):
        ml = pymeshlab.MeshSet()
        ml.load_new_mesh(plyFiles[i])
        ml.save_current_mesh("Test.stl", binary=False)
        fp = open("Test.stl")
        data1 = []
        line = fp.readline()
        while line != "":
            data1.append(line)
            line = fp.readline()
        fp.close()
        data1=np.array(data1)
        datas.append(data1)
    datas=np.array(datas,dtype=object)
    data=[]
    data.append(datas[0][0])
    for i in range(datas.shape[0]):
        for j in range(datas[i].shape[0]-2):
            data.append(datas[i][j+1])
    data.append(datas[0][datas[0].shape[0]-1])
    data=np.array(data)
    fp = open(outputFile, "w")
    for i in range(data.shape[0]):
        fp.write(data[i])
    fp.close()
    ml = pymeshlab.MeshSet()
    ml.load_new_mesh(outputFile)
    ml.save_current_mesh(outputFile, binary=True)
    os.remove("Test.stl")
    del ml
"""
xyz文件转为ply文件
"""
import numpy as np
import open3d as o3d
def xyzToPly(xyzfile,outputplyfile):
    for i in range(xyzfile.shape[0]):
        pcd = o3d.io.read_point_cloud(xyzfile[i])
        pcd.estimate_normals()
        # to obtain a consistent normal orientation
        pcd.orient_normals_consistent_tangent_plane(k=25)
        # or you might want to flip the normals to make them point outward, not mandatory
        pcd.normals = o3d.utility.Vector3dVector(- np.asarray(pcd.normals))
        # surface reconstruction using Poisson reconstruction
        mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
        # paint uniform color to better visualize, not mandatory
        mesh.paint_uniform_color(np.array([0.7, 0.7, 0.7]))
        o3d.io.write_triangle_mesh(outputplyfile[i], mesh)
