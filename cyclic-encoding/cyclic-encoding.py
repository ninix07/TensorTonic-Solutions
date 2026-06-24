import numpy as np
def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    values =np.asarray(values)
    values = 2* np.pi * values /period


    return [[np.sin(v),np.cos(v)] for v in values]
