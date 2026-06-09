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
    vocab_len= len(vocab)
    doc_len= len(documents)
    vocab_index ={word:i for i,word in enumerate(vocab)}

    tf = np.zeros((doc_len,vocab_len))
    df = np.zeros(vocab_len)

    for i, doc in enumerate(documents):
        count= Counter(doc)
        for word,freq in count.items():
            j = vocab_index[word]
            tf[i,j]= freq/len(doc)
            df[j]+=1

    idf = np.log(doc_len/df)
    idf[df==0.0] = 0.0
    
    tf_idf = tf * idf
    return tf_idf, vocab