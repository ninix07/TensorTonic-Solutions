def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    stopwords=set(stopwords)
    rt_list=[token for token in tokens if token not in stopwords ]

    return rt_list