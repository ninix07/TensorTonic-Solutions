import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    image = np.asarray(image,dtype=np.int64).flatten()

    return np.bincount(image,minlength=256).tolist()

    