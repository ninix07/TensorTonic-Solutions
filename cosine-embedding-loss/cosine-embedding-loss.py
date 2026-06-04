import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here

    x1= np.asarray(x1)
    x2= np.asarray(x2)

    product = np.dot(x1,x2) 
    x1_norm = np.linalg.norm(x1)
    x2_norm = np.linalg.norm(x2)
    cos_val = product / (x1_norm*x2_norm)
    return (1-cos_val) if label==1 else max(0,cos_val -margin)