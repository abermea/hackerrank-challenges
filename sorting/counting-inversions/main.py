#!/bin/python3

import math
import os
import random
import re
import sys
import logging
logger = logging.getLogger(__name__)

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
swaps = 0

def countInversions(arr):
    mergesort(arr)
    return swaps

def merge(A, temp, frm, mid, to):
 
    k = frm
    i = frm
    j = mid + 1
 
    while i <= mid and j <= to:
        if A[i] < A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
            swaps += 1
 
        k += 1
 
    while i < len(A) and i <= mid:
        temp[k] = A[i]
        k += 1
        i += 1
 
    for i in range(frm, to + 1):
        A[i] = temp[i]
 
 
def mergesort(A):
 
    low = 0
    high = len(A) - 1
    mid = int(high / 2)
 
    temp = A.copy()
 
    m = 1
    while m <= high - low:
 
        for i in range(low, high, 2*m):
            frm = i
            mid += m - 1
            to = min(i + 2*m - 1, high)
            merge(A, temp, frm, mid, to)
 
        m = 2*m
 


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    cases = [
        # ("./case5.txt", 40001, 926),
    ]

    # for case in cases:
    #     f = Path(__file__).with_name(case[0]).open("r")

    #     expenditures = []
    #     d = case[1]
    #     result = case[2]

    #     for line in f.readlines():
    #         expenditures.append(list(map(int, line.rstrip().split())))

    #     for expenditure in expenditures:
    #         ans = countInversions(expenditure, d)
    #         test = ans == result
    #         print(f'{case[0]}: {test}, Expected {case[2]}, Got {ans}')