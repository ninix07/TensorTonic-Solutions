def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    n = len(values)
    output=[]
    index_get = window_size//2
    for i in range(n-window_size+1):
        curr_vals = values[i:i+window_size]
        curr_vals = sorted(curr_vals)
        median = curr_vals[index_get] if window_size%2!=0 else (curr_vals[index_get] +curr_vals[index_get-1])/2 
        output.append(median)

    return output