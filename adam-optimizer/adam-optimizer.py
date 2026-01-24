import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    

    m_t= beta1*m+(1-beta1)*grad
    v_t= beta2*v+(1-beta2)*np.pow(grad,2)
    m_t_cap= m_t/ (1- np.pow(beta1,t))
    v_t_cap= v_t/ (1- np.pow(beta2,t))

    param_t= param - lr * (m_t_cap /(np.pow(v_t_cap,0.5)+eps) )
    return param_t, m_t,v_t