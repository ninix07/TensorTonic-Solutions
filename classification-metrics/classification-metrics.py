import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    classes = np.unique(np.concatenate((y_true, y_pred)))

    y_true_c = y_true[:,None]==classes[None,:]
    y_pred_c = y_pred[:,None]==classes[None,:]

    tp_c = np.sum(y_true_c & y_pred_c, axis=0)
    fp_c = np.sum(~y_true_c & y_pred_c,axis=0)
    fn_c = np.sum(y_true_c & ~y_pred_c,axis=0)

    precision_c = tp_c / (tp_c + fp_c)
    recall_c    = tp_c / (tp_c + fn_c)
    f1_c        = 2 * precision_c * recall_c / (precision_c + recall_c)

    precision , recall , f1=0,0,0
    
    if average == "macro":
        precision = np.mean(precision_c)
        recall = np.mean(recall_c)
        f1 = np.mean(f1_c)
    elif average == "micro":
        tp_total = np.sum(tp_c)
        fp_total = np.sum(fp_c)
        fn_total = np.sum(fn_c)
        precision = tp_total / (tp_total + fp_total)
        recall = tp_total / (tp_total + fn_total)
        f1 = 2 * precision * recall / (precision + recall)
    elif average == "weighted":
        support_c = np.sum(y_true_c, axis=0)
        precision = np.sum(precision_c * support_c) / np.sum(support_c)
        recall = np.sum(recall_c * support_c) / np.sum(support_c)
        f1 = np.sum(f1_c * support_c) / np.sum(support_c)

    else:
        idx =np.where(classes == pos_label)[0][0]
        f1 = f1_c[idx]
        precision =precision_c[idx]
        recall= recall_c[idx]


    return {"accuracy": np.mean(y_true==y_pred), "precision": precision ,"recall": recall ,"f1": f1}