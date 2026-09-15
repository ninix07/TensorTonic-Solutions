import numpy as np

def vae_loss(x: np.ndarray, reconstruction: np.ndarray,
             mu: np.ndarray, log_var: np.ndarray) -> dict:
    """
    Returns total_loss, reconstruction_loss, and kl_loss as Python floats.
    """

    r_loss = np.mean(np.sum((x-reconstruction)**2,axis=-1))
    kl_loss = -0.5* np.mean(np.sum(1+log_var-(mu**2)-np.exp(log_var), axis=-1))
    return {"total_loss" : r_loss+kl_loss , "reconstruction_loss": r_loss , "kl_loss" : kl_loss}
    