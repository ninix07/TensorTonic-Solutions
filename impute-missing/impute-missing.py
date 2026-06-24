import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.asarray(X)

    fill_values = np.nanmean(X, axis=0) if strategy=='mean' else np.nanmedian(X, axis=0)

    fill_values = np.nan_to_num(fill_values, nan=0.0)
    X = np.where(np.isnan(X),fill_values,X)


    return X