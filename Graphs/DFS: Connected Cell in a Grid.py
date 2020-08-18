"""

problem link : https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxRegion function below.
def maxRegion(grid):
    rows = len(grid[0])
    cols = len(grid)

    def is_valid(i, j):
        if 0 <= i < cols and 0 <= j < rows \
                and grid[i][j] == 1:
            return True
        return False

    def dfs(x, y):
        if is_valid(x, y):
            res = 0
            grid[x][y] = -1
            for (dx, dy) in moves:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    res += 1 + dfs(nx, ny)
            return res
        else:
            return 0

    moves = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    max_cnt = - sys.maxsize

    for i in range(cols):
        for j in range(rows):
            if grid[i][j] == 1:
                max_cnt = max(max_cnt, dfs(i, j) + 1)

    return max_cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
