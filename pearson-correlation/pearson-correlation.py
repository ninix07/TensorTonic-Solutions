import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    
    X = np.asarray(X)
    N=X.shape[0]
    mean = np.mean(X,axis=0)
    X_centered = X - mean 
    cov = np.dot(X_centered.T,X_centered) / (N-1) 
    std = np.std(X,axis=0,ddof=1) # ddof is degree of freedom if 0 divides by N if 1 divide by N-1

    return cov / np.outer(std,std)
   