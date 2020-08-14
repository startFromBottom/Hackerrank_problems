"""

problem link : https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""

# Use PyPy3
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below.
def commonChild(s1, s2):
    # Longest common subsequence problem

    r = len(s1) + 1
    c = len(s2) + 1

    memo = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(1, r):
        for j in range(1, c):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])

    return memo[r - 1][c - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
