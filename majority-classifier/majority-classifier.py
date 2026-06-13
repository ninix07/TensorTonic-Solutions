import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y_train= np.asarray(y_train)
    n= len(X_test)
    val,counts = np.unique(y_train, return_counts=True)
    number= val[np.argmax(counts)]
    return np.full(n,number)