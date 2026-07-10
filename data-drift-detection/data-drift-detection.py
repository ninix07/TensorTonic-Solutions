
def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    tot_reference_counts = sum(reference_counts)
    tot_production_counts = sum(production_counts)
    diff= [abs((reference_counts[i]/tot_reference_counts) -(production_counts[i]/tot_production_counts))for i in range(len(reference_counts))]
        
    diff = sum(diff)/2

    return {"score":diff , "drift_detected": True if diff > threshold else False}