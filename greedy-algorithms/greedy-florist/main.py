#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    fpp = [0] * k
    cost = 0
    c.sort(reverse=True)

    for i in range(len(c)):
        fpp[i % len(fpp)] += 1
    
    control = 0
    for person in fpp:
        sales = 1
        flowers2buy = c[control:control + person]
        print(flowers2buy)
        for flower in reversed(flowers2buy):
            cost += sales * flower
            sales += 1
        control += person

    print(fpp, cost)

    return cost


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(str(minimumCost) + '\n')

