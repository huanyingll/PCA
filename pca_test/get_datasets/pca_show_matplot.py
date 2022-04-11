# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

# %matplotlib inline

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
def plot_linear_cube(x, y, z, dx, dy, dz, color='red'):
    fig = plt.figure()
    ax = Axes3D(fig)
    xx = [x, x, x + dx, x + dx, x]
    yy = [y, y + dy, y + dy, y, y]
    kwargs = {'alpha': 1, 'color': color}
    ax.plot3D(xx, yy, [z] * 5, **kwargs)
    ax.plot3D(xx, yy, [z + dz] * 5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z + dz], **kwargs)
    ax.plot3D([x, x], [y + dy, y + dy], [z, z + dz], **kwargs)
    ax.plot3D([x + dx, x + dx], [y + dy, y + dy], [z, z + dz], **kwargs)
    ax.plot3D([x + dx, x + dx], [y, y], [z, z + dz], **kwargs)
    plt.title('Cube')
    plt.show()



def plot_opaque_cube(x, y, z, dx, dy, dz):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    xx = np.linspace(x, x + dx, 2)
    yy = np.linspace(y, y + dy, 2)
    zz = np.linspace(z, z + dz, 2)

    xx2, yy2 = np.meshgrid(xx, yy)

    ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
    ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))

    yy2, zz2 = np.meshgrid(yy, zz)
    ax.plot_surface(np.full_like(yy2, x), yy2, zz2)
    ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)

    xx2, zz2 = np.meshgrid(xx, zz)
    ax.plot_surface(xx2, np.full_like(yy2, y), zz2)
    ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)

    plt.title("Cube")
    plt.show()
class create3D:
    def __init__(self, list,width):
        print("create3D __init__")
        self.x=list.shape[0]
        self.y=list.shape[1]
        self.z=list.shape[2]
        self.width=width
        self.list=list
        self.count=0
        def recreate():
            list2=self.list
            for i in range(self.x):
                for j in range(self.y):
                    for k in range(self.z):
                        if i!=0 and i!=self.x-1 and j!=0 and j!=self.y-1 and k!=0 and k!=self.z-1:
                            if self.list[i-1,j,k] == 1 and self.list[i+1,j,k] == 1 and self.list[i,j-1,k] == 1 and self.list[i,j+1,k] == 1 and self.list[i,j,k-1] == 1 and self.list[i,j,k+1] == 1:
                                list2[i,j,k]=0
            self.list=list2
        recreate()
        for i in range(self.list.shape[0]):
            for j in range(self.list.shape[1]):
                for k in range(self.list.shape[2]):
                    if self.list[i,j,k]==1:
                        self.count+=1
        print("count:%s" % self.count)
    def show(self):

        print("create3D show")
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        def plot_opaque_cube(x, y, z, dx, dy, dz):

            xx = np.linspace(x, x + dx, 2)
            yy = np.linspace(y, y + dy, 2)
            zz = np.linspace(z, z + dz, 2)
            xx2, yy2 = np.meshgrid(xx, yy)
            ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
            ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))
            yy2, zz2 = np.meshgrid(yy, zz)
            ax.plot_surface(np.full_like(yy2, x), yy2, zz2)
            ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)
            xx2, zz2 = np.meshgrid(xx, zz)
            ax.plot_surface(xx2, np.full_like(yy2, y), zz2)
            ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)
        now =0
        path=0
        for i in range(self.x):
            for j in range(self.y):
                for k in range(self.z):
                    if self.list[i,j,k]==1:
                        #print("添加正方体:",i * self.width,j * self.width,k * self.width)
                        plot_opaque_cube(i * self.width, j * self.width, k * self.width, self.width, self.width,
                                         self.width)
                        now+=1
                        if now !=0:
                            if int(self.count / now) == 100:
                                path += 1
                                print("\r","模型创建中：",str(path) + "/100",end="",flush=True)
                                now = 0
        print("\n","模型创建成功")
        plt.title("Cube")
        plt.show()
"""
if __name__ == "__main__":
    plot_opaque_cube(50,50,50,10,10,10)
"""

import numpy as np
data =np.load("L1.npy")
pic=create3D(data,10)
pic.show()