import numpy as np

from pca.pca_test.fileOperate import *
from pca.pca_test.get_datasets.stl_spines_to_points import spinesToPoints


def get_spines_to_points():
    stlfiles=["../../datasets/Models/1/L1.stl",
              "../../datasets/Models/1/L2.stl",
              "../../datasets/Models/1/L3.stl",
              "../../datasets/Models/1/L4.stl",
              "../../datasets/Models/1/L5.stl"]
    stlfiles=np.array(stlfiles)
    outputfile="../../datasets/pointCloudData/1L.xyz"
    headdata,data=spinesToPoints(stlfiles)
    OutputFile(outputfile,data,headdata=headdata,kind="havehead")



if __name__ == "__main__":
    get_spines_to_points()