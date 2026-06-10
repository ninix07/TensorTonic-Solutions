import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x= np.asarray(x)
    mean = np.mean(x)
    s_squred = np.sum((x-mean)**2)/ (len(x)-1)
    return s_squred, s_squred**0.5
    