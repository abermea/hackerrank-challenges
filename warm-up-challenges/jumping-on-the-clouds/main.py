#!/bin/python3

def jumpingOnClouds(c):
    return jump(c, 0)

def jump(clouds, index):
    if(index >= len(clouds) - 1):
        return 0

    if(clouds[index] == 1):
        return 20000

    a = jump(clouds, index + 1)
    b = jump(clouds, index + 2)

    return min(a,b) + 1
