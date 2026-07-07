def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hit =0 
    for i,t in enumerate(ground_truth):
        if t[0] in recommendations[i][:k]:
            hit+=1

    return hit/len(ground_truth)