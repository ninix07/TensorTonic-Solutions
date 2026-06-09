import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    number_of_docs = len(docs)
    avg_doc_len = sum(len(doc) for doc in docs) / len(docs) if docs else 0
    scores = np.zeros(number_of_docs)
    df= {}
    counters= []
    for doc in docs:
        count_df = Counter(doc)
        for words in count_df.keys():
            df[words] = df.get(words,0) +1
        counters.append(count_df)

    for i, doc in enumerate(docs):
        count_df = counters[i]
        total = 0
        for query in query_tokens:
             if query not in count_df.keys():
                 idf = 0 
             else:
                 numerator = number_of_docs - df[query] +0.5
                 denominator = df[query] +0.5 
                 idf = np.log((numerator/denominator)+1)

                 curr_score = idf * (count_df[query] *(k1+1)) / (count_df[query] + k1 * ( 1-b + (b*len(doc)/avg_doc_len)))
                 total+=curr_score
        scores[i] = total
    return scores
            