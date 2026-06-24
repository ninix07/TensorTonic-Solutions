import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    
    min = [float('inf')]*D
    max = [float('-inf')]*D
    return {"min": min , "max": max}

def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    X_batch = np.asarray(X_batch)
    batch_min =np.min(X_batch,axis=0)
    batch_max = np.max(X_batch,axis=0)
    state['min'] = np.minimum(batch_min,state['min'])
    state['max']= np.maximum(batch_max,state['max'])

    X_batch = (X_batch- state['min'])/(state['max']-state['min'] +eps)
        
    return X_batch