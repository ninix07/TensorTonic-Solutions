import numpy as np
import numpy.typing as npt


def compute_ddpm_loss(epsilon: list, epsilon_pred: list) -> float:
    """
    Returns the mean DDPM noise-prediction loss.
    """
    epsilon_np_arr: npt.NDArray[np.float64] = np.asarray(epsilon, dtype=np.float64)
    epsilon_pred_np_arr: npt.NDArray[np.float64] = np.asarray(
        epsilon_pred, dtype=np.float64
    )

    return np.round(np.mean((epsilon_np_arr - epsilon_pred_np_arr) ** 2), 6)
