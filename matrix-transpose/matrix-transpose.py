import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m,n= np.shape(A)
    
    return np.array([[A[j][i] for j in range(m) ]for  i in range(n)])
    
    
    
    
