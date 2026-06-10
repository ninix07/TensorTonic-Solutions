import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x= np.asarray(x)
    q= np.asarray(q)

    return np.asarray([np.percentile(x,percentile ,method='linear') for percentile in q]) 