# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid
from functools import lru_cache
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(i, j):
            best = 0
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j):
                    if grid[i][j] < grid[n_i][n_j]:
                        best = max(dfs(n_i, n_j) + 1, best)
            return best

        def is_in_bounds(i, j):
            return (i >= 0 and i < MAX_I and
                    j >= 0 and j < MAX_J)

        MAX_I = len(grid)
        MAX_J = len(grid[0])

        directions = [(-1, 1), (0, 1), (1, 1)]

        best = 0
        for i in range(MAX_I):
            best = max(dfs(i, 0), best)
        return best
        