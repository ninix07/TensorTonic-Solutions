import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    # Write code here
    X_train = np.asarray(X_train)
    X_test  = np.asarray(X_test)
    if X_train.ndim ==1 :
        X_train =X_train.reshape(-1,1)
        X_test = X_test.reshape(-1,1)

    dis = X_test[:, np.newaxis, :] - X_train[np.newaxis, :, :]
    dist_matrix = np.sum(dis ** 2, axis=-1)
    if k > len(X_train):
        padding_width = k - len(X_train)
        padded_indices = np.pad(
            np.argsort(dist_matrix, axis=1), 
            pad_width=((0, 0), (0, padding_width)), 
            mode='constant', 
            constant_values=-1
        )
        return padded_indices
    else:
        return np.argsort(dist_matrix, axis=1)[:, :k]