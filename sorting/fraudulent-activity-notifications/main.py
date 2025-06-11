#!/bin/python3

import sys
from pathlib import Path
from collections import Counter
import logging
logger = logging.getLogger(__name__)

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    times, prev, mid = 0, 0, d / 2
    counts = counter(expenditure[0:d])
    
    for i in range(d, len(expenditure)):
        median_value = median(counts, mid)
        logger.info(f'Prev: {prev}, Curr: {i}, Median: {median_value}, Threshold: {2 * median_value}, Period: {d}, Mid: {mid}, Expeniture: {expenditure}, Counts: {counts}')
        if expenditure[i] >= 2 * median_value:
            times += 1
        counts[expenditure[prev]] -= 1
        counts[expenditure[i]] += 1
        prev += 1

    return times

def counter(arr):
    counts = [0] * 201
    for k, v in enumerate(arr):
        counts[v] += 1
    return counts

def median(arr, mid):
    i, cs = 0, 0
    while (cs < mid):
        cs += arr[i]
        i += 1
    return i - 1 if float(cs) != mid else (2 * i - 1) / 2
    
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    cases = [
        # ("./case5.txt", 40001, 926),
        ("./case6.txt", 4, 0),
    ]

    for case in cases:
        f = Path(__file__).with_name(case[0]).open("r")

        expenditures = []
        d = case[1]
        result = case[2]

        for line in f.readlines():
            expenditures.append(list(map(int, line.rstrip().split())))

        for expenditure in expenditures:
            ans = activityNotifications(expenditure, d)
            test = ans == result
            print(f'{case[0]}: {test}, Expected {case[2]}, Got {ans}')

