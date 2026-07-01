import numpy as np

def adadelta_step(w, grad, E_grad_sq, E_update_sq, rho=0.9, eps=1e-6):
    """
    Perform one AdaDelta update step.
    """
    # Write code here
    w = np.asarray(w)
    grad = np.asarray(grad)

    E_grad_sq = np.asarray(E_grad_sq)
    E_update_sq= np.asarray(E_update_sq)

    E_grad_sq_t = rho *E_grad_sq + (1-rho)*(grad**2)

    param_update = -((E_update_sq+eps)**0.5) /((E_grad_sq_t+eps)**0.5) *grad

    E_update_sq_t = rho * E_update_sq + (1-rho)* (param_update**2)

    w_t = w + param_update


    return w_t , E_grad_sq_t,E_update_sq_t