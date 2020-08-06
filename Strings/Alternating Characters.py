"""

problem link : https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""


def alternating_characters(s):
    dup_cnt = 0
    alphabet = s[0]
    del_cnt = 0

    for i, char in enumerate(s):
        if char == alphabet:
            dup_cnt += 1
        else:
            del_cnt += dup_cnt - 1
            alphabet = char
            dup_cnt = 1
    del_cnt += dup_cnt - 1

    return del_cnt


N = int(input())

for _ in range(N):
    s = input()
    cnt = alternating_characters(s)
    print(cnt)
