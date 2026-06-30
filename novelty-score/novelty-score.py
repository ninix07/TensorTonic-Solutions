import numpy as np
def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    return np.sum(-np.log2(np.asarray(item_counts)/n_users))/len(recommendations)