"""

problem link : https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

"""

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))

    ai, bi, ci = 0, 0, 0
    cnt = 0

    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1

        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1

        cnt += ai * ci
        bi += 1
    return cnt


def tripletsViaBisect(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    return sum((bisect.bisect(a, x) * bisect.bisect(c, x) for x in b))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
