import numpy as np
def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    bins = np.linspace(0, 1, n_bins + 1)

    ece_bin = np.zeros(n_bins)
    for i in range(n_bins):
        pred_in_bin = (bins[i+1] > y_pred if i < n_bins-1 else bins[i+1] >= y_pred) & (y_pred >= bins[i]) 
        if np.sum(pred_in_bin)==0:
            continue
        acc= np.mean(y_true[pred_in_bin])
        conf= np.mean(y_pred[pred_in_bin])
        ece_bin[i] = np.sum(pred_in_bin) *(abs(acc-conf))/len(y_pred)

    return np.sum(ece_bin)