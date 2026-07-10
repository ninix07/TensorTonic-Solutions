def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    return_arr = []

    for req in requests:
        user_id = req["user_id"]
        user_val = feature_store.get(user_id,defaults)
        online_features = req["online_features"]
        return_arr.append(user_val|online_features)


    return return_arr