"""

problem link : https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    min_diff = sys.maxsize
    arr.sort()
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i - 1])
    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
