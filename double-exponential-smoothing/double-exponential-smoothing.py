def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here
    level =[series[0]]
    trend =[series[1]-series[0]]

    for i in range(1,len(series)):
        curr_level = alpha*series[i]+(1-alpha)*(level[-1]+trend[-1])
        curr_trend = beta*(curr_level-level[-1]) +(1-beta)*trend[-1]
        
        level.append(curr_level)
        trend.append(curr_trend)

    return level