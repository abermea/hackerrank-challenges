#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    if (sum(prices) <= k):
        return len(prices)

    prices.sort()
    
    count = 0
    total = 0

    for price in prices:
        total += price
        if total > k:
            break
        count += 1
    
    return count