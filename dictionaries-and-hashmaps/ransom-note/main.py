#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for elem in note:
        try:
            index = magazine.index(elem)
            magazine.pop(index)
        except ValueError:
            print('No')
            return False
    print('Yes')
    return True

magazine = ['give','me','one','grand','today','night']
note = ['give','one','grand','today']
print(checkMagazine(magazine,note))