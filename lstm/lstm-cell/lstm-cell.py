import numpy as np

def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0/(1.0+np.exp(-np.clip(x,-500,500)))

def lstm_cell(x_t: np.ndarray, h_prev: np.ndarray, C_prev: np.ndarray,
              W_f: np.ndarray, W_i: np.ndarray, W_c: np.ndarray, W_o: np.ndarray,
              b_f: np.ndarray, b_i: np.ndarray, b_c: np.ndarray, b_o: np.ndarray) -> dict:
    """
    Returns hidden_state and cell_state as float64 arrays.
    """
    concat_val = np.concat((h_prev,x_t),axis=-1).T

    f_t = sigmoid(np.dot(W_f,concat_val)+b_f).T
    i_t = sigmoid(np.dot(W_i,concat_val)+b_i).T
    C_tilde = np.tanh(np.dot(W_c,concat_val)+b_c).T

    C_t = f_t * C_prev + i_t * C_tilde
    o_t = sigmoid(np.dot(W_o,concat_val)+b_o).T
    h_t = o_t * np.tanh(C_t)
    return {"hidden_state": h_t,"cell_state" :C_t }