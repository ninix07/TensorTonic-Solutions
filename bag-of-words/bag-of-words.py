import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """

    return np.array([tokens.count(v) for v in vocab], dtype=int)
        