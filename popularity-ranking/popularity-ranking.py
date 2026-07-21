def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here

    rank = []


    for  r,vote in items:
        wr= (vote *r  + min_votes*global_mean )/(vote+min_votes)

        rank.append(wr)



    return rank        