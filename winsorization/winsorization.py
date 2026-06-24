import math
def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    # Write code here
    n =len(values)
    k_lower = (n-1) *lower_pct /100
    k_upper = (n-1) * upper_pct/100

    low_val = values[math.floor(k_lower)]+ (k_lower-math.floor(k_lower))* (values[math.ceil(k_lower)]-values[math.floor(k_lower)])
    upper_val= values[math.floor(k_upper)]+ (k_upper-math.floor(k_upper))* (values[math.ceil(k_upper)]-values[math.floor(k_upper)])


    return [max(low_val, min(upper_val, val)) for val in values]