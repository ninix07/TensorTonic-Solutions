import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    w= np.asarray(w)
    g = np.asarray(g)
    G = np.asarray(G)

    G_t = G + (g**2)

    w_t = w - ((lr*g)/(np.sqrt(G_t+eps)))

    return w_t , G_t

    