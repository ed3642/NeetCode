# https://leetcode.com/problems/stone-game-iii

from functools import cache
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # classic minimax, take some values and subtrack opponents optimal play
        # this implementation is called negamax where the players turns are implicitly accounted for
        # the maximizer is always the first player
        # the minimizer is always the second player

        # interesting note: negamax can only be implemented for 2 players. For 3+ players classic minimax with the explicit curr_player_state is needed.

        # max score diff respective to each player
        @cache
        def dp(i):
            if i >= N:
                return 0

            op1, op2, op3 = -INF, -INF, -INF
            val_taken = stoneValue[i]
            op1 = val_taken-dp(i+1)
            if i+1 < N:
                val_taken += stoneValue[i+1]
                op2 = val_taken-dp(i+2)
            if i+2 < N:
                val_taken += stoneValue[i+2]
                op3 = val_taken-dp(i+3)
            return max(op1, op2, op3)

        # alice goes first her score will go towards +inf and bobs towards -inf
        INF = float('inf')
        N = len(stoneValue)
        res = dp(0)
        if res > 0:
            return 'Alice'
        elif res == 0:
            return 'Tie'
        return 'Bob'