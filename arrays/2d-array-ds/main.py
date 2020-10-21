#!/bin/python3

def hourglassSum(arr):
    results = []

    for i in range(1, 5):
        for j in range(1, 5):
            results.append(computeHGSum(arr, i, j))
    return max(results)


def computeHGSum(arr, i, j):
    return sum([arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1], arr[i][j], arr[i+1][j-1], arr[i+1][j], arr[i+1][j+1]])

# Test Cases

input = [
    [ 1, 1, 1, 0, 0, 0],
    [ 0, 1, 0, 0, 0, 0],
    [ 1, 1, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0]
]

print(hourglassSum(input))

input = [
    [-9, -9, -9,  1, 1, 1],
    [ 0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [ 0,  0,  8,  6, 6, 0],
    [ 0,  0,  0, -2, 0, 0],
    [ 0,  0,  1,  2, 4, 0]
]

print(hourglassSum(input))