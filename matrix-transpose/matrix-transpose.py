import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A= np.asarray(A)
    m,n= A.shape
    B = np.array([[A[i][j] for i in range(m)] for j in range(n)])

    return B