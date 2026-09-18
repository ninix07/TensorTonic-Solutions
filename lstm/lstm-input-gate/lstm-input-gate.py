import numpy as np

def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))

def input_gate(h_prev: np.ndarray, x_t: np.ndarray,
               W_i: np.ndarray, b_i: np.ndarray,
               W_c: np.ndarray, b_c: np.ndarray) -> dict:
    """
    Returns input_gate and candidate_state as float64 arrays.
    """
    concat_val = np.concat((h_prev,x_t),axis=-1)
    i_t = sigmoid(np.dot(W_i, concat_val.T)+b_i).T
    can_t= np.tanh(np.dot(W_c, concat_val.T)+b_c).T



    return {
        "input_gate" : i_t,
        "candidate_state" : can_t
    }