"""

problem link : https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

"""

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from typing import Set


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, c_cities):
    total_cost = 0

    # make bidirectional graph
    graph = defaultdict(list)
    for c1, c2 in c_cities:
        graph[c1].append(c2)
        graph[c2].append(c1)

    visited = set()

    def dfs(node: int, v: Set) -> Set:
        for k in graph[node]:
            if k not in visited:
                visited.add(k)
                v.add(k)
                v = dfs(k, v)
        return v

    for c in graph:
        if c not in visited:
            group = dfs(c, set())
            l = len(group)
            # add cost for each group
            total_cost += min(c_lib + (l - 1) * c_road, c_lib * l)

    # finally, add isolated cities cost(library cost)
    total_cost += (n - len(visited)) * c_lib

    return total_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
