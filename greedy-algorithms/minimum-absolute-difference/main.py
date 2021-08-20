#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    pairs = list(zip(arr, arr[1:] + arr[:1])) 
    results = list(map(lambda x: abs(x[0] - x[1]), pairs))
    return min(results)