def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    return [ordering.index(val) for val in values]