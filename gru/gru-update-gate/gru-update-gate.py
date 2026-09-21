import numpy as np

def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))

def update_gate(h_prev: np.ndarray, x_t: np.ndarray,
          W_z: np.ndarray, b_z: np.ndarray) -> np.ndarray:
    """
    Returns the float64 update-gate values.
    """
    concat_val = np.concat((h_prev,x_t),axis=-1)
    inside_val = np.dot(concat_val,W_z.T) +b_z
    return sigmoid(inside_val)