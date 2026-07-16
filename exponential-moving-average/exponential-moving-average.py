def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    EMA= [values[0]]

    for i in range(1,len(values)):
        EMA.append(alpha*values[i]+(1-alpha)*EMA[-1])

    return EMA