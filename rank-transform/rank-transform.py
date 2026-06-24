from collections import Counter
def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here

    val_df={}
    count_df = Counter(values)
    for i,v in enumerate(sorted(values)):
        val_df[v] = val_df.get(v,0)+i+1

    return [val_df[v]/count_df[v] for v in values]