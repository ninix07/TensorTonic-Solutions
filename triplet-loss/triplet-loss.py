import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor= np.asarray(anchor)
    positive= np.asarray(positive)
    negative= np.asarray(negative)
    positive_dist= np.linalg.norm(anchor-positive, axis = -1)**2 
    negative_dist= np.linalg.norm(anchor-negative, axis=-1)**2
    loss= np.maximum(0,positive_dist-negative_dist +margin)
    return np.mean(loss)