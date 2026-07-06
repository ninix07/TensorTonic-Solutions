def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    best_model = {}
    for model in models:
        if model["accuracy"] > best_model.get("accuracy",0):
            best_model = model
            continue
        elif model["accuracy"] == best_model.get("accuracy",0):
            if model["latency"] < best_model.get("latency",float('inf')):
                best_model = model 
                continue
            elif model["latency"] == best_model.get("latency",float('inf')):
                best_model = model if model["timestamp"] > best_model.get("timestamp",0) else best_model

        

    return best_model["name"]