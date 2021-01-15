#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    prev = s[0]
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == prev:
            deletions += 1
        else:
            prev = s[i]
    
    return deletions