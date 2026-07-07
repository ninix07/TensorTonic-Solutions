import numpy as np
def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    
    recommendations = [item for sublist in recommendations for item in sublist]
    unique = len(set(recommendations))
    return unique/n_items