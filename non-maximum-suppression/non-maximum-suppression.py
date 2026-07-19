def get_iou(box_a,box_b):
    inter_x1 = max(box_a[0],box_b[0])
    inter_y1 = max(box_a[1],box_b[1])
    inter_x2 = min(box_a[2],box_b[2])
    inter_y2 = min(box_a[3],box_b[3])

    inter_width = max(0,inter_x2-inter_x1)
    inter_height = max(0,inter_y2-inter_y1)

    intersection = inter_width * inter_height

    area1 = (box_a[2]-box_a[0]) * (box_a[3]-box_a[1])
    area2 = (box_b[2]-box_b[0]) * (box_b[3]-box_b[1])

    union = area1+ area2 -intersection
    return intersection/union   

def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    # Write code here
    if not boxes:
        return []

    order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    output = []

    while order:
        current =order[0]
        output.append(current)

        order =order[1:]

        order = [i for i in order if get_iou(boxes[current],boxes[i]) < iou_threshold ]


    return output

        

    

    
    