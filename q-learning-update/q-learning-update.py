import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    Q = np.asarray(Q,dtype=float)
    Q_new = Q.copy()
    
    err = r+ gamma*np.max(Q[s_next,:])- Q[s,a]

    Q_new[s,a]= Q[s,a]+alpha*err
    return Q_new.tolist()