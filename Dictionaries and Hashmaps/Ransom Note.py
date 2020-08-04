"""

problem link : https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

"""

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m_counter = Counter(magazine)
    n_counter = Counter(note)

    for n_word, n_cnt in n_counter.items():
        if n_word not in m_counter and n_cnt > m_counter[n_word]:
            return False
    return True


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
