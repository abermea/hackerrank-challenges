#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    counter = Counter()
    for c in s:
        counter[c] += 1
    
    counter2 = Counter()

    for elem in counter.values():
        counter2[elem] += 1
    
    counter2v = counter2.values()

    if len(counter2v) > 2:
        return 'NO'
    
    if counter2[1] == 1:
        return 'YES'
    
    cmax = max(counter2v)
    cmin = min(counter2v)

    if len(counter2v) == 2 and cmax <= cmin + 1:
        return 'NO'
        
    return 'YES'