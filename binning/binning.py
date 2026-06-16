import math
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    if len(set(values))==1:
        return [0 for _ in range(len(values))]
    max_val = max(values)
    min_val = min(values)

    w= (max_val-min_val)/num_bins

    bin = [min(math.floor((val - min_val)/w),num_bins-1) for val in values]

    return bin