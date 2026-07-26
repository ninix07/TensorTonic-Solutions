import numpy as np
def baseline_predict(ratings_matrix, target_pairs):
    """
    Compute baseline predictions using global mean and user/item biases.
    """
    # Write code here
    ratings_matrix = np.asarray(ratings_matrix)
    target_pairs = np.asarray(target_pairs)
    mask = ratings_matrix != 0
    global_mean = np.sum(ratings_matrix)/np.sum(mask)

    user_mean = np.sum(ratings_matrix,axis=1)/np.sum(mask,axis=1)
    item_mean =np.sum(ratings_matrix,axis=0)/np.sum(mask,axis=0)

    user_bias = user_mean-global_mean
    item_bias = item_mean - global_mean

    predictions = []
    for u, i in target_pairs:
        pred = global_mean +user_bias[u]+item_bias[i]
        predictions.append(pred)

    return predictions