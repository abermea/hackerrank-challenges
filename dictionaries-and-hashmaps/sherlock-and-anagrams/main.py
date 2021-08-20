#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    s = s.strip()
    counter = Counter()
    count = 0

    substrings = [''.join(sorted(s[i: j])) 
            for i in range(len(s)) 
            for j in range(i + 1, len(s) + 1)]

    for substring in substrings:
        counter[substring] += 1
    
    for elem in counter.values():
        if elem > 1:
            count += (math.factorial(elem) // (2 * math.factorial(elem - 2)))

    return count
