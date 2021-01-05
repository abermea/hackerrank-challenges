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

# Test cases

arr = [7, 1, 3, 2, 4, 5, 6]
print(minimumSwaps(arr))

