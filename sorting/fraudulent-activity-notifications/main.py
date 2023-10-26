#!/bin/python3

import math
import os
import random
import re
import sys
from pathlib import Path

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    times = 0
    trailing_expenditures = expenditure[:d]
    trailing_expenditures.sort()

    for i in range(d, len(expenditure)):
        trailing_median = computeMedian(trailing_expenditures)
        current_expenditure = expenditure[i]
        notification_threshold = 2 * trailing_median

        print(i, current_expenditure, notification_threshold)

        if current_expenditure >= notification_threshold:
            print("Alert!")
            times += 1

        trailing_expenditures = trailing_expenditures[1:]
        idx = next((idx for idx, value in enumerate(trailing_expenditures) if value >= current_expenditure), -1)
        print(current_expenditure, idx, idx - 10, trailing_expenditures[idx - 10:idx + 10], idx + 10)
        trailing_expenditures.insert(idx, current_expenditure)

    return times

def computeMedian(arr):
    midpoint = int(len(arr)/2)
    if len(arr) % 2 == 1:
        return arr[midpoint]
    else:
        return (arr[midpoint - 1] + arr[midpoint]) / 2
    
if __name__ == '__main__':
    cases = [
        ("./case5.txt", 40001, 926),
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
            print("{0}: {1}, Expected {2}, Got {3}".format(case[0], test, case[2], ans))

