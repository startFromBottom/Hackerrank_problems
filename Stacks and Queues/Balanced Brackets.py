"""

problem link : https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s):
    dic = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    for char in s:
        if not stack and char in dic:
            return "NO"
        if char in dic.values():
            stack.append(char)
        elif dic[char] == stack[-1]:
            stack.pop()
        else:
            return "NO"

    if stack:
        return "NO"
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
