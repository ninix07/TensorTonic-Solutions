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
        count_df = Counter(curr_sample)

        max_count= max(count_df.values())

        classes=[key for key,val in count_df.items() if val ==max_count ]

        class_pred[i]= min(classes)


    return class_pred.tolist()