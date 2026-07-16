def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    output=[]
    n= len(values)
    for i in range(len(values[:n-window_size+1])):
        output.append(sum(values[i:i+window_size])/window_size)

    return output
        