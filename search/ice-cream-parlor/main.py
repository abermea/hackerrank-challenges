#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    possible = [(index + 1, value) for index, value in enumerate(cost) if value < money]
    max_viable = max(possible, key = lambda x: x[1])
    possible = [x for x in possible if x[1] >= money - max_viable[1]]
    possible.sort(key = lambda x: x[1])

    for i in range(0, len(possible)):
        for j in range(len(possible) - 1, i, -1):
            value = possible[i][1] + possible[j][1]
            if value < money:
                continue
            if value == money:
                first = min(possible[i][0], possible[j][0])
                second = max(possible[i][0], possible[j][0])
                print("{0} {1}".format(first, second))
                return
