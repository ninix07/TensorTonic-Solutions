import numpy as np
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    image = np.asarray(image)
    weights = np.array([0.299, 0.587, 0.114])
    return np.dot(image,weights).tolist()