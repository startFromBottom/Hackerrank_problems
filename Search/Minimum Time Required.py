"""

problem link : https://www.hackerrank.com/challenges/minimum-time-required/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# # Complete the minTime function below.
# # Time limits exceeded

# def minTime(machines, goal):
#     counter = Counter(machines)
#     days = 1
#     productions = 0
#     while True:
#         for k, v in counter.items():
#             if days % k == 0:
#                 productions += v
#         if productions >= goal:
#             break
#         days += 1
#     return days

def minTime(machines, goal):
    machines.sort()
    lowest, highest = machines[0], machines[-1]

    # 가장 빠르게 처리
    lo = (goal // (len(machines) / lowest))
    # 가장 느리게 처리
    hi = (goal // (len(machines) / highest))

    while lo < hi:
        mid = (hi + lo) // 2
        total = sum([mid // machine for machine in machines])
        if total >= goal:
            hi = mid
        elif total < goal:
            lo = mid + 1
    return int(lo)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
