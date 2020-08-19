"""

problem link : https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

"""

# !/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the reverse function below.

def reverse(head):
    def recursion(node: DoublyLinkedListNode, cur: DoublyLinkedListNode = None) -> DoublyLinkedListNode:
        """
        :param node: 현재 node
        :param cur: recursion 통해 쌓아가는 reversed linked list
        :return:
        """
        if not node:
            return cur
        next, node.next = node.next, cur
        if cur:
            cur.prev = node
        return recursion(next, node)

    return recursion(head)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        # print_doubly_linked_list(llist1, ' ', fptr)
        # fptr.write('\n')

    # fptr.close()
