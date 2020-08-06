#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    total_cnt = 0
    # convert s to ex) format
    # ex) s = "aaabbbbcaa" -> [(a, 3), (b, 4), (c, 1), (a, 2)]
    l = []
    last_char = s[0]
    continuous_cnt = 1
    for i, char in enumerate(s):
        if i == 0:
            continue
        if last_char == char:
            continuous_cnt += 1

        else:
            l.append((last_char, continuous_cnt))
            continuous_cnt = 1
            last_char = char

        if i == len(s) - 1:
            l.append((last_char, continuous_cnt))

    for i, (char, cnt) in enumerate(l):
        # count all of the characters are the same
        total_cnt += (cnt * (cnt + 1)) // 2
        if i == 0 or i == len(l) - 1:
            continue
        # count all characters except the middle one are the same
        if cnt == 1 and l[i - 1][0] == l[i + 1][0]:
            total_cnt += min(l[i - 1][1], l[i + 1][1])

    return total_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
