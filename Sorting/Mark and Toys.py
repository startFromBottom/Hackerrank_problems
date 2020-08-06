"""

problem link

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    price_sum = 0
    max_cnt = 0
    for i, p in enumerate(prices):
        price_sum += p
        if price_sum > k:
            break
        max_cnt += 1
    return max_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
