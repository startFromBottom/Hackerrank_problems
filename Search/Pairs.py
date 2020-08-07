"""

problem link : https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

"""


#!/bin/python3

import math
import os
import random
import re
import sys


## Complete the pairs function below.
## time exeeed
# def pairs(k, arr):
#     cnt = 0
#     arr.sort()
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[j] - arr[i] >= k:
#                 if arr[j] - arr[i] == k:
#                     cnt += 1
#                 continue
#     return cnt

def pairs(k, arr):
    # two-pointer solution
    cnt = 0
    arr.sort()
    lo, hi = 0, 1
    while hi < len(arr):
        if arr[hi] - arr[lo] > k:
            if hi == lo + 1:
                lo += 1
                hi += 1
            else:
                lo += 1
        elif arr[hi] - arr[lo] < k:
            hi += 1
        else:  # arr[hi] - arr[lo] = k
            cnt += 1
            lo += 1
            hi += 1

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
