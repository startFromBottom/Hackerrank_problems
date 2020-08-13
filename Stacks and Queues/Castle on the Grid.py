#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    cols = len(grid)
    rows = len(grid[0])

    def is_valid(x, y):
        if 0 <= x < cols and 0 <= y < rows and grid[x][y] == ".":
            return True
        return False

    q = deque([(startX, startY, 0)])
    visited = set((startX, startY))
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while q:
        x, y, cnt = q.pop()
        for dx, dy in moves:
            tx, ty = x, y
            while True:
                tx, ty = tx + dx, ty + dy
                if is_valid(tx, ty):
                    if (tx, ty) == (goalX, goalY):
                        return cnt + 1
                    if (tx, ty) not in visited:
                        visited.add((tx, ty))
                        q.appendleft((tx, ty, cnt + 1))
                else:
                    break
    return -1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
