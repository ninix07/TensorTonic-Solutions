import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x= np.asarray(x,dtype=float)
    vectorized_erf = np.vectorize(math.erf)
    erf_x = vectorized_erf(x/ np.sqrt(2))
    cdf= 1+erf_x
    return x*cdf/2
