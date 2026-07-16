def retraining_policy(daily_stats, config):
    """
    Decide which days to trigger model retraining.
    """
    # Write code here
    n = len(daily_stats)
    retrain_list=[]
    last_retrain_day = 0
    for i in range(n):
        curr_stat = daily_stats[i]
        prev_stat = daily_stats[i-1]
        if curr_stat["drift_score"] > config["drift_threshold"] or curr_stat["performance"] < config["performance_threshold"] or (curr_stat["day"] - last_retrain_day) >= config["max_staleness"]:
            if not last_retrain_day or curr_stat["day"]-last_retrain_day >= config["cooldown"]:
                if config["budget"]<config["retrain_cost"]:
                    break
                retrain_list.append(curr_stat["day"])
                config["budget"]-=config["retrain_cost"]
                last_retrain_day=curr_stat["day"]

    return retrain_list