#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    important = list(filter(lambda x: x[1] > 0, contests))
    important.sort()
    notImportant = list(filter(lambda x: x[1] == 0, contests))
    luck = 0

    for i in range(0, len(important) - k):
        important[i][0] *= -1

    for event in important:
        luck += event[0]

    for event in notImportant:
        luck += event[0]
    
    return luck