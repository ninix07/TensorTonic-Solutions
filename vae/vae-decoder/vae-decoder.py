import numpy as np

def vae_decoder(z: np.ndarray, W_dec: np.ndarray, b_dec: np.ndarray) -> np.ndarray:
    """
    Returns the float64 reconstruction with shape (B, D).
    """
    sig_ins = np.dot(z,W_dec) + b_dec
    X_bar = 1/(1+np.exp(-sig_ins))


    return X_bar