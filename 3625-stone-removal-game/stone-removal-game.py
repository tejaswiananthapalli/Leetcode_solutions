class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 0
        take = 10

        while n >= take:
            n = n - take
            take = take - 1
            turn = turn + 1

        return turn % 2 == 1