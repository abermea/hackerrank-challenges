#!/bin/python3

import math
import os
import random
import re
import sys
from pathlib import Path

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    unfairness = arr[-1] - arr[0]
    
    i = 0
    while (i + k) <= len(arr):
        idx = i + k
        current = arr[i:idx:k-1]
        unfairness = min(unfairness, current[-1] - current[0])
        i += 1
    
    return unfairness

if __name__ == '__main__':
    files = [
        ("./case16.txt", 2, 2),
    ]

    for file in files:
        f = Path(__file__).with_name(file[0]).open("r")

        arr = []
        k = file[1]
        result = file[2]

        for line in f.readlines():
            arr.append(int(line))
        
        ans = maxMin(k, arr)

        test = ans == result
        print("{0}: {1}".format(file[1], test))
