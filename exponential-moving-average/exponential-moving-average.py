def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    # Write code here
    EMA= [values[0]]

    for i in range(1,len(values)):
        EMA.append( alpha * values[i] + (1-alpha)* EMA[i-1])


    return EMA

    