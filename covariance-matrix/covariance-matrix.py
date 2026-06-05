import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    
    N= len(X)
    X= np.asarray(X)
    if X.ndim != 2 or N<2:
        return None
    miu = np.mean(X, axis=0)
    
    X_centered = X -miu 
    return np.dot(X_centered.T , X_centered)/ (N-1)
    