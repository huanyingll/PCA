from pca.pca_test.fileOperate import *
from pca.pca_test.kriging import kriging
from pca.pca_test.createVirtualSpines import createVirtualSpines
def batch_createVirtualSpines(referencedatasets,deformparameters,undeformdata,workplace,outputstlfiles):
    referencedata = []
    for i in range(referencedatasets.shape[0]):
        d = InputFile(referencedatasets[i])
        referencedata.append(d)
    referencedata=np.array(referencedata)
    for dp in range(deformparameters.shape[0]):
        """
        生成虚拟脊椎数据，保存为xyz文件
        """
        print("生成虚拟脊椎标记点数据-"+str(dp + 1) + ":", end="")
        # 创建虚拟骨骼标记点
        ul, dl = createVirtualSpines(referencedata,np.array(deformparameters[dp]).shape[0], np.array(deformparameters[dp]))
        headdata, otherdata = InputFile(undeformdata, "havehead")
        print("虚拟标记点生成完成,", end="")
        k = kriging(ul, dl, otherdata)
        d = k.fix()
        d = np.array(d)
        xyzfiles = []
        for i in range(headdata.shape[0]):
            sum = 0
            data2 = []
            for j in range(i):
                sum += int(headdata[j])
            for j in range(int(headdata[i])):
                data2.append(d[j + sum])
            data2 = np.array(data2)
            f = workplace + "xyz_"+ str(i+1) + ".xyz"
            xyzfiles.append(f)
            OutputFile(f, data2)
        xyzfiles = np.array(xyzfiles)
        print("虚拟数据生成完成")
        """
        xyz文件转ply文件，并删除xyz文件
        """
        print("生成ply文件-" + str(dp + 1) + ":", end="")
        plyfiles = []
        for i in range(xyzfiles.shape[0]):
            plyfiles.append(workplace+"ply_"+ str(i+1) +".ply")
        plyfiles = np.array(plyfiles)
        xyzToPly(xyzfiles, plyfiles)
        for f in xyzfiles:
            os.remove(f)
        print("ply文件生成完成")
        """
        ply文件转stl文件并合并
        """
        print("生成stl文件-" + str(dp + 1) + ":", end="")
        mergeStl(plyfiles, outputstlfiles[dp])
        for f in plyfiles:
            os.remove(f)
        print("stl文件——"+outputstlfiles[dp]+"生成完成")

