"""

problem link : https://www.hackerrank.com/challenges/min-max-riddle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

"""

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


def max_window_dict(arr):
    stack = []
    arr.append(0)
    d = defaultdict(int)
    for i, v in enumerate(arr):
        t = i
        while stack and stack[-1][0] >= v:
            pv, pi = stack.pop()
            d[v] = max(d[v], i - pi + 1)
            d[pv] = max(d[pv], i - pi)
            t = pi
        stack.append((v, t))
    del d[0]
    return d


def riddle(arr):
    # complete this function

    # step 1
    # make dictionary(key: each number, value: maximum window size)
    dic = max_window_dict(arr)
    # step 2
    # make inverse dict(key : each window size, value : maximum number)
    e = defaultdict(int)
    for k in dic:
        e[dic[k]] = max(e[dic[k]], k)

    # step 3
    # starting from i=len(arr) - 2 iterate down to a window size of 1,
    # looking up the corresponding values in inverted_windows and
    # fill missing values with the previous largest window value

    ans = [e[len(arr) - 1]]
    for i in range(len(arr) - 2, 0, -1):
        if e[i] < ans[-1]:
            ans.append(ans[-1])
        else:
            ans.append(e[i])
    return ans[::-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
