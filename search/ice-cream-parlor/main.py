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

def whatFlavorsE(cost, money):
    possible = list(map(lambda x, y: (x, y), range(1, len(cost) + 1), cost))
    possible = list(filter(lambda x: x[1] < money, possible))
    max_viable = max(possible, key = lambda x: x[1])
    possible = list(filter(lambda x: x[1] < money - max_viable[1], possible))

    results = {(av[1] + bv[1]):("{0} {1}".format(av[0], bv[0])) 
                    for ai,av in enumerate(possible) 
                    for bi,bv in enumerate(possible) 
                    if av[0] < bv[0]
                        and ai < bi}

    print(results[money])

def whatFlavorsD(cost, money):
    for i in range(0, len(cost)):
        for j in range(i + 1, len(cost)):
            value = cost[i] + cost[j]
            if value == money:
                print("{0} {1}".format(i + 1, j + 1))
                

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

