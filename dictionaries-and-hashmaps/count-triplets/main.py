import math
from itertools import combinations, product
from collections import Counter, defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    first = defaultdict(int)
    second = defaultdict(int)
    count = 0

    for value in arr:
        if value % (r*r) == 0:
            count += second[value // r]
        if value % r == 0:
            second[value] += first[value // r]
        first[value] += 1
    
    return count
