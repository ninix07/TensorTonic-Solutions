import numpy as np
def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    predictions= np.asarray(predictions)
    targets = np.asarray(targets)

    prob_t = np.where(targets==1, predictions, 1-predictions)
    
    loss= - alpha * ((1-prob_t)**gamma) * np.log(prob_t)
    return np.mean(loss)