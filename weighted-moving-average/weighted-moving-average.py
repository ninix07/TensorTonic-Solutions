import numpy as np
def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    values = np.asarray(values)
    weights = np.asarray(weights)
    k =len(weights)
    output=[]
    for i in range(len(values)-k+1):
        output.append(float(np.sum(values[i:i+k]*weights)/np.sum(weights)))

    return output