import numpy as np

def vae_forward(x: np.ndarray, epsilon: np.ndarray,
                W_mu: np.ndarray, b_mu: np.ndarray,
                W_logvar: np.ndarray, b_logvar: np.ndarray,
                W_dec: np.ndarray, b_dec: np.ndarray) -> dict:
    """
    Returns reconstruction, mu, log_var, and z as float64 arrays.
    """
    miu = np.dot(x, W_mu) + b_mu

    log_var = np.dot(x, W_logvar) + b_logvar

    Z = miu + np.exp(log_var/2) * epsilon
    ins = np.dot(Z,W_dec)+b_dec
    return {"reconstruction": 1/ (1+ np.exp(-ins)), "mu": miu , "log_var": log_var , "z" :Z }