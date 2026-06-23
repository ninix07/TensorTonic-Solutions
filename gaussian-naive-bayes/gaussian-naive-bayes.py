import numpy as np
def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    y_train = np.asarray(y_train)
    X_train = np.asarray(X_train)
    X_test= np.asarray(X_test)
    vals,counts = np.unique(y_train, return_counts=True)
    eps= 1e-9
    prior = counts/np.sum(counts)


    mean = np.zeros((len(vals),X_train.shape[1]))
    variance = np.zeros((len(vals),X_train.shape[1]))
    for i,v in enumerate(vals):
            mask = v==y_train
            mean[i]= X_train[mask].mean(axis=0)
            variance[i]=X_train[mask].var(axis=0)

    y_test=np.zeros(X_test.shape[0])
    for t, test in enumerate(X_test):
        scores = np.zeros(len(vals))
        for i, v in enumerate(vals):
            log_pdf = -0.5*np.log(2*np.pi*(variance[i]+eps)) - (test-mean[i])**2/(2*(variance[i]+eps))
            scores[i] = np.sum(log_pdf)+ np.log(prior[i])
        best_idx = np.argmax(scores)
        y_test[t] = vals[best_idx]

    return y_test.tolist()