import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.asarray(x)
    axis=0
    gamma = np.asarray(gamma)
    beta = np.asarray(beta)
    if x.ndim ==4:
        gamma = gamma.reshape(1,gamma.shape[0],1,1,)
        beta = beta.reshape(1,beta.shape[0],1,1,)
        axis =(0,2,3)
    mean = np.mean(x,axis=axis,keepdims=True)

    var = np.mean((x-mean)**2,axis=axis,keepdims=True)

    x_cap = (x- mean) / (np.sqrt(var+eps))
    
    return gamma * x_cap +beta