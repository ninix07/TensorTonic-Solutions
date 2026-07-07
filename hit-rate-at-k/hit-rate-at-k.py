def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hit =0 

    hit = sum([1 if t[0] in recommendations[i][:k] else 0 for i,t in enumerate(ground_truth)])

    return hit/len(ground_truth)