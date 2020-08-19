"""

problem link : https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

"""

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    if head is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not (fast and fast.next):
            return False
        slow = slow.next
        fast = fast.next.next

    return True
