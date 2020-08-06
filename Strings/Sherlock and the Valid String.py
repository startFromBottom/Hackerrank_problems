#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
from collections import Counter


def check_valid_string(s):
    char_counter = Counter(s)
    values = char_counter.values()
    max_cnt, min_cnt = max(values), min(values)
    count_counter = Counter(values)
    # ex) aaabbbccc
    if len(count_counter) == 1:
        return "YES"
    elif len(count_counter) == 2:
        # ex) aaaabbbcccddd
        if count_counter[max_cnt] == 1 and max_cnt == min_cnt + 1:
            return "YES"
        # ex) aaabbbccccd
        elif count_counter[min_cnt] == 1 and min_cnt == 1:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = check_valid_string(s)

    fptr.write(result + '\n')

    fptr.close()
