import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    dot_product= np.dot(a,b)
    a_norm= np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    if a_norm > 0.0 and b_norm > 0.0:
        return (dot_product)/(a_norm*b_norm)
    else:
        return 0.0