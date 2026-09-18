import numpy as np

def discriminator(x: np.ndarray, W: np.ndarray) -> np.ndarray:
    """
    Returns discriminator probabilities as a float64 array with shape (B, 1).
    """
    inner_el = np.dot(x,W)

    return 1/(1+np.exp(-inner_el))
    