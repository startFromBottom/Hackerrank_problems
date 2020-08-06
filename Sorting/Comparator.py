from functools import cmp_to_key


class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    @staticmethod
    def comparator(a, b) -> int:
        """
        :param a: Player
        :param b: Player
        :return:
        """
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        elif a.name < b.name:
            return -1
        elif a.name > b.name:
            return 1
        else:
            return 0





if __name__ == "__main__":
    p1 = Player("aaa", 123)
    p2 = Player("bbb", 123)

    data = [p1, p2]

# n = int(input())
# data = []
# for i in range(n):
#     name, score = input().split()
#     score = int(score)
#     player = Player(name, score)
#     data.append(player)
#
# data = sorted(data, key=cmp_to_key(Player.comparator))
# for i in data:
#     print(i.name, i.score)