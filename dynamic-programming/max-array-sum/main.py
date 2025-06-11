#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_curr = 0
    max_tally = [0] * len(arr)

    for index, elem in enumerate(arr):
        max_curr = max(max_curr, elem, max_tally[index - 2] + elem)
        max_tally[index] = max_curr

    return max_curr      
