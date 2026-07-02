import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.asarray(rater1)
    rater2 = np.asarray(rater2)
    

    p0 = np.sum(rater1==rater2)/len(rater1)

    _,count1 = np.unique(rater1,return_counts=True)
    _,count2 = np.unique(rater2,return_counts=True)

    p_e = np.sum(count1*count2/(len(rater1)**2))
    if p_e ==1:
        return 1
    return (p0 - p_e)/(1-p_e)

    