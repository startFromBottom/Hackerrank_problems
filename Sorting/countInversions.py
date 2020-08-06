"""

problem link : https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

"""

# !/bin/python3

import math
import os
import random
import re
import sys


def merge(l1, l2, swap_cnt):
    res = []
    p1, p2 = 0, 0
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] <= l2[p2]:
            res.append(l1[p1])
            p1 += 1
        else:
            res.append(l2[p2])
            swap_cnt += len(l1) - p1
            p2 += 1
    if l1:
        res.extend(l1[p1:])
    if l2:
        res.extend(l2[p2:])
    return res, swap_cnt


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, l_cnt = merge_sort(arr[:mid])
    right, r_cnt = merge_sort(arr[mid:])
    return merge(left, right, l_cnt + r_cnt)


def countInversions(arr):
    arr, cnt = merge_sort(arr)
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
