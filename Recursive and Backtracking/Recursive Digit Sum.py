"""

problem link : https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

"""


# !/bin/python3


# Complete the superDigit function below.
def digit_sum(n: int):
    """
    poor efficiency

    :param n:
    :return:
    """
    if n < 10:
        return n
    total = 0
    digits = 0
    t = n
    while t > 0:
        t = t // 10
        digits += 1

    while digits > 0:
        temp = 10 ** (digits - 1)
        first_digit = n // temp
        total += first_digit
        n -= temp * first_digit
        digits -= 1

    return total


def digit_sum_1(n: int):
    return sum([int(s) for s in str(n)])


def superDigit(n, k):
    first_digit_sum = digit_sum_1(n) * k

    def recursion(num: int):
        if num < 10:
            return num
        return recursion(digit_sum(num))

    return recursion(first_digit_sum)


def superDigit_1(n, k):
    x = n * k % 9
    return x if x else 9


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
