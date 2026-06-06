import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        matrix = np.asarray(matrix)
    except :
        return None
    if np.ndim(matrix) !=2:
        return None
    if matrix.size == 0 or matrix.shape[0] != matrix.shape[1]:
        return None
    eigen_val = np.linalg.eigvals(matrix)
    np.lexsort((eigen_val.imag , eigen_val.real))
    
    return eigen_val