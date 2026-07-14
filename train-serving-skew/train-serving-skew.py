import numpy as np

def detect_skew(train_dist, serving_dist, threshold=0.2, eps=1e-10):
    """
    Detect train-serving skew using PSI.
    """
    # Write code here
    output={}
    for key in train_dist:
        train_data = np.asarray(train_dist[key])+eps
        serve_data= np.asarray(serving_dist[key])+eps

        psi_val = np.sum((serve_data-train_data)*np.log(serve_data/train_data))
        output[key] = { "psi" : psi_val , "skewed": True if psi_val > threshold else False }


    return output