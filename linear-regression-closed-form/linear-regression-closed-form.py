import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    X = np.asarray(X)
    y= np.asarray(y)

    X_T_X = np.dot(X.T, X)
    X_T_y = np.dot(X.T,y)
    inv = np.linalg.inv(X_T_X)
    return np.dot(inv,X_T_y)