import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    # Your code here
    upper = torch.matmul(Q,K.transpose(-2,-1))
    val = upper/ math.sqrt(K.shape[-1])
    s_m = F.softmax(val,dim=-1)

    return torch.matmul(s_m,V)