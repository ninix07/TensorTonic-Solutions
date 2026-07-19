import numpy as np
def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    # Write code here
    image = np.asarray(image)
    H,W = image.shape
    output = np.zeros((new_h,new_w))

    for i in range(new_h):
        for j in range(new_w):
            src_y = i * (H-1)/(new_h-1) if new_h >1 else 0
            src_x = j * (W-1)/(new_w-1) if new_w > 1 else 0
            
            y_0 = int(np.floor(src_y))
            x_0  = int(np.floor(src_x))
            dx = src_x-x_0
            dy = src_y-y_0

            y_1= min(y_0+1,H-1)
            x_1 = min(x_0+1,W-1)

            output[i][j] = image[y_0][x_0]*(1-dy)*(1-dx)+ image[y_1][x_0]*dy*(1-dx) + image[y_0][x_1] * (1-dy)*dx + image[y_1][x_1] * dy *dx


    return output.tolist()