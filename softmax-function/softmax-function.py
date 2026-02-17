import numpy as np

def softmax(x):
    x = np.array(x)

    if x.ndim == 1:
        max_x = np.max(x)
        e = np.exp(x - max_x)
        return e / np.sum(e)

    elif x.ndim == 2:
        max_x = np.max(x, axis=1, keepdims=True)
        e = np.exp(x - max_x)
        return e / np.sum(e, axis=1, keepdims=True)
