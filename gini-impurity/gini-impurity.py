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
    gini_right =0
    gini_left= 0
    # compute right gini 
    if right_len > 0:
        y_right = np.asarray(y_right)
        _,count = np.unique(y_right,return_counts= True)
        
        prob_right = count/np.sum(count)
        
        gini_right = 1- np.sum(prob_right **2)
    
     # compute right gini 
    if left_len > 0:
        y_left = np.asarray(y_left)
        _,count = np.unique(y_left,return_counts= True)
        
        prob_left = count/np.sum(count) 
        
        gini_left = 1- np.sum(prob_left **2)
    
    
    return  (left_len * gini_left  + right_len *gini_right ) / total_n
    
