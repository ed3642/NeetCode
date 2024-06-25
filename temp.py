#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMinimumOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING image as parameter.
#

def findMinimumOperations(image):
    # Write your code here
    # greedy?

    ops = 0
    bits = list(int(ch) for ch in image)

    for i in range(len(image)):
        ...

