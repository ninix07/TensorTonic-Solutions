import math
def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    # Write code here
    shadow_lookup_dict = {r["input_id"]:r for r in shadow_log}

    prod_acc_count=0
    shadow_acc_count=0
    shadow_lat=[]
    agreement=[]

    for p in production_log:
        s= shadow_lookup_dict[p["input_id"]]
        if p["prediction"]==p["actual"]:
            prod_acc_count+=1
        if s["prediction"]==s["actual"]:
            shadow_acc_count+=1

        agreement.append(s["prediction"]==p["prediction"])
        shadow_lat.append(s["latency_ms"])
    shadow_acc = shadow_acc_count/len(agreement)
    prod_acc = prod_acc_count/len(agreement)
    agreement_rate = sum(agreement)/len(agreement)
    shadow_lat = sorted(shadow_lat)
    idx=math.ceil(0.95 * len(shadow_lat))-1
    p95 = shadow_lat[idx]
    if (shadow_acc-prod_acc) >= criteria["min_accuracy_gain"] and p95 <= criteria["max_latency_p95"] and agreement_rate >= criteria["min_agreement_rate"]:
        return {
            "promote": True,
            "metrics": {
                "shadow_accuracy": shadow_acc,
                "production_accuracy": prod_acc,
                "accuracy_gain": shadow_acc-prod_acc,
                "shadow_latency_p95": p95,
                "agreement_rate": agreement_rate,
            },
        }
    return {
    "promote": False,
    "metrics": {
        "shadow_accuracy": shadow_acc,
        "production_accuracy": prod_acc,
        "accuracy_gain": shadow_acc-prod_acc,
        "shadow_latency_p95": p95,
        "agreement_rate": agreement_rate,
    },
}