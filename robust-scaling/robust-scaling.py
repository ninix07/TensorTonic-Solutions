import numpy as np
def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here

    if len(values)==0:
        return []
    if len(values) ==1 :
        return [0]
    values= np.asarray(values)
    sorted_arr = np.sort(values)
    n = len(sorted_arr)
    mid = n // 2
    median = np.median(sorted_arr)
    
    if n % 2 == 0:
        lower, upper = sorted_arr[:mid], sorted_arr[mid:]
    else:
        lower, upper = sorted_arr[:mid], sorted_arr[mid+1:]
    
    q1, q3 = np.median(lower), np.median(upper)
    
    iqr = q3 - q1
    denominator = np.where(iqr == 0, 1, iqr)

    scaled_data = (values - median) / denominator
    
    return scaled_data.tolist()