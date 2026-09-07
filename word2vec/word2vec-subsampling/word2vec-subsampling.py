import torch

def subsample_keep_probs(counts: torch.Tensor,
                         t: float = 1e-5) -> torch.Tensor:
    """
    Returns the float64 keep probability for every vocabulary word.
    """
    f_w: torch.Tensor = counts / torch.sum(counts)

    return torch.clamp(torch.sqrt(t/f_w),max=1.0)