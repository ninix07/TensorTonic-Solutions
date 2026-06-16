import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X= np.asarray(X)
    min_X = np.min(X,keepdims=True,axis=axis)
    max_X =np.max(X,keepdims=True,axis=axis)
    
    num= X- min_X
    den= np.maximum(eps, (max_X-min_X))
    return num/den
    