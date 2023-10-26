#!/bin/python3

import math
import os
import random
import re
import sys
from pathlib import Path

#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def primality(n):
    max_possible = int(math.sqrt(n)) + 1

    if n == 1:
        return "Not prime"

    for i in range(2, max_possible):
        if n % i == 0:
            return "Not prime"
            
    return "Prime"

if __name__ == '__main__':
    files = [
        ("./case9.txt", "./case9-results.txt"),
    ]

    for file in files:
        f = Path(__file__).with_name(file[0]).open("r")
        r = Path(__file__).with_name(file[1]).open("r")

        arr = []
        results = []

        for line in f.readlines():
            arr.append(int(line.strip()))

        for line in r.readlines():
            results.append(line.strip())
        
        for elem in zip(arr, results):
            ans = primality(elem[0])
            test = ans == elem[1]
            print("{0}: {1}, Got: {2}, Expected: {3}".format(elem[0], test, ans, elem[1]))