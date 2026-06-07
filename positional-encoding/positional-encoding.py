import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pe= np.zeros((seq_len,d_model))
    position = np.arange(seq_len)[:, np.newaxis]
    
    even_indices = np.arange(0, d_model, 2)
    denominator = base ** (even_indices / d_model)
    
    # 4. Calculate the angles: shape (seq_len, len(even_indices))
    angles = position / denominator
    
    # 5. Fill the even columns with sine and odd columns with cosine
    pe[:, 0::2] = np.sin(angles[:, :pe[:, 0::2].shape[1]])
    pe[:, 1::2] = np.cos(angles[:, :pe[:, 1::2].shape[1]])
    
    return pe
    
    return pos