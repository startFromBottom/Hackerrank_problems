"""

problem link : https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

"""

import math
import os
import random
import re
import sys


# Complete the stepPerms function below.
def stepPerms(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    memo = [0] * (n + 1)
    memo[1], memo[2], memo[3] = 1, 2, 4
    for i in range(4, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        # fptr.write(str(res) + '\n')

    # fptr.close()
