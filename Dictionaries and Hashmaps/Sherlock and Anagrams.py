"""

problem link : https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

"""

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    cnt = 0
    for l in range(1, len(s)):
        dic = defaultdict(list)
        
        for i in range(0, len(s) - l + 1):
            part = "".join(sorted(s[i:i + l]))
            dic[part].append(i)

        for k, v in dic.items():
            length = len(v)
            if length > 1:
                cnt += (length * (length - 1)) // 2
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
