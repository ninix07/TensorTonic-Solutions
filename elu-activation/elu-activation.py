import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x = np.asarray(x) 
    exp_x= np.exp(x)
    x= np.where(x>0, x , alpha *(exp_x -1))
    return x.tolist()