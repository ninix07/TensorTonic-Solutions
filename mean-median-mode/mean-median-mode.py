import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    value,counts = np.unique(x,return_counts= True)
    node_index = np.argmax(counts)
    return np.mean(x), np.median(x), x[node_index]