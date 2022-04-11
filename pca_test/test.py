import math
#import vtk
from pca.pca_test.GPA import GPA
import pymeshlab
from pca.pca_test.fileOperate import *
from pca.pca_test.kriging import kriging
from pca.pca_test.createVirtualSpines import createVirtualSpines
"""
ok!没问题啦!注意标记点的顺序要对！
"""
def test_gpa():
    #array1=[[1,1],[-1,1],[-1,-1],[1,-1]]
    #array2=[[6,3],[6,-3],[0,3],[0,-3]]
    #array2 = [[3, 1], [3, -1], [2, 0], [4, 0]]
    #array1=[[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1],[1,1,-1],[-1,1,-1],[-1,-1,-1],[1,-1,-1]]
    array1 = [[2, 2, 2], [0, 2, 2], [0, 0, 2], [2, 0, 2], [2, 2, 0], [0, 2, 0], [0, 0, 0], [2, 0, 0]]
    #array2 = [[5, 5, 3], [-1, 5, 3], [-1, -1, 3], [5, -1, 3], [5, 5, -3], [-1, 5, -3], [-1, -1, -3], [5, -1, -3]]
    #array2=[[math.sqrt(2)+1,0+2,0+3],[0+1,math.sqrt(2)+2,0+3],[-math.sqrt(2)+1,0+2,0+3],[0+1,-math.sqrt(2)+2,0+3],[math.sqrt(2)+1,0+2,2+3],[0+1,math.sqrt(2)+2,2+3],[-math.sqrt(2)+1,0+2,2+3],[0+1,-math.sqrt(2)+2,2+3]]
    array2=[[2,2*math.sqrt(2),0],[0,2*math.sqrt(2),0],[0,math.sqrt(2),math.sqrt(2)],[2,math.sqrt(2),math.sqrt(2)],[2,math.sqrt(2),-math.sqrt(2)],[0,math.sqrt(2),-math.sqrt(2)],[0,0,0],[2,0,0]]
    array=[]
    array.append(array1)
    array.append(array2)
    array=np.array(array)
    gpa=GPA(array)
    data=gpa.fix()
    print("data")
    print(data[0])
    """
    ax = plt.subplot(projection='3d')  # 创建一个三维的绘图工程
    ax.set_title('3d_image_show')  # 设置本图名称
    for i in range(data[0].shape[0]):
        ax.scatter(data[0][i][0], data[0][i][1], data[0][i][2], c='r')  # 绘制数据点 c: 'r'红色，'y'黄色，等颜色
    ax.set_xlabel('X')  # 设置x坐标轴
    ax.set_ylabel('Y')  # 设置y坐标轴
    ax.set_zlabel('Z')  # 设置z坐标轴
    plt.show()
    """

def test_meshlab():
    file = ["L1.ply", "L2.ply", "L3.ply", "L4.ply", "L5.ply"]
    file=np.array(file)
    for i in range(file.shape[0]):
        ml = pymeshlab.MeshSet()
        ml.load_new_mesh(file[i])
        ml.save_current_mesh("LL"+str(i+1)+".stl")
    print("hello world")
def test_createSpines():
    createVirtualSpines("/Users/zhaoyifei/Documents/Q/2/test_UL.txt",
                        "/Users/zhaoyifei/Documents/Q/2/test_DL.txt ", -0.5)
def test_kriging():
    k=kriging(InputFile("/Users/zhaoyifei/Documents/Q/2/UL2.txt"),
              InputFile("/Users/zhaoyifei/Documents/Q/2/DL2.txt"),
              InputFile("/Users/zhaoyifei/Documents/Q/2/LL.txt"))
    d=k.fix()
    OutputFile("/Users/zhaoyifei/Documents/Q/2/D2.txt",d)
def test_pptk():
    print("hello world")
def test_mergestl():
    a=["LL1.stl","LL2.stl","LL3.stl","LL4.stl","LL5.stl"]
    a=np.array(a)
    o="m.stl"
    mergeStl(a,o)
def test_vtk():
    print(os.path.realpath("说明文档.txt"))
    ml = pymeshlab.MeshSet()
    ml.load_new_mesh("1.stl")
    ml.save_current_mesh("11.stl")
if __name__ == "__main__":
    test_mergestl()
    #test_mergestl()
    #test_meshlab()



