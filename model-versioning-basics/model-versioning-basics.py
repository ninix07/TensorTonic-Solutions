def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    if not models:
        return None

    def model_rank(model):
        return (
            model["accuracy"],
            -model["latency"],
            model["timestamp"]
        )
        

    return sorted(models,key=model_rank)[-1]["name"]