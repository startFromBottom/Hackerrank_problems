"""

problem link : https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

"""


# !/bin/python3


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


# Complete the sortedInsert function below.

def sortedInsert(head, data):
    dummy = head
    before = cur = head

    while cur and cur.data < data:
        before = cur
        cur = cur.next
    # add data in front of cur
    if cur == head:
        cur.prev = DoublyLinkedListNode(data)
        temp = cur.prev
        temp.next = cur
        return cur.prev
    elif cur is None:
        before.next = DoublyLinkedListNode(data)
    else:
        temp = cur.prev
        new = DoublyLinkedListNode(data)
        temp.next = new
        new.prev = temp
        new.next = cur
        cur.prev = new

    return dummy


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        # print_doubly_linked_list(llist1, ' ', fptr)
        # fptr.write('\n')

    # fptr.close()
