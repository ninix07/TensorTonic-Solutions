import math
import numpy as np

def roi_pool(feature_map, rois, output_size):
    """
    Apply ROI Pooling to extract fixed-size features.
    """
    # Write code here
    feature_map = np.asarray(feature_map)
    alloutput=[]
    for roi in rois:
        output = np.zeros((output_size,output_size))
        roi_h = roi[3]-roi[1]
        roi_w = roi[2]-roi[0]
        for i in range(output_size):
            for j in range(output_size):
                h_start = roi[1]+int(np.floor(i*roi_h/output_size))
                h_end = roi[1]+int(np.floor((i+1)*roi_h/output_size))
                w_start = roi[0]+int(np.floor(j*roi_w/output_size))
                w_end = roi[0]+int(np.floor((j+1)*roi_w/output_size))
    
                if h_end ==h_start:
                    h_end=h_end+1
                if w_end ==w_start:
                    w_end=w_end+1
                output[i][j]= np.max(feature_map[h_start:h_end,w_start:w_end])
        alloutput.append(output.tolist())
    return alloutput