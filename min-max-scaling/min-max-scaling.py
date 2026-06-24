import numpy as np
def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    
    data= np.asarray(data)
    min = np.min(data,axis=0)
    max = np.max(data,axis=0)
    range_val = max - min
    denominator = np.where(range_val == 0, 1, range_val)

    scaled_data = (data - min) / denominator
    scaled_data = np.where(range_val == 0, 0.0, scaled_data)
    
    return scaled_data.tolist()