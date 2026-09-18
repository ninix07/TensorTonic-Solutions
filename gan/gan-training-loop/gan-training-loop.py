import numpy as np

def train_discriminator_step(
    real_data: np.ndarray,
    fake_data: np.ndarray,
    D_W: np.ndarray,
    learning_rate: float,
) -> dict:
    """
    Returns updated discriminator weights and the pre-update loss.
    """
    
    p_real = 1/(1+np.exp(-(np.dot(real_data,D_W))))
    p_fake = 1/(1+np.exp(-(np.dot(fake_data,D_W))))

    dis_loss= -np.mean(np.log(p_real)+np.log(1-p_fake))

    weight_grad= (np.dot(real_data.T, (p_real-1)) + np.dot(fake_data.T,p_fake))/real_data.shape[0]

    updated_weight = D_W- learning_rate*weight_grad

    return{
        "new_discriminator_weights": updated_weight,
        "discriminator_loss": dis_loss
    }