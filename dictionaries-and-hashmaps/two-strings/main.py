#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for c in s2:
        if c in s1:
            return 'YES'
    return 'NO'

