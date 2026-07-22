import numpy as np
def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here
    image = np.asarray(image)
    H,W= image.shape

    cy = (H-1)/2
    cx = (W-1)/2
    angle = np.deg2rad(angle_degrees)
    cos = np.cos(angle)
    sin = np.sin(angle)
    output = np.zeros((H,W))
    for  i in range(H):
        for j in range(W):
            dy=i-cy
            dx= j-cx
            src_y = int(np.round(cy +dy*cos +dx*sin))
            src_x = int(np.round(cx - dy*sin +dx*cos))
            if src_x < W and src_y <H:
                output[i][j]= image[src_y,src_x]


    return output.tolist()
            