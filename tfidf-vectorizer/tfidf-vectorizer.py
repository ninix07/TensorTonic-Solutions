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
    matrix= np.zeros((doc_len, vocab_len))
    vocab_index = {word: i for i,word in enumerate(vocab)}
    df={}
    document_counters=[]
    
    for doc in documents:
        count_df = Counter(doc)
        document_counters.append(count_df)
        for key in count_df.keys():
            df[key] = df.get(key,0) +1
    
    idf={}
    for word in vocab:
        idf[word] = np.log(doc_len / df[word])

    for i,doc in enumerate(documents):
        count_df= document_counters[i]
        for key,val in count_df.items():
            tf = val/len(doc)
            matrix[i][vocab_index[key]]= tf *idf[key]

    return (matrix,vocab)