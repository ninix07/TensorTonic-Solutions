import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    num = np.sum((y_true-y_pred)**2)
    den= np.sum((y_true-np.mean(y_true))**2)

    if len(np.unique(y_true))==1:
        if (y_pred==y_true).all():
            return 1.0
        return 0.0
    return 1- (num/den) 