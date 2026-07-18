import numpy as np
def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here
    n = len(values)
    values = np.asarray(values)
    output_list =[]
    for i in range(n-window_size+1):
        mean =np.mean(values[i:i+window_size])
        variance = np.sqrt(1/window_size * np.sum((values[i:i+window_size]- mean)**2) )
        output_list.append(variance)


    return output_list
    
    