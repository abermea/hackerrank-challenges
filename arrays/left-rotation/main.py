#!/bin/python3

def rotLeft(a, d):
    lena = len(a)
    result = []
    for i in range(0, lena):
        index = (d % lena + i) % lena
        result.append(a[index])
    
    return result
    
# Test Cases
a = [1, 2, 3, 4, 5]
print(rotLeft(a, 4))

a = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
print(rotLeft(a, 10))

a = [33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97]
print(rotLeft(a, 13))
