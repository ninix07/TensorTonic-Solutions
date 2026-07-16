def schedule_pipeline(tasks, resource_budget):
    """
    Schedule ETL tasks respecting dependencies and resource limits.
    """
    # Write code here
    t=0
    completed = set()
    running =[]
    started= {}
    not_started =tasks.copy()
    while not_started:
        still_running =[]
        for task,end_time in running:
            if end_time <= t:
                completed.add(task["name"])
            else:
                still_running.append((task,end_time))
        running=still_running
        ready= [task for task in not_started if all(dep in completed for dep in task["depends_on"]) ]

        ready.sort(key=lambda x : x["name"])
        current_usage = sum(task["resources"] for task,end_time in running)
        for task in ready:
            if current_usage + task["resources"] <= resource_budget:
                started[task["name"]] =t
                running.append((task,t+task["duration"]))
                not_started.remove(task)
                current_usage +=task["resources"]

        t = min(end_time for _,end_time in running)

    return sorted(started.items(),key=lambda x :(x[1],x[0]))