import numpy as np

def detect_mode_collapse(generated_samples: np.ndarray, threshold: float = 0.1) -> dict:
    """
    Returns diversity_score and is_collapsed in a dictionary.
    """

    feature_mean = np.mean(generated_samples, axis=0)

    s_j = np.sqrt(np.mean((generated_samples-feature_mean)**2, axis=0))

    diversity_score = np.mean(s_j) 
    return {
        "diversity_score": diversity_score,
        "is_collapsed": True if diversity_score < threshold else False
    }