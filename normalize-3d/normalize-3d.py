import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v)

    if v.ndim ==1: 
        norm = np.sqrt(np.sum(v**2))
        return v/norm if norm >1e-10 else np.zeros((v.shape))
    norm =np.sqrt(np.sum(v**2,axis=1,keepdims=True)) 
    return np.where(norm, v/norm, np.zeros((v.shape)))
        