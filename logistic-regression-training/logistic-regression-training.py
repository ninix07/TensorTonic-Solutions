import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def calculate_loss(y, y_pred):
    total_loss=0
    for i in range(len(y)):
        total_loss += y[i]*np.log(y_pred[i]) + (1-y[i])* np.log(1-y_pred[i])
    return -total_loss/ len(y)
def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    weights= np.zeros(X.shape[1])
    bias= 0.0
    i= 0
    loss=float('-inf')
    while i < steps or loss==0.0:
        y_pred= np.dot(X,weights)+bias
        y_pred= _sigmoid(y_pred)
        w_del = np.dot(X.T,(y_pred-y))/ len(y)
        b_del = np.mean(y_pred-y)
        weights = weights- lr* w_del 
        bias= bias- lr*b_del
        loss= calculate_loss(y,y_pred)
        i+=1
    return weights,bias



