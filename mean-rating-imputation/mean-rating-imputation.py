import numpy as np
def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    # Write code here
    ratings_matrix = np.asarray(ratings_matrix)
    mask = ratings_matrix!=0
    if mode == "user":
        
        row_sum = np.sum(ratings_matrix,axis=1)
        row_count = np.sum(mask,axis=1)
        user_means = np.where(row_count>0, row_sum/row_count,0)
        user_means=user_means.reshape(-1,1)
        return np.where(mask,ratings_matrix,user_means).tolist()

    row_sum = np.sum(ratings_matrix,axis=0)
    row_count = np.sum(mask,axis=0)
    user_means = np.where(row_count>0, row_sum/row_count,0)
    return np.where(mask,ratings_matrix,user_means).tolist()