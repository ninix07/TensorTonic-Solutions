import numpy as np
def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    # Write code here
    image = np.asarray(image)
    H,W = image.shape
    hist = np.bincount(image.flatten(), minlength =256)

    cdf = np.cumsum(hist)

    cdf_min =cdf[cdf>0].min()
    denominator = cdf[255]- cdf_min
    new_val = np.round((cdf[image] - cdf_min) / (denominator) * 255) if denominator else np.zeros((H,W))

    return new_val.tolist()