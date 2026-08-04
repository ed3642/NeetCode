# https://leetcode.com/problems/predict-the-winner/

from functools import cache
from typing import List

class Solution:
    # bottom up solution is a lot less intuitive

    def predictTheWinner(self, nums: List[int]) -> bool:
        # can reframe representation of dp to not need curr_player
        # each turn the current player wants to maximize the difference between scores so that they win
        # So each step current player wants to take the current value and subtract the other players optimal play

        N = len(nums)

        # Max Score Difference of other player so they are winning
        @cache
        def msd(l, r):
            if l == r:
                return nums[l]

            op1 = nums[l]-msd(l+1, r)
            op2 = nums[r]-msd(l, r-1)
            return max(op1, op2)

        return msd(0, N-1) >= 0


    def predictTheWinner(self, nums: List[int]) -> bool:
        # this is a classic minimax algo

        N = len(nums)

        # max player1 - player2 scores
        @cache
        def ms(l, r, curr_player):
            if l == r:
                if curr_player == 0:
                    return nums[l] # player1 gets the last points
                else:
                    return -nums[l] # player2 gets the last points

            if curr_player == 0:
                op1 = ms(l+1, r, curr_player^1)+nums[l]
                op2 = ms(l, r-1, curr_player^1)+nums[r]
                return max(op1, op2) # player1 must max the score diff
            else:
                op1 = ms(l+1, r, curr_player^1)-nums[l]
                op2 = ms(l, r-1, curr_player^1)-nums[r]
                return min(op1, op2) # player2 must min the score diff 

        return ms(0, N-1, 0) >= 0
