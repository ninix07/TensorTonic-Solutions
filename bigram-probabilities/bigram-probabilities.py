from collections import Counter
def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    # Your code here
   
    bigram_counts =Counter(tuple(tokens[i:i+2]) for i in range(len(tokens)-1))

    unigram_counts = Counter(tokens[:-1])


    probs = {}
    vocab =set(tokens)
    for w1 in vocab:
        for w2 in vocab:
            probs[(w1,w2)] = (bigram_counts.get((w1,w2), 0) + 1) / (unigram_counts[w1] + len(vocab))


    return bigram_counts,probs