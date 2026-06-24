def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    n = len(values)
    rt_list = []
    
    for i in range(n):
        if values[i] is None:
            l_index = max(j for j in range(i) if values[j] is not None)
            r_index = min(j for j in range(i + 1, n) if values[j] is not None)
            left_known = values[l_index]
            right_known = values[r_index]
            rt_list.append(left_known + (i-l_index)/(r_index-l_index) * (right_known-left_known))
            
        else:
            rt_list.append(values[i])



    return rt_list
            

        
                                                                   

            