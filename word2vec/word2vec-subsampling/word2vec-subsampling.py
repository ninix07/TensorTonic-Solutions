import torch

def subsample_keep_probs(counts: torch.Tensor,
                         t: float = 1e-5) -> torch.Tensor:
    """
    Returns the float64 keep probability for every vocabulary word.
    """
    f_w: torch.Tensor = counts / torch.sum(counts)

    return torch.min(torch.tensor(1.0),torch.sqrt(t/f_w))