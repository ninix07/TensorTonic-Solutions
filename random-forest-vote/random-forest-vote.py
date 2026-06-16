import numpy as np
from collections import Counter
def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    predictions = np.asarray(predictions)

    num_of_columns = predictions.shape[1]

    class_pred=np.zeros(predictions.shape[1])

    for i in range(num_of_columns):
        curr_sample = predictions[:,i]
        counts = np.bincount(curr_sample)

        max_count= counts.max()

        class_pred[i]= np.min(np.where(counts==max_count))


    return class_pred.tolist()