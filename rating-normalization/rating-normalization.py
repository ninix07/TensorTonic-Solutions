import numpy as np
def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    matrix = np.asarray(matrix)

    row_sums = np.sum(matrix, axis=1, keepdims=True)
    row_counts = np.sum(matrix != 0, axis=1, keepdims=True)
    mean = row_sums/row_counts
    matrix = np.where(matrix !=0,matrix-mean,0)

    return matrix.tolist()
        
        