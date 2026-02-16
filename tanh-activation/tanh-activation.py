import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x= np.array(x)
    exponent= np.exp(x)
    neg_exp= np.exp(-x)
    return (exponent-neg_exp)/(exponent+neg_exp)