import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if len(y_true)==0  and len(y_pred)==0 :
        return np.zeros((num_classes,num_classes))
    num_classes = np.max(np.concatenate((y_true,y_pred)))+1 if num_classes is None else num_classes
    indices = y_true *num_classes +y_pred
    conf_matrix = np.bincount(indices,minlength= num_classes*num_classes).reshape(num_classes,num_classes).astype(float)
    
    if normalize =="none":
        return conf_matrix

    elif normalize == "all":
        sum = np.sum(conf_matrix) 
        return conf_matrix/sum if sum else conf_matrix

    elif normalize =="true":
        sum =np.sum(conf_matrix,axis=1,keepdims=True)
        sum = np.where(sum == 0, 1, sum)
        return conf_matrix/sum 

    else:
        sum =np.sum(conf_matrix,axis=0,keepdims=True)
        sum =np.where(sum == 0, 1, sum)
        return conf_matrix/sum 

    
         