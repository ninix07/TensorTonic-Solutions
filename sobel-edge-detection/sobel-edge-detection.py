import numpy as np
def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    # Write code here
    image = np.asarray(image)
    H,W = image.shape
    padded_image = np.pad(image, (1,1), 'constant')
    Kx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])
    Ky = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]])
    output=np.zeros((H,W))
    for  i in range(H):
        for j in range(W):
            neighbours = padded_image[i:i+3, j:j+3]
            G_x = (neighbours * Kx).sum()
            G_y = (neighbours*Ky).sum()
            output[i][j]=np.sqrt((G_x**2)+(G_y**2))


    return output.tolist()
            