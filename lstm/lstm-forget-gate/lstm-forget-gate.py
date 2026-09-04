import numpy as np
import numpy.typing as npt

def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))

def forget_gate(h_prev: np.ndarray, x_t: np.ndarray,
                W_f: np.ndarray, b_f: np.ndarray) -> np.ndarray:
    """
    Returns the float64 forget-gate values.
    """
    first_term:npt.NDArray = np.concatenate([h_prev,x_t],axis=-1) @ W_f.T


    return 1/(1+np.exp(-(first_term+b_f)))