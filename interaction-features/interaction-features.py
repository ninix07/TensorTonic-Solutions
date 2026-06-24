def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """


    return [ list(x) + [x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x))] for x in X]