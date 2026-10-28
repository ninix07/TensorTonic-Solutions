import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray, W_xh: np.ndarray,
                W_hh: np.ndarray, b_h: np.ndarray) -> dict:
    """
    Returns hidden_states and final_hidden_state as float64 arrays.
    """
    hidden = h_0.copy()
    hidden_states=[]
    T = X.shape[1]
    for  step in range(T):
        curr_hidden = np.tanh(X[:,step,:]@ W_xh.T + hidden @ W_hh.T +b_h)
        hidden_states.append(curr_hidden)
        hidden = curr_hidden

    return {"hidden_states": np.stack(hidden_states,axis=1), "final_hidden_state": hidden}
        
        