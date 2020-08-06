"""

problem link : https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a):
    swap_cnt = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                swap_cnt += 1
                a[j], a[j + 1] = a[j + 1], a[j]
    print("Array is sorted in {} swaps.".format(swap_cnt))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
