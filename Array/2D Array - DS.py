"""

problem link : https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

"""

# !/bin/python3

import math
import os
import random
import re
import sys
from typing import List


# Complete the hourglassSum function below.

def hourglass_area_sum(arr: List[List[int]],
                       r_start: int, c_start: int) -> int:
    """
    scan hourglass area and get sum of area
    :param arr: input 2D array
    :param r_start: start of index in row direction
    :param c_start: start of index in column direction
    :return: sum of area
    """
    total = 0
    for c in range(c_start, c_start + 3):
        for r in range(r_start, r_start + 3):
            if (c, r) not in [(c_start + 1, r_start), (c_start + 1, r_start + 2)]:
                total += arr[c][r]
    return total


def hourglassSum(arr):
    max_sum = -sys.maxsize
    for c in range(len(arr) - 2):
        for r in range(len(arr[0]) - 2):
            sum = hourglass_area_sum(arr, r, c)
            max_sum = max(sum, max_sum)
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
