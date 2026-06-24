import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    """
    Split features X and labels y into train/test while preserving class proportions.
    """
    # Write code here
    X = np.asarray(X)
    y=np.asarray(y)
    indices = [i for i in range(len(X))]
    val,counts = np.unique(y,return_counts=True)
    proportion = counts/np.sum(counts)
    class_indices = []

    for v in val:
        curr_class_idx = np.where(y==v)[0]
        if rng:
            rng.shuffle(curr_class_idx)
        else:
            np.random.shuffle(curr_class_idx)
        class_indices.append(curr_class_idx)

    test_len = np.round(len(y) *test_size).astype(int)
    class_test_counts = np.round(proportion * test_len).astype(int)
    test_indices, train_indices = zip(*[
    (class_index[:count], class_index[count:])
    for count, class_index in zip(class_test_counts, class_indices)
])
        
    test_indices= np.sort(np.concatenate(test_indices))
    train_indices= np.sort(np.concatenate(train_indices))
    X_test = X[test_indices]
    y_test = y[test_indices]
    X_train = X[train_indices]
    y_train = y[train_indices]
    return X_train,X_test, y_train,y_test