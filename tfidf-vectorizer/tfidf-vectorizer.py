import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    documents =[ [el.lower() for el in doc.split()] for doc in documents]
    
    vocab = set(el for doc in documents for el in doc)
    vocab = sorted(vocab)
    matrix= np.zeros((len(documents),len(vocab)))
    df={}
    for word in vocab:
        for doc in documents:
            if word in doc:
                if word not in df.keys():
                    df[word] =0 
                df[word]+=1           
    for i,doc in enumerate(documents):
        for j,word in enumerate(vocab):
             idf = np.log(len(documents) / df[word])
             tf =doc.count(word) /len(doc) 
             matrix[i][j]=  tf * idf         
    
    
    return (matrix,vocab)