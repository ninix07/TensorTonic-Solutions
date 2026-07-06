import numpy as np
def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))

def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """
    n = len(y_list)
    grad = np.asarray(grad)
    s_list = np.asarray(s_list)
    y_list = np.asarray(y_list)
    rho =np.zeros(n)
    alpha = np.zeros(n)
    q = grad.copy()
    for i in range(n-1,-1,-1):
        rho[i] = 1 / _dot(y_list[i], s_list[i])
        alpha[i] = rho[i]* _dot(s_list[i],q)

        q = q - alpha[i]* y_list[i]



    gamma = _dot(s_list[-1],y_list[-1])/_dot(y_list[-1],y_list[-1])

    r = gamma *q

    beta = np.zeros(n)
    for  i in range(0,n):
        beta[i] = rho[i] * _dot(y_list[i],r)

        r= r+ s_list[i]*(alpha[i]-beta[i])


    return -r
        
        



    