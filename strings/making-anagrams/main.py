#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0

    for letter in alphabet:
        count += abs(a.count(letter) - b.count(letter))

    return count