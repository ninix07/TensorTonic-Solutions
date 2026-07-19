import numpy as np
def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    # Write code here
    image = np.asarray(image)
    kernel = np.asarray(kernel)

    H,W = image.shape
    kh,kw = kernel.shape

    H_out = int(np.floor((H+2*padding-kh)/stride)+1)
    W_out = int(np.floor((W+2*padding-kw)/stride)+1)

    padded_image = np.pad(image , ((padding,padding),(padding,padding)),mode='constant')
    output = np.zeros((H_out,W_out))

    for i in range(H_out):
        for j in range(W_out):
            row_start = i*stride
            col_start = j*stride
            patch = padded_image[row_start:row_start+kh, col_start:col_start+kw]
            output[i][j] = np.sum(patch*kernel)

    return output.tolist()