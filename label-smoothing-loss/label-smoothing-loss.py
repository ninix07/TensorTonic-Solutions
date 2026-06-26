import numpy as np
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    K = len(predictions)
    predictions=np.asarray(predictions)
    mask = (np.arange(K) == target)


    loss = np.where(mask, (1-epsilon)+(epsilon/K),epsilon/K)

    return -np.sum(loss * np.log(predictions))

    