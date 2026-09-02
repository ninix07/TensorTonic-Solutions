import numpy as np


def get_alpha_bar(betas):
    """
    Compute cumulative product of (1-beta).
    Return list of floats rounded to 6 decimals.
    """
    betas = np.asarray(betas)
    alphas = 1.0 - betas
    alpha_bar = np.cumprod(alphas)
    return np.round(alpha_bar, 6).tolist()


def forward_diffusion(x_0, t, betas, epsilon):
    """
    Returns: tuple of (np.ndarray x_t , np.ndarray epsilon) with same shape as x_0
    """
    x_0 = np.asarray(x_0)
    epsilon = np.asarray(epsilon)
    alpha_bar = get_alpha_bar(betas)
    alpha_bar = np.asarray(alpha_bar)

    #timestep is calculated from 1 while the indexing is from 0, so we need to subtract 1 from t to get the correct index
    x_t = np.sqrt(alpha_bar[t-1]) * x_0 + np.sqrt(1 - alpha_bar[t-1]) * epsilon

    return x_t.tolist()

