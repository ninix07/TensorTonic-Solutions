import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    entropy_y = _entropy(y)
    y_left = y[split_mask]
    y_right = y[~split_mask]
    entropy_y_left = _entropy(y_left) *len(y_left)
    entropy_y_right = _entropy(y_right) *len(y_right)

    return entropy_y - (entropy_y_left+entropy_y_right)/len(y)
    