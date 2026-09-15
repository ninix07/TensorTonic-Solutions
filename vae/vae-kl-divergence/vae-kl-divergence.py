import numpy as np

def kl_divergence(mu: np.ndarray, log_var: np.ndarray) -> float:
    """
    Returns the batch-mean KL divergence as a Python float.
    """
    inner_val = 1+ log_var - (mu**2) - np.exp(log_var)
    sum_val = np.sum(inner_val, axis=-1)
    return -0.5* np.mean(sum_val)