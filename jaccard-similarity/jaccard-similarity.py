def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here

    if not set_a and not set_b:
        return 0.0

    union=set()
    intersection=set()

    for a  in set_a:
        if a not in union:
            union.add(a)
        if a in set_b:
            intersection.add(a)

    for b in set_b:
        if b not in union:
            union.add(b)


    return len(intersection)/len(union)
    