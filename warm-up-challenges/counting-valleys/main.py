#!/bin/python3

def countingValleys(steps, path):
    # Write your code here
    heights = []
    valleys = 0
    control = 0
    
    for step in path:
        if(step == 'U'):
            control += 1
        else:
            control -= 1
        heights.append(control)
    
    control = heights[0]
    for height in heights:
        if control == -1 and height == 0:
            valleys += 1
        control = height
    
    return valleys