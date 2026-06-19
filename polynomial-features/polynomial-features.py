import numpy as np
def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    polynomial = np.zeros((len(values),degree+1))
    polynomial = [[value**j for j in range(degree+1)] for value in values ]
    return polynomial