#!/bin/python3

def repeatedString(s, n):
    if(n < len(s)):
        s = s[:n]

    times = int(n / len(s))
    reminder = s[:n % len(s)]

    count = 0
    for char in s:
        if(char == 'a'):
            count += 1
    
    count *= times
    for char in reminder:
        if(char == 'a'):
            count += 1

    return count

