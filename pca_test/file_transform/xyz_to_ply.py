import numpy as np
import open3d as o3d
file=["../L1.xyz","../L2.xyz","../L3.xyz","../L4.xyz","../L5.xyz"]
file=np.array(file)
for i in range(file.shape[0]):
    pcd = o3d.io.read_point_cloud(file[i])
    pcd.estimate_normals()

    # to obtain a consistent normal orientation
    pcd.orient_normals_consistent_tangent_plane(k=25)
    # or you might want to flip the normals to make them point outward, not mandatory
    pcd.normals = o3d.utility.Vector3dVector(- np.asarray(pcd.normals))

    # surface reconstruction using Poisson reconstruction
    mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)

    # paint uniform color to better visualize, not mandatory
    mesh.paint_uniform_color(np.array([0.7, 0.7, 0.7]))

    o3d.io.write_triangle_mesh("../L"+str(i+1)+".ply", mesh)
