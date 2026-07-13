import numpy as np

def mean_average_precision(y_true_list, y_score_list, k=None):
    """
    Compute Mean Average Precision (mAP) for multiple retrieval queries.
    """
    # Write code here
    ap_per_query = []
    for y_true, y_score in zip(y_true_list,y_score_list):
        
        y_true= np.asarray(y_true)
        y_score = np.asarray(y_score)
        sorted_indices = np.argsort(-y_score)
    
        y_true_sorted = y_true[sorted_indices]
        r = y_true_sorted.sum()
        if r ==0:
            ap_per_query.append(0)
            continue
        if  k :
            y_true_sorted = y_true_sorted[:k]
    
        precision = np.cumsum(y_true_sorted)/np.arange(1, len(y_true_sorted) + 1)
    
        ap = np.sum(precision*y_true_sorted) / r

        ap_per_query.append(ap)

    return np.mean(ap_per_query) , ap_per_query

    