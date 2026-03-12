import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    positive_dist= np.linalg.norm(np.asarray(anchor) - np.asarray(positive), axis = -1)**2 
    negative_dist= np.linalg.norm(np.asarray(anchor) - np.asarray(negative), axis=-1)**2

    return np.mean(np.maximum(0,positive_dist-negative_dist +margin))