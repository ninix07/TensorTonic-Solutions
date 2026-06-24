import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    if not num_classes:
        num_classes= len(set(y))

    rt_list=[]
    
    for class_val in y:
        curr_encoding = np.zeros(num_classes)
        curr_encoding[class_val]=1
        rt_list.append(curr_encoding.tolist())
    return rt_list