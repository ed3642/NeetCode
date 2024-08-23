# https://leetcode.com/problems/stone-game-ii
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        
        # alice always starts
        # minimize bobs rocks

        @lru_cache(maxsize=None)
        def max_rocks(start, previous_max_pile_i_taken):
            # can pick up all the remaining piles
            if start + 2 * previous_max_pile_i_taken >= N:
                return postfix_sum[start]

            # minimax the next players move => mininimize the next players best move
            _min = float('inf')
            for i in range(1, 2 * previous_max_pile_i_taken + 1):
                pos = start + i
                _min = min(max_rocks(pos, max(i, previous_max_pile_i_taken)), _min)
            
            # subtract oponents best outcome
            return postfix_sum[start] - _min 

        N = len(piles)
        postfix_sum = piles.copy()
        for i in range(N - 2, -1, -1):
            postfix_sum[i] += postfix_sum[i + 1]

        return max_rocks(0, 1)