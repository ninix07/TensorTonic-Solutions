def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here

    output =[]

    for p in range(0,period):
         curr_arr= series[p::period]

         output.append(sum(curr_arr)/len(curr_arr))

    return output

