#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from pathlib import Path
from itertools import zip_longest

# Complete the freqQuery function below.
def freqQuery(queries):
    db = defaultdict(lambda: 0)
    ops = defaultdict(lambda: 0)
    out = []
    
    for query in queries:
        if query[0] == 1:
            ops[1] += 1
            db[query[1]] += 1
        
        if query[0] == 2:
            ops[2] += 1
            db[query[1]] -= 1 if db[query[1]] > 0 else 0
            
        if query[0] == 3:
            ops[3] += 1
            out.append(1 if ops[1] + ops[2] >= query[1] and query[1] in db.values() else 0)

    return out

if __name__ == '__main__':
    files = [
        ("./case12.txt", "./case12-results.txt"),
        ("./case11.txt", "./case11-results.txt"),
    ]

    for file in files:
        f = Path(__file__).with_name(file[0]).open("r")
        r = Path(__file__).with_name(file[1]).open("r")

        queries = []
        results = []

        for line in f.readlines():
            queries.append(list(map(int, line.rstrip().split())))
        
        for line in r.readlines():
            results.append(int(line))

        ans = freqQuery(queries)

        test = ans == results
        print("{0}: {1}".format(file[1], test))
        # if test is False:
        #     zipped = zip_longest(ans, results, fillvalue=None)
        #     print(list(zipped))