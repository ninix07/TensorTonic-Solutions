from collections import Counter
def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here

    count = Counter(values)

    total = sum(count.values())


    return [count[val]/total for val in values]

    