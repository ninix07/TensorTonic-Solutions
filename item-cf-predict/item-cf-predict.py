import numpy as np
def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """
    # Write code here
    user_ratings = np.asarray(user_ratings)
    item_similarities = np.asarray(item_similarities)
    mask = np.ones(len(user_ratings),dtype=bool)
    mask[target]= 0
    user_ratings = user_ratings[mask]
    item_similarities =item_similarities[mask]
    valid = (user_ratings != 0) & (item_similarities > 0)
    user_ratings = user_ratings[valid]
    item_similarities= item_similarities[valid]
    if np.sum(item_similarities)==0 :
        return 0.0
    return np.sum(user_ratings*item_similarities)/np.sum(item_similarities) 