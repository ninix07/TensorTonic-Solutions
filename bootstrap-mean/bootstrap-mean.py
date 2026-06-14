import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    means = np.zeros(n_bootstrap)
    x= np.asarray(x)
    if not rng:
        rng = np.random.default_rng()
    for i in range(n_bootstrap):
        idx = rng.integers(0,len(x), size=len(x))
        boot= x[idx]
        means[i]= np.mean(boot)

    alpha = (1-ci)/2
    lower = np.quantile(means, alpha)
    upper = np.quantile(means, 1-alpha)

    return means,lower,upper
