import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)

    dot_product = np.dot(a,b)
    a_norm = np.linalg.norm(a) +1e-15
    b_norm = np.linalg.norm(b) + 1e-15
    return dot_product/ (a_norm *b_norm)    