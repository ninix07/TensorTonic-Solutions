def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    n = len(returns)
    output = []
    for i in range(n):
        curr_gain = 1+output[-1] if output else 1
        curr_gain = curr_gain*(1+returns[i])
        output.append(curr_gain-1)

    return output
    