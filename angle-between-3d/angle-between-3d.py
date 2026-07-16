import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v= np.asarray(v)
    w = np.asarray(w)
    dot_product = np.dot(v,w)

    v_norm = np.linalg.norm(v,ord=2)
    w_norm = np.linalg.norm(w,ord=2)

    if v_norm < 1e-10 or w_norm < 1e-10:
        return np.nan

    cos_val = dot_product/ (v_norm * w_norm) 

    cos_val= np.clip(cos_val,-1,1)

    return np.arccos(cos_val)