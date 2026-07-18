def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    stride = image_size / feature_size
    output_list=[]
    width_height=[]
    for s in scales:
        for r in aspect_ratios:
            width_height.append((s*(r**0.5),s/(r**0.5)))
    for i in range(0,feature_size):
        for  j in range(0,feature_size):
            cx= (j+0.5)*stride
            cy= (i+0.5)*stride
            for w,h in width_height:
                output_list.append([cx-w/2,cy-h/2,cx+w/2,cy+h/2])


    return output_list

        




    
            
            