import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here
    
    sample_idx = np.arange(N)
    if shuffle:
        if rng:
            sample_idx= rng.permutation(sample_idx)
        else:
            np.random.shuffle(sample_idx)


    
    folds = np.array_split(sample_idx,k)

    results = [(np.concatenate(folds[:i]+folds[i+1:]), folds[i]) for i in range(k)]
    return results

    
    