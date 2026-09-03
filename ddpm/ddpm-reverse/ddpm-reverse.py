import numpy as np


def reverse_step(
    x_t: list, t: int, epsilon_pred: list, betas: list[float], z: list = None
) -> list:
    """
    Returns x at timestep t - 1, rounded to four decimals.
    """
    betas = np.asarray(betas, dtype=np.float64)
    alphas = 1.0 - betas
    alphas_cumprod = np.cumprod(alphas)
    epsilon_pred = np.asarray(epsilon_pred, dtype=np.float64)
    x_t = np.asarray(x_t, dtype=np.float64)
    z = np.asarray(z, dtype=np.float64)
    sqrt_alpha_t = np.sqrt(alphas[t - 1])
    sqrt_one_minus_cum_alpha_t = np.sqrt(1 - alphas_cumprod[t - 1])

    miu_t = (
        x_t - betas[t - 1] * epsilon_pred / sqrt_one_minus_cum_alpha_t
    ) / sqrt_alpha_t

    return (
        np.round(miu_t + np.sqrt(betas[t - 1]) * z, 4) if t > 1 else np.round(miu_t, 4)
    )

