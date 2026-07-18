import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here

    points = np.asarray(points)
    points_ndim = points.ndim
    if points_ndim ==1:
        points = points.reshape(1,3)
    cos = np.cos(theta)
    sin = np.sin(theta)
    transformation = np.asarray([[cos,-sin,0],[sin,cos,0],[0,0,1]])
    
    return_list= np.dot(transformation,points.T).T

    return return_list.reshape(3,) if points_ndim==1 else return_list