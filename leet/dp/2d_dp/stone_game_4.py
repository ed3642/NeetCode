# https://leetcode.com/problems/stone-game-iv

from functools import cache
import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        # Curr Player Can Win at s stones remaining
        @cache
        def cpcw(rem):
            if rem == 0:
                return False

            for s in squares:
                if s > rem:
                    continue
                next_rem = rem-s
                if next_rem >= 0:
                    if not cpcw(next_rem):
                        return True
            return False

        max_pull = math.ceil(math.sqrt(n))+1
        squares = list(reversed([i*i for i in range(1, max_pull)]))

        return cpcw(n)