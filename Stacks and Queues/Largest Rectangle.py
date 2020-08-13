"""

problem link : https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    area = 0
    i = 0
    while i < len(h):
        if not stack or h[i] >= h[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            v = stack.pop()
            area = max(area, h[v] * (i - stack[-1] - 1 if stack else i))

    while stack:
        v = stack.pop()
        area = max(area, h[v] * (i - stack[-1] - 1 if stack else i))
    return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
