import numpy as np
def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    series = np.asarray(series)
    mean = np.mean(series)
    n=len(series)
    gamma_0= np.sum((series-mean)**2)
    if not gamma_0:
        return [1.0]+[0.0]*(max_lag)

    results = []
    

    for k in range(0,max_lag+1):
        num = np.sum((series[:n-k]-mean)*(series[k:]-mean))
        results.append(num/gamma_0)


    return results

        
        