"""
Given a long integer, find the number of ways to represent it as a sum of two or more consecutive positive integers
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'consecutive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER num as parameter.
#

def consecutive(num):
    result = []
    n = 2
    for i in range(1, num):
        a = i
        while n < num//2:
            if 2*a*n + n*(n-1) == 2 * num:
                result.append((a, n))
            n += 1
    return result

if __name__ == '__main__':
    print(consecutive(10))