import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    w = np.asarray(w)
    g = np.asarray(g)
    s= np.asarray(s)
    s_t= beta * s +(1-beta)* (g**2)
    w_t = w - (lr*g/((s_t+eps)**0.5))
    return  w_t, s_t