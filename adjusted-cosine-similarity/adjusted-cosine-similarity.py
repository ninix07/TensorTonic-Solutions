import numpy as np
def adjusted_cosine_similarity(ratings_matrix, item_i, item_j):
    """
    Compute adjusted cosine similarity between two items.
    """
    # Write code here
    ratings_matrix = np.asarray(ratings_matrix)
    j_val= ratings_matrix[:,item_j]
    i_val = ratings_matrix[:,item_i]
    mask = (j_val!=0) & (i_val != 0)
    i_val = i_val[mask]
    j_val = j_val[mask]
    rated_mask = ratings_matrix != 0
    row_sums = np.sum(ratings_matrix, axis=1)
    row_count = np.sum(rated_mask, axis=1)
    user_means = row_sums / row_count
    user_means= user_means[mask]

    i_centered = i_val-user_means
    j_centered = j_val-user_means

    return np.sum(i_centered*j_centered)/(np.sqrt(np.sum(i_centered**2))*np.sqrt(np.sum(j_centered**2)))
    