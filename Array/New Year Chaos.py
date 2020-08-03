"""

problem link : https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# def minimumBribes(q):
#     positions = {v:i+1 for i, v in enumerate(q)}
#     ans = 0
#     for end_pos, start_pos in positions.items():
#         dist = end_pos - start_pos
#         if dist >= 3:
#             print("Too chaotic")
#             return
#         else:
#             ans += abs(dist)
#     print(ans // 2)


# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    q = [n - 1 for n in q]  # index 헷갈리지 않기 위해서..!

    for cur_pos, start_pos in enumerate(q):
        if start_pos - cur_pos > 2:
            print("Too chaotic")
            return

        # 몇 번 움직였는지를 카운트할 때,
        # 특정 person이 몇 번 교환 요청을 했는지가 아니라
        # 몇 번 교환 요청을 요구 받았는지를 세보자.

        # 특정 person(P)과 교환을 하려는 사람은,
        # 가능한 최대 교환 횟수가 2번이므로, P의 원래 자리 앞 자리까지만 이동이 가능하다.
        # -> q에서 start_pos - 1 index ~ cur_pos - 1 index 값을 확인하여
        # start_pos 보다 큰 값을 확인한다. -> 이 것이 곧 P가 몇 번 교환 요청을 받았나와 동치다.
        # start_pos = 0 일 수도 있으니 max(start_pos - 1)로 무조건 0보다 크거나 같게 만든다.

        for j in range(max(start_pos - 1, 0), cur_pos):
            if q[j] > start_pos:
                moves += 1
    print(moves)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

    print([i for i in range(0, 0)])
