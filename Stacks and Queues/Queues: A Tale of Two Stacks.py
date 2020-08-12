"""

problem link : https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

"""


class MyQueue(object):

    def __init__(self):
        self.left = []
        self.right = []

    def peek(self):
        return self.left[-1]

    def pop(self):
        val = self.left.pop()
        if not self.left:
            while self.right:
                self.left.append(self.right.pop())
        return val

    def put(self, value):
        if not self.left and not self.right:
            self.left.append(value)
        elif self.left:
            self.right.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
