import numpy as np
def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    
    series= np.asarray(series)
    for _ in range(order):
        diff=series[1:]-series[:-1]
        series=diff
    return diff.tolist()