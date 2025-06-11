#!/bin/python3

def sockMerchant(n, ar):
    pairs = 0
    ar.sort()

    for elem in ar:
        filtered = list(filter(lambda x: x == elem, ar))
        ar = list(filter(lambda x: x != elem, ar))
        pairs += len(filtered) - (len(filtered) % 2)
    
    return int(pairs / 2)