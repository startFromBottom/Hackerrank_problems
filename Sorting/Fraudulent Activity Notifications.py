"""

problem link : https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

"""



#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    noti = 0  # answer
    start = sorted(expenditure[:d])
    median = (start[d // 2] + start[d // 2 - 1]) / 2 if d % 2 == 0 \
        else start[d // 2]

    amount = expenditure[d]
    if amount >= 2 * median:
        noti += 1

    for i in range(d, len(expenditure) - 1):
        # find element to remove
        rm_idx = bisect.bisect_left(start, expenditure[i - d])
        del start[rm_idx]
        # insert element
        bisect.insort_left(start, expenditure[i])
        median = (start[d // 2] + start[d // 2 - 1]) / 2 if d % 2 == 0 \
            else start[d // 2]

        amount = expenditure[i + 1]
        if amount >= 2 * median:
            noti += 1

    return noti


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    # fptr.close()
