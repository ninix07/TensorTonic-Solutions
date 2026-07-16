import numpy as np
def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if system_type =="regression":
        mae = np.mean(abs(y_true-y_pred))
        rmse = np.sqrt(np.mean((y_true-y_pred)**2))

        return [("mae",mae),("rmse",rmse)]

    elif system_type == "ranking":
        sorted_indices = np.argsort((-y_pred))
        y_pred_sorted = y_pred[sorted_indices]
        y_true_sorted = y_true[sorted_indices]
        y_true_k = y_true_sorted[:3]
        y_pred_sorted_k = y_pred_sorted[:3]

        relevant_in_top3 = np.sum(y_true_k)
        total_relevant = np.sum(y_true) 

        return [("precision_at_3",relevant_in_top3/3),("recall_at_3",relevant_in_top3/total_relevant if total_relevant else 0)]


    else:
        TP = sum(1 for yt,yp in zip(y_true,y_pred) if yt==1 and yp==1)
        TN = sum(1 for yt,yp in zip(y_true,y_pred) if yt==0 and yp==0)
        FP = sum(1 for yt,yp in zip(y_true,y_pred) if yt==0 and yp==1)
        FN = sum(1 for yt,yp in zip(y_true,y_pred) if yt==1 and yp==0)

        n= len(y_true)

        acc = (TP+TN)/n if n else 0
        precision = TP/ (TP+FP) if (TP+FP) else 0
        recall = TP/ (TP+FN) if (TP+FN) else 0
        f1 = 2* precision*recall / (precision+recall) if (precision+recall) else 0

        return [("accuracy", acc), ("f1", f1), ("precision", precision), ("recall", recall)]