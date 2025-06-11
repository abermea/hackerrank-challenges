#!/bin/python3
from functools import reduce

def arrayManipulation(n, queries):
    oplen = 0
    for query in queries:
        curr = max(query[0:2])
        oplen = max(oplen, curr)
    
    tally = [0] * (oplen + 1)

    for query in queries:
        tally[query[0] - 1] += query[2]
        tally[query[1]] -= query[2]

    s = 0
    m = 0
    for elem in tally:
        s += elem
        m = max(m, s)
    
    return m
