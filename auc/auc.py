import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    n,m = len(fpr), len(tpr)
    fpr = np.asarray(fpr)
    tpr = np.asarray(tpr)
    if m!=n :
        raise ValueError

    return np.trapezoid(y=tpr,x=fpr)