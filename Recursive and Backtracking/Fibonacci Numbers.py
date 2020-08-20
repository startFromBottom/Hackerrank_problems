"""

problem link : https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

"""


def fibonacci(n):
    """
    recursion (not efficient)
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_1(n):
    """
    recursion solution (more efficient than fibonacci)
    """

    def go(a, b, cur):
        if cur == n:
            return a
        return go(b, a + b, cur + 1)

    return go(0, 1, 0)


def fibonacci_2(n):
    """
    memoization technics
    """
    if n <= 1:
        return n
    memo = [0] * n
    memo[0], memo[1] = 1, 1
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[-1]


def fibonacci_3(n):
    """
    iterative solution
    """
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x


n = int(input())
print(fibonacci(n))
