import numpy as np
def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here

    X = np.asarray(X)
    y = np.asarray(y)
    identity = np.identity(X.shape[1])

    inv = np.dot(X.T,X)+ lam *identity
    X_T_y = np.dot(X.T,y)
    
    return np.dot(np.linalg.inv(inv),X_T_y)