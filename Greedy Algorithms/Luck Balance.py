"""

problem link : https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):

    # 중요하지 않은 대회는 모두 진다
    not_importants_sum = sum([c[0] for c in contests if c[1] == 0])

    # 중요한 대회 : 제일 큰 k개는 지고, 나머지는 이겨야 한다.
    importants = sorted([c for c in contests if c[1] == 1], key=lambda x: -x[0])
    lose_sum = sum([c[0] for c in importants[:k]])
    win_sum = sum([c[0] for c in importants[k:]])

    return not_importants_sum + lose_sum - win_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
