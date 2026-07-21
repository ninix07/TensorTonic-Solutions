def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    non_rated_indices = [i for i in range(len(scores)) if i not in rated_indices]

    non_rated_indices = sorted(non_rated_indices, key = lambda x: -scores[x])
    
    return non_rated_indices[:k]