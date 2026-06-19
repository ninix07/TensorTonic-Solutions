import numpy as np

def naive_bayes_bernoulli(X_train, y_train, X_test):
    """
    Compute log-likelihood P(y|x) for Bernoulli Naive Bayes.
    """
    # Write code here
    X_train=np.asarray(X_train)
    X_test = np.asarray(X_test)
    y_train = np.asarray(y_train)
    vals,count = np.unique(y_train, return_counts=True)
    class_count= np.sum(count)
    prior = count / class_count
    theta_list=np.asarray([((X_train[y_train==val].sum(axis=0))+1)/(count[i]+2) for i,val in enumerate(vals)])
    X_test = X_test[:,np.newaxis,:]
    logits = X_test *np.log(theta_list) + (1-X_test) *np.log(1-theta_list)
    return logits.sum(axis=2) +np.log(prior)