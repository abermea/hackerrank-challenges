#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    cost = 0
    c.sort()
    c = c[::-1]
    c = [c[i:i + k] for i in range(0, len(c), k)]
    
    for index, element in enumerate(c):
        cost += sum(element) * (index + 1)
        
    return cost
