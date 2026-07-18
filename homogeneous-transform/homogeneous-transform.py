import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    T = np.asarray(T)
    points = np.asarray(points)
    points_dim = points.ndim
    if points_dim==1 :
        points = points.reshape(1,3)
    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack([points,ones])
    return_list= np.dot(T,points_h.T).T[:,:3] 
    return return_list.reshape(3,) if points_dim ==1 else return_list