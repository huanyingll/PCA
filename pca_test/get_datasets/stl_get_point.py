import vtk
import numpy as np
#右键选点，按下中键取消点的选择。按一次取消上一次选点，选取的点坐标和模型文件在同一个文件夹中


def getfilename():
    filename= input("输入文件名称: ")  # C:/Users/big tiger/Desktop/foot/GTQ pyinstaller -F C:\Users\big tiger\PycharmProjects\POINTpicker\pointpicker.py
    return filename

def GetstlData(filename):
    stlReader = vtk.vtkSTLReader()
    stlReader.SetFileName("../../datasets/Models/spines/"+filename+".stl")
    stlReader.Update()
    data = stlReader.GetOutput()
    print("nodes number：", data.GetNumberOfPoints())
    if data.GetNumberOfPoints() == 0:
        raise ValueError("No point data could be loaded from " + filename)
        return None

    return data

class interactor(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self,parent=None):
        self.AddObserver("RightButtonPressEvent",self.RightButtonPressEvent)
        self.AddObserver("MiddleButtonPressEvent", self.MiddleButtonPressEvent)
        self.i=1
        self.controlpoints={}

        self.actor=[]

    def RightButtonPressEvent(self, obj, event):
        clickPos = self.GetInteractor().GetEventPosition()#得到二维图像点
        #print("Picking pixel: ", clickPos)

        # Pick from this location
        picker = self.GetInteractor().GetPicker()#初始化picker动作
        picker.Pick(clickPos[0], clickPos[1], 0, self.GetDefaultRenderer())#自己定义的渲染函数

        value_list=[]
        for j in range(len(self.controlpoints)):
            value_list.append(self.controlpoints[j + 1])
        value_list_1 = np.array(value_list)
        np.savetxt(filename + ".txt",value_list_1)

        # If CellId = -1, nothing was picked
        if  value_list.count(data.GetPoint(picker.GetPointId()))==0:

            point_position = data.GetPoint(picker.GetPointId())
            # print("Pick position is: ", picker.GetPickPosition())#选点的坐标
            #print("Cell id is:", picker.GetCellId())
            #print("Point id is:", picker.GetPointId())
            #贴合到实体上的坐标
            self.controlpoints[self.i]=point_position
            print(self.i,":",self.controlpoints[self.i])#json.dumps(,indent=0)

            # Create a sphere
            sphereSource = vtk.vtkSphereSource()
            sphereSource.SetCenter(point_position)
            # sphereSource.SetRadius(0.2)
            sphereSource.SetRadius(1)

            # Create a mapper and actor
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(sphereSource.GetOutputPort())

            self.actor.append(vtk.vtkActor())
            self.actor[self.i-1].SetMapper(mapper)
            self.actor[self.i-1].GetProperty().SetColor(1.0, 0.0, 0.0)
            self.GetDefaultRenderer().AddActor(self.actor[self.i-1])
            self.i += 1
        self.OnRightButtonDown()
        value_list = []
        for j in range(len(self.controlpoints)):
            value_list.append(self.controlpoints[j + 1])
        value_list_1 = np.array(value_list)
        np.savetxt(filename + ".txt", value_list_1)
        return

    def MiddleButtonPressEvent(self,obj,event):
        num=len(self.controlpoints)
        if num>0:
            del self.controlpoints[num]
            self.i=self.i-1
            self.GetDefaultRenderer().RemoveActor(self.actor[self.i-1])
        value_list=[]
        for j in range(len(self.controlpoints)):
            value_list.append(self.controlpoints[j + 1])
        value_list_1 = np.array(value_list)
        np.savetxt(filename + ".txt",value_list_1)
        self.OnMiddleButtonDown()
        return





def CreateScene():
    # Create a rendering window and renderer
    renWin = vtk.vtkRenderWindow()
    # Set window size
    renWin.SetSize(600, 600)
    ren = vtk.vtkRenderer()
    # Set background color
    #ren.GradientBackgroundOn()
    #ren.SetBackground(.1, .1, .1)
    #ren.SetBackground2(0.8, 0.8, 0.8)

    renWin.AddRenderer(ren)

    # Create a renderwindowinteractor
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    #交互风格
    style = interactor()
    style.SetDefaultRenderer(ren)
    iren.SetInteractorStyle(style)

    # vtkCellPicker will shoot a ray into a 3D scene and return information about
    # the first object that the ray hits.
    CellPicker = vtk.vtkCellPicker()
    iren.SetPicker(CellPicker)

    # load STL file
    global data
    global filename
    filename=getfilename()
    data=GetstlData(filename)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(data)  # maps polygonal data to graphics primitives
    actor = vtk.vtkLODActor()
    actor.SetMapper(mapper)
    actor.GetProperty().EdgeVisibilityOn()#这两行可以使用网格展现
    actor.GetProperty().SetLineWidth(0.3)

    ren.AddActor(actor)

    # Enable user interface interactor
    iren.Initialize()
    iren.Start()


if __name__ == "__main__":

    CreateScene()

