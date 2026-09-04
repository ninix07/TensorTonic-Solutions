import numpy as np
import numpy.typing as npt


def ddpm_sample(
    x_T: list, betas: list[float], epsilon_preds: list, z_values: list
) -> list:
    """
    Returns the final denoised sample rounded to four decimals.
    """

    x_T: npt.NDArray[np.float64] = np.asarray(x_T, dtype=np.float64)
    betas: npt.NDArray[np.float64] = np.asarray(betas, dtype=np.float64)
    epsilon_preds: npt.NDArray[np.float64] = np.asarray(epsilon_preds, dtype=np.float64)
    z_values: npt.NDArray[np.float64] = np.asarray(z_values, dtype=np.float64)
    alphas: npt.NDArray[np.float64] = 1 - betas
    alphas_cumprod: npt.NDArray[np.float64] = np.cumprod(alphas)
    T = len(betas)
    curr_x = x_T
    for i, t in enumerate(range(T - 1, -1, -1)):
        print(f"timestep: {t}")
        beta_t = betas[t]
        epsilon_t = epsilon_preds[i]

        # Compute the mean and variance for the current timestep
        mean_t = (1 / np.sqrt(alphas[t])) * (
            curr_x - (beta_t * epsilon_t / np.sqrt(1 - alphas_cumprod[t]))
        )

        var_t = beta_t

        # Sample from the Gaussian distribution
        curr_x = mean_t + np.sqrt(var_t) * z_values[i] if t > 0 else mean_t

    return np.round(curr_x, 4).tolist()


