import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    F,_,u,v= W.shape
    N,_,h,w = x.shape
    OH = h-u +1
    OW = w-v +1
    out = np.zeros((N,F,OH,OW))
    for i in range(OH):
        for j in range(OW):
            for f in range(F):
                patch = x[:, :, i:i+u, j:j+v]
                out[:,f,i,j]= np.sum(patch*W[f], axis=(1,2,3)) + b[f]

    return out