import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    upper_mask = np.triu(np.ones_like(scores), k=1)

    masked = np.where(upper_mask, mask_value,scores)

    return masked