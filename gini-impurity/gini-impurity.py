import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    right_len= len(y_right)
    left_len = len(y_left)
    total_n = right_len +left_len
    if total_n == 0:
        return 0.0
    y_right = np.asarray(y_right)
    y_left = np.asarray(y_left)
    # compute right gini 
    def compute_gini(arr):
        if len(arr) == 0 :
            return 0 

        _,count = np.unique(arr,return_counts= True)
        
        prob = count/np.sum(count)
        
        return 1- np.sum(prob **2)

    gini_right = compute_gini(y_right)
    gini_left = compute_gini(y_left)

    
    
     
    
    
    return  (left_len * gini_left  + right_len *gini_right ) / total_n
    
