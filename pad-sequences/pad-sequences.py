import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not max_len:
        max_len = max([len(seq) for seq in seqs])
 
    padded_val = np.array([ np.pad(seq[:max_len],pad_width = (0,max_len-len(seq[:max_len])),mode='constant', constant_values=pad_value) for seq in seqs])

    return padded_val