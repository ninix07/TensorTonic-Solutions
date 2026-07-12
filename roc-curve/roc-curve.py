import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    sorted_indices = np.lexsort((y_true,-y_score))

    sorted_labels = y_true[sorted_indices]
    sorted_scores = y_score[sorted_indices]

    cum_labels = np.cumsum(sorted_labels)
    cum_fp = (np.arange(len(sorted_labels))+1)- cum_labels

    sorted_score_diff = np.diff(sorted_scores)
    change_points = np.where(sorted_score_diff != 0)[0]
    change_points = np.append(change_points,len(sorted_scores)-1)
    threshold = sorted_scores[change_points]
    tp = cum_labels[change_points]
    fp = cum_fp[change_points]
    p = y_true.sum()
    n = len(y_true)-p
    return  np.concatenate(([0],fp/n)), np.concatenate(([0],tp/p)) ,np.concatenate(([np.inf],threshold))