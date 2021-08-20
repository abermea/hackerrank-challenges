#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    stack = []

    print(s)

    for c in s:
        if c in opening:
            stack.append(c)
        if c in closing:
            try:
                prev = stack.pop()
                if opening.index(prev) != closing.index(c):
                    return 'NO'
            except IndexError:
                return 'NO'
    
    if len(stack) != 0: 
        return 'NO'
    return 'YES'
