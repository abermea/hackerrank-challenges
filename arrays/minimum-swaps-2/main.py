#!/bin/python3

def minimumSwaps(arr):
    swaps = 0
    mapped = list(map(lambda x: {'current_value': x, 'should_be_at': x - 1}, arr))
    for current in range(0, len(mapped)):
        while(mapped[current]['should_be_at'] != current):
            should_be = mapped[current]['should_be_at']
            mapped[current], mapped[should_be] = mapped[should_be], mapped[current]
            swaps += 1
    return swaps

def minimumSwapsO(arr):
    swaps = 0
    lenarr = len(arr)
    for i in range(0, lenarr):
        if(arr[i] != (i + 1)):
            index = arr[i:lenarr].index(i + 1)
            arr[i], arr[index + i], swaps = arr[index + i], arr[i], swaps + 1
    
    return swaps

def diff_arrays(a, b):
    return [abs(x - y) for x,y in zip(a,b)]

def first(arr):
    sorted_arr = sorted(arr)
    diff = diff_arrays(arr, sorted_arr)
    filtered = list(filter(lambda x: x != 0, diff))
    return len(filtered) - 1

# Test cases

arr = [7, 1, 3, 2, 4, 5, 6]
print(minimumSwaps(arr))

