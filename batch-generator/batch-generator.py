import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    n=len(y)
    X= np.asarray(X)
    y=np.asarray(y)

    if rng is None:
        rng = np.random

    indices = [i for i in range(n)]
    rng.shuffle(indices)

    for start in range(0, n, batch_size):
        batch_idx = indices[start:start+batch_size]
        if drop_last and len(batch_idx) < batch_size:
            break
        yield X[batch_idx], y[batch_idx]
    