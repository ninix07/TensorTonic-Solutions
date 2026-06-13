def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
  
    return_list =[]  
    for point in points:
        best_dist = float('inf')
        best_index=0
        for i, centroid in enumerate(centroids):
            curr_dist = sum((c - p) ** 2 for c, p in zip(centroid, point)) ** 2
            if curr_dist < best_dist:
                best_index =i
                best_dist = curr_dist
        return_list.append(best_index)

    return return_list