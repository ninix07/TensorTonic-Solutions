import math
import numpy as np

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here
    relevance_scores = np.asarray(relevance_scores)
    sorted_relevance_score = np.sort(relevance_scores)[::-1][:k]
    relevance_scores = relevance_scores[:k]
    idx = np.arange(1,len(relevance_scores)+1)
    dcg =np.sum( ((2**relevance_scores)-1)/np.log2(idx+1))
    idcg = np.sum( ((2**sorted_relevance_score)-1)/np.log2(idx+1))


    return dcg/idcg if idcg > 0 else 0