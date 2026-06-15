import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here

    points = np.asarray(points)
    assignments = np.asarray(assignments)
    centroids = []
    for i in range(k):
        curr_points = points[assignments==i]
        centroid = np.mean(curr_points,axis=0)
        centroids.append(centroid.tolist())

    return centroids
        