#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    n = len(a) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if a[j] > a[j+1] : 
                a[j], a[j+1], swaps = a[j+1], a[j], swaps + 1
    
    print("Array is sorted in {0} swaps.".format(swaps))
    print("First Element: {0}".format(a[0]))
    print("Last Element: {0}".format(a[-1]))
