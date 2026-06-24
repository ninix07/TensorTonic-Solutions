import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    n=len(x)
    x=np.asarray(x)
    if not rng:
        random = np.random.random(size = n)
    else:
        random = rng.random(size=x.shape)
    random = np.where(random < 1-p , 1/(1-p) ,0 )

    return x*random, random
