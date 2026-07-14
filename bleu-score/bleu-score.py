from collections import Counter
import math
def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    # Write code here
    if len(candidate) ==0:
        return 0.0
    precisions =[]
    for n in range(1,max_n+1):
        candidate_counts = Counter(tuple(candidate[i:i+n]) for i in range(len(candidate)-n+1))
        ref_counts = Counter(tuple(reference[i:i+n]) for i in range(len(reference)-n+1))

        numerator_counts = sum(min(candidate_counts[ng],ref_counts.get(ng,0)) for ng in candidate_counts)
        denominator = sum(candidate_counts.values())
    
        precisions.append(numerator_counts/denominator)
    

    geo_mean =math.exp( (1/max_n)* sum(math.log(p) for  p in precisions))
    c= len(candidate)
    r = len(reference)
    BP = 1 if c>= r else math.exp(min(0,1-(r/c)))
    return BP* geo_mean