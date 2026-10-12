import torch

def neuron_forward(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor) -> tuple:
    """
    Returns a tuple of scalar tensors: preactivation and tanh output.
    """

    dot_prod = torch.dot(weights,inputs)+bias   
    pre_activation = torch.sum(dot_prod)
    return pre_activation ,torch.tanh(pre_activation)
