import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g= np.asarray(g)
    
    norm = np.linalg.norm(g.ravel(),ord=2)
    if max_norm <=0 :
        return g
    return g if norm<= max_norm else g*max_norm/norm