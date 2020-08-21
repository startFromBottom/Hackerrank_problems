"""

problem link : https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

"""
import itertools


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT


def lca(root, v1, v2):
    def search(root, v, path):
        if root is None:
            return -1
        if root.info == v:
            return path + [root]
        elif root.info > v:
            return search(root.left, v, path + [root])
        else:
            return search(root.right, v, path + [root])

    path1 = search(root, v1, [])
    path2 = search(root, v2, [])

    i = -1
    for n1, n2 in itertools.zip_longest(path1, path2):
        i += 1
        if n1 != n2:
            break
    return path1[i - 1]


# Enter your code here

tree = BinarySearchTree()
