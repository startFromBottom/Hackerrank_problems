"""

problem link : https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

"""

import sys


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    def check(node, min, max):
        if node is None:
            return True
        if node.data <= min or node.data >= max:
            return False
        return check(node.left, min, node.data) \
               and check(node.right, node.data, max)

    return check(root, -sys.maxsize, sys.maxsize)
