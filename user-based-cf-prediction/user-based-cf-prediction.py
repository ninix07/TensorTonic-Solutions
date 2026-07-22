import numpy as np
def user_based_cf_prediction(similarities, ratings):
    """
    Predict a rating using user-based collaborative filtering.
    """
    # Write code here

    similarities = np.asarray(similarities)
    ratings = np.asarray(ratings)
    pos_similarities = similarities[similarities>=0]
    ratings = ratings[similarities>=0]
    if not np.sum(pos_similarities):
        return 0
    return np.sum(pos_similarities*ratings)/np.sum(pos_similarities)