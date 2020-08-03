"""

problem link : https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
#     """
#     Time Complexity : O(len(arr) ** 2) -> time limit exceed
#
#     :param arr:
#     :return:
#     """
#     swap_cnt = 0
#     arr = [n - 1 for n in arr]  # index 안 헷갈리도록...!
#
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[j] == i:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 swap_cnt += 1
#                 break
#     return swap_cnt


def minimumSwaps(arr):
    """
    Time Complexity: O(len(arr))

    :return:
    """
    swap_cnt = 0
    arr = [n - 1 for n in arr]  # index 안 헷갈리도록...!
    val_idx_dict = {val: i for i, val in enumerate(arr)}

    for i, val in enumerate(arr):
        if val == i:
            continue
        swap_idx = val_idx_dict[i]
        arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
        # refresh val_idx_dict
        val_idx_dict[val] = i
        val_idx_dict[arr[swap_idx]] = swap_idx

        swap_cnt += 1

    return swap_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
