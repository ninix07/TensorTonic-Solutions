import numpy as np

def get_factorial(k):
    if k <=1:
        return 1
    return np.exp(np.sum(np.log([i for i in range(1,k+1)])))

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    pmf=  np.exp(-lam) * (lam**k)/ get_factorial(k)

    cdf = np.sum([np.exp(-lam) * (lam**i)/ get_factorial(i) for i in range(k+1)])
    return pmf ,cdf