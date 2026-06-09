import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    N= len(docs)
    docs_len =np.array([len(doc) for doc in docs])
    avg_doc_len = np.mean(docs_len)

    unique_queries = list(set(query_tokens))

    tf = np.zeros((N,len(unique_queries)))
    df= np.zeros(len(unique_queries))

    for i,doc in enumerate(docs):
        counts= Counter(doc)
        for j, query in enumerate(unique_queries):
            freq = counts.get(query,0)
            if freq:
                tf[i,j] = freq
                df[j]+=1


    idf = np.log(((N-df +0.5)/(df+0.5))+1)

    idf[df==0] =0.0

    numerator = tf *(k1+1)
    denominator = tf + k1*(1-b + (b*docs_len[:,None]/avg_doc_len))

    scores = np.sum((idf*numerator/denominator) , axis=1)

    return scores
    
            