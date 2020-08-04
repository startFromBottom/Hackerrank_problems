"""

problem link :  https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

"""

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the freqQuery function below.
def freqQuery(queries):
    # key : 각 원소, value : 원소의 개수
    val_counter = defaultdict(int)
    # key: frequency, value : array 내에 frequency 만큼 존재하는 원소의 집합
    frequency_dict = defaultdict(set)

    arr = []

    for i, q in enumerate(queries):

        if q[0] == 1:  # insert
            val_counter[q[1]] += 1
            cnt = val_counter[q[1]]
            if q[1] in frequency_dict[cnt - 1]:
                frequency_dict[cnt - 1].remove(q[1])
            frequency_dict[cnt].add(q[1])
        elif q[0] == 2 and val_counter[q[1]] > 0:  # delete
            val_counter[q[1]] -= 1
            cnt = val_counter[q[1]]
            if cnt >= 0 or q[1] in frequency_dict[cnt + 1]:
                frequency_dict[cnt + 1].remove(q[1])
            frequency_dict[cnt].add(q[1])
        elif q[0] == 3:  # check frequency
            if frequency_dict[q[1]]:
                arr.append(1)
            else:
                arr.append(0)
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
