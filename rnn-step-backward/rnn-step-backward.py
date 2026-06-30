import numpy as np

def rnn_step_backward(dh, cache):
    """
    Returns:
        dx_t: gradient wrt input x_t      (shape: D,)
        dh_prev: gradient wrt previous h (shape: H,)
        dW: gradient wrt W               (shape: H x D)
        dU: gradient wrt U               (shape: H x H)
        db: gradient wrt bias            (shape: H,)
    """
    # Write code here
    dh = np.asarray(dh)


    x_t = np.asarray(cache[0])
    h_prev = np.asarray(cache[1])
    h_t = np.asarray(cache[2])
    W = np.asarray(cache[3])
    U = np.asarray(cache[4])
    b = np.asarray(cache[5])


    dz = dh *(1-np.pow(h_t,2))
    db= dz
    d_x_t = W.T @ dz
    dh_prev = U.T @ dz
    dU = np.outer(dz, h_prev)
    dW= np.outer(dz,x_t)

    return d_x_t,dh_prev,dW,dU,db
    

    
    

