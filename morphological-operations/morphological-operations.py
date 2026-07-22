import numpy as np
def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """
    # Write code here
    image = np.asarray(image)
    kernel = np.asarray(kernel)
    k_H, k_W = kernel.shape
    H,W = image.shape
    pad_H = k_H//2
    pad_W =k_W//2
    padded_image = np.pad(image ,pad_width =((pad_H,pad_H),(pad_W,pad_W)))
    output= np.zeros((H,W))
    for  i in range(H):
        for  j in range(W):
            window = padded_image[i:i+k_H, j:j+k_W]
            masked = window[kernel==1]
            if operation=="dilate":
                output[i][j] = 1 if np.sum(masked)>0 else 0
            else:
                
                output[i][j] =1 if masked.all() else 0


    return output.tolist()