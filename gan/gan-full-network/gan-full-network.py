import numpy as np

def gan_forward(
    z: np.ndarray,
    real_data: np.ndarray,
    G_W: np.ndarray,
    G_b: np.ndarray,
    D_W: np.ndarray,
) -> dict:
    """
    Returns generated samples, probabilities, and both GAN losses.
    """
    generated_sample  = np.tanh(np.dot(z,G_W)+G_b)
    real_val = np.dot(real_data,D_W)
    fake_val = np.dot(generated_sample,D_W)
    p_real = 1/(1+np.exp(-real_val))
    p_fake = 1/(1+np.exp(-fake_val))

    eps = 1e-8
    p_real = np.clip(p_real,eps,1-eps)
    p_fake = np.clip(p_fake,eps,1-eps)
    dis_loss = -np.mean(np.log(p_real)+np.log(1-p_fake))

    gen_loss = -np.mean(np.log(p_fake))

    return {
        "generated_samples" : generated_sample,
        "real_probabilities": p_real,
        "fake_probabilities": p_fake,
        "discriminator_loss": dis_loss,
        "generator_loss" : gen_loss
    }

    