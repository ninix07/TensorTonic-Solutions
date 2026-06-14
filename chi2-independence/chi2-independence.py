import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    C = np.asarray(C)
    col_sum = np.sum(C, axis=0)
    row_sum = np.sum(C, axis=1)
    total = np.sum(C)
    
    E = np.outer(row_sum, col_sum) / total

    chi = np.sum(((C-E)**2) / E)
    return chi,E