import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y= np.asarray(y)
    y_unique, y_counts = np.unique_counts(y)
    num_class = len(y_unique)
       
    return - np.sum(y_counts *np.log2(y_counts/np.sum(y_counts))/np.sum(y_counts))

    