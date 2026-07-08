from collections import Counter
def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    words = [word for sentence in sentences for word in sentence]

    return Counter(words)
    