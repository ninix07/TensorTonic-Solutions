def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here

    max_lag = max(lags)
    result = []

    for i in range(max_lag,len(series)):
        result.append([ series[i-lag] for lag in lags ])


    return result