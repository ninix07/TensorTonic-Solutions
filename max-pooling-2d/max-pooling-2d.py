import numpy as np
def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    X = np.asarray(X)
    H,W = X.shape
    H_out = int(np.floor(H/pool_size))
    W_out = int(np.floor(W/pool_size))

    output = np.zeros((H_out,W_out))

    for  i in range(H_out):
        for  j in range(W_out):
            output[i][j] = np.max(X[i*pool_size:i*pool_size+pool_size,j*pool_size:j*pool_size+pool_size])


    return output.tolist()
    