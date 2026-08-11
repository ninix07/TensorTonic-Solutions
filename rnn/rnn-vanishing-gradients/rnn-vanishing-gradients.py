import numpy as np

def compute_gradient_norm_decay(T: int, W_hh: np.ndarray) -> list:
    """
    Simulate gradient norm decay over T time steps.
    Returns list of gradient norms.
    """
    # YOUR CODE HERE
    spec_norm = np.linalg.norm(W_hh,ord=2)
    rt= [1.0]
    for  i in range(1,T):
        rt.append(rt[i-1]*spec_norm)

    return rt
        