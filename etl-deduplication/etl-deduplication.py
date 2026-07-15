def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    # Write code here
    output = {}
    
    for r in records:
        output_key = tuple(r[key] for key in key_columns)
        if output.get(output_key) is None:
            output[output_key] = r
            continue
        if strategy =="last":
            output[output_key] = r
        elif strategy =="most_complete":
            curr_val = output[output_key].values()
            new_val = r.values()
            curr_count = sum([v is not None for v in curr_val])
            new_count = sum([v is not None for v in new_val])
            if new_count > curr_count :
                output[output_key] = r

            

    return list(output.values())