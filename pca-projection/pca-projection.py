import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here

    X = np.asarray(X)
    mean = np.mean(X,axis=0)
    X_c = X - mean
    N = X.shape[1]
    C = np.dot(X_c.T, X_c)/ (N-1)
    eigenvalues,eigenvectors = np.linalg.eig(C)
    sorted_indices = np.argsort(eigenvalues)
    top_k_indices = sorted_indices[::-1][:k]
    top_k_vectors = eigenvectors[:,top_k_indices]

    return np.dot(X_c, top_k_vectors)
    
   

    

    
    
