import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
   
    norm_factor =1
    matrix = np.asarray(matrix)
    if np.ndim(matrix)!=2 or axis not in [0,1,None] :
        return None
    if norm_type == 'l2':
        norm_factor = np.linalg.norm(matrix, axis =axis,keepdims=True)
    elif norm_type == 'l1':
        norm_factor = np.linalg.norm(matrix, ord=1, axis=axis,keepdims=True)
    elif norm_type == 'max':
        norm_factor = np.max(matrix,axis=axis,keepdims=True)
    else:
        return None
    norm_factor = np.where(norm_factor ==0 , 1, norm_factor)
    return matrix/norm_factor 

    