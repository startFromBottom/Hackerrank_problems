"""

problem link : https://www.hackerrank.com/challenges/matrix/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

"""


# !/bin/python3


# Complete the minTime function below.


def minTime(roads, machines):
    """

    :param roads: each element : (city1, city2, time)
    :param machines:
    :return:
    """
    count = 0
    parents = list(range(n))
    set_counts = [1] * n

    roads.sort(key=lambda x: x[2], reverse=True)

    is_machine = [False] * n
    for m in machines:
        is_machine[m] = True

    def find(x):
        """
        find parent in disjoint set
        """
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(n1, n2):
        """
        merge n1's parent and n2's parent
        """
        n1 = find(n1)
        n2 = find(n2)
        if n1 != n2:
            # merge small set into large set
            if set_counts[n1] > set_counts[n2]:
                parents[n2] = n1
                set_counts[n1] += set_counts[n2]
            else:
                parents[n1] = n2
                set_counts[n2] += set_counts[n1]

    for (c1, c2, t) in roads:
        c1, c2 = find(c1), find(c2)
        if not (is_machine[c1] and is_machine[c2]):
            union(c1, c2)
            is_machine[c1] = is_machine[c1] or is_machine[c2]
            is_machine[c2] = is_machine[c1]
        else:
            count += t
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input())
        machines.append(machines_item)

    result = minTime(roads, machines)

    # fptr.write(str(result) + '\n')

    # fptr.close()
