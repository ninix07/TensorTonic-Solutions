def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    change = []

    n = len(series)
    for i in range(1,n):
        change.append((series[i]-series[i-1])/series[i-1] if series[i-1] else 0.0)

    return change