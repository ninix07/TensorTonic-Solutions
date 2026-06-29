import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1 = np.asarray(Z1) 
    Z2 = np.asarray(Z2)

    S = np.dot(Z1,Z2.T) / temperature
    S = S- np.max(S)

    return - np.mean(np.diag(np.log(np.exp(S)/np.sum(np.exp(S),axis=1, keepdims=True))))