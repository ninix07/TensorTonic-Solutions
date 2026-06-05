import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n=len(v)
    diag_matrix = np.zeros((n,n))

    for i in range(n):
        diag_matrix[i][i] = v[i]

    return diag_matrix


    # or use
    #np.diag(v)