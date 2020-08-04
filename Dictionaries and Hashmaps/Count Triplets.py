#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    if len(arr) <= 2:
        return 0

    # store the frequency of the numbers encountered yet
    map_arr = defaultdict(int)
    # store the frequency of pairs(2nd, 3rd triplets)
    map_pair = defaultdict(int)
    cnt = 0
    for x in arr[::-1]:
        r_x = x * r
        r_r_x = r_x * r

        # case 1 : when x is the first element of triplets
        cnt += map_pair[(r_x, r_r_x)]
        # case 2 : x is the second element of triplets
        map_pair[(x, r_x)] += map_arr[r_x]
        # case : x is the third elemet of triplets
        map_arr[x] += 1

    return cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
