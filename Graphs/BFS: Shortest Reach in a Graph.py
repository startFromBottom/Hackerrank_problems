"""

problem link : https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

"""

from collections import deque, defaultdict


class Graph:

    def __init__(self, n):
        self.size = n
        self.graph = defaultdict(list)

    def connect(self, n1: int, n2: int) -> None:
        """
        add one edge and node to graph
        :param n1: node
        :param n2: node
        """
        self.graph[n1 + 1].append(n2 + 1)
        self.graph[n2 + 1].append(n1 + 1)

    def find_all_distances(self, start: int):

        distances = {}
        visited = {start + 1}
        q = deque([(start + 1, 0)])
        while q:
            node, d = q.pop()
            for next_node in self.graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    q.appendleft((next_node, d + 1))
                    distances[next_node] = (d + 1) * 6

        all_nodes = range(1, self.size + 1)
        for a in all_nodes:
            if a not in visited:
                distances[a] = -1

        print(" ".join([str(distances[k]) for k in sorted(distances)]))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
