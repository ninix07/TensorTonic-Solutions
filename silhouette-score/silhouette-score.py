import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    X = np.asarray(X)
    labels = np.asarray(labels)
    dist = np.sqrt(np.sum((X[:,None,:]- X[None,:,:])**2,axis=-1))

    same_cluster = labels[:,None]==labels[None,:]
    diag = np.eye(X.shape[0],dtype=bool)
    same_cluster = same_cluster & ~diag
    a = np.sum(np.where(same_cluster,dist,0),axis=-1)/np.sum(same_cluster,axis=-1)
    unique_labels = np.unique(labels)
    b_candidates = []
    for label in unique_labels:
        mask = labels == label
        cluster_dists = dist[:, mask]
        avg_to_cluster = cluster_dists.mean(axis=1)
        avg_to_cluster[mask] = np.inf
        b_candidates.append(avg_to_cluster)
        
    
        
    b = np.array(b_candidates).min(axis=0)
    
    return np.mean((b-a)/np.maximum(a,b))
    

    

    