import numpy as np

def decision_tree_split(X, y):
    """
    Find the best feature and threshold to split the data.
    """
    X= np.asarray(X)
    y= np.asarray(y)
    def get_gini(y):
        _,counts = np.unique(y,return_counts=True)
        prob = counts / np.sum(counts)

        return 1- np.sum(prob**2)


    def get_gini_split(y_left, y_right):
        gini_left =get_gini(y_left)
        gini_right= get_gini(y_right)

        return (len(y_left)*gini_left + len(y_right)*gini_right)/(len(y_left)+len(y_right))


    best_feature =None
    best_threshold= None
    best_gini = float('inf')
    parent_gini =get_gini(y)
    for i in range(X.shape[1]):
        unique_vals = np.unique(X[:,i])
        thresholds = (unique_vals[:-1] +unique_vals[1:]) /2

        for threshold in thresholds:
            y_left = y[X[:,i]<=threshold]
            y_right = y[X[:,i] > threshold]

            gini_split = get_gini_split(y_left,y_right)

            if gini_split < best_gini:
                best_feature =i
                best_threshold= threshold
                best_gini = gini_split


    return [best_feature,best_threshold]
        