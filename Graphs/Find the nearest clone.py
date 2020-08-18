"""

problem link : https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

"""
# !/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = defaultdict(list)
    start = -1

    # color : ids[k - 1] k : key of graph
    for f, t in zip(graph_from, graph_to):
        if start == -1 and ids[f - 1] == val:
            start = f
        elif start == -1 and ids[t - 1] == val:
            start = t

        graph[f].append(t)
        graph[t].append(f)

    q = deque([(start, 0)])
    visited = set()

    while q:
        node, d = q.pop()
        if ids[node - 1] == val and node != start:
            return d
        for n in graph[node]:
            if n not in visited:
                q.appendleft((n, d + 1))
                visited.add(n)

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
