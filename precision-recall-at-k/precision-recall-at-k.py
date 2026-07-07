import numpy as np
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recommended = np.asarray(recommended)
    relevant = np.asarray(relevant)
    count = np.sum(np.isin(recommended[:k], relevant))

    return [count/k , count/ len(relevant)]
    
    