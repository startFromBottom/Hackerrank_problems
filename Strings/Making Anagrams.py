"""

problem link : https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""
# !/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    del_cnt = 0
    a_counter = Counter(a)
    b_counter = Counter(b)
    commons = (a_counter & b_counter)

    for a, v in a_counter.items():
        if a not in commons:
            del_cnt += v
        elif v > commons[a]:
            del_cnt += v - commons[a]

    for i, v in b_counter.items():
        if i not in commons:
            del_cnt += v
        elif v > commons[i]:
            del_cnt += v - commons[i]

    return del_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
