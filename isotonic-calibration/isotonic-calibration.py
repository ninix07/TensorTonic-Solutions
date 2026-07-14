import numpy as np
def calibrate_isotonic(cal_labels, cal_probs, new_probs):
    """
    Apply isotonic regression calibration.
    """
    # Write code here
    cal_labels = np.asarray(cal_labels)
    cal_probs = np.asarray(cal_probs)
    new_probs=np.asarray(new_probs)

    sorted_indices = np.argsort(cal_probs)
    cal_labels = cal_labels[sorted_indices]
    cal_probs = cal_probs[sorted_indices]
    stack =[]

    for label in cal_labels :
        stack.append([label,1])
        while len(stack)>= 2 and stack[-2][0] > stack[-1][0]:
            mean1,count1 = stack[-2]
            mean2,count2 = stack[-1]
            stack.pop()
            stack.pop()
            new_count = count1 + count2
            new_mean = (mean1*count1 + mean2*count2)/new_count
            stack.append([new_mean,new_count])


    calibrated_labels =np.repeat([group[0]for group in stack ], [group[1] for group in stack] )

    return np.interp(new_probs,cal_probs,calibrated_labels).tolist()