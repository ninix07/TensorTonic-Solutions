import math
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    n = len(actual_tokens)
    p = [math.log(prob_distributions[t][actual_tokens[t]]) for  t in range(n)]
    l_p = -sum(p)/n

    return math.exp(l_p)
        
        
    
    