# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            _sum = grid[i][j]
            grid[i][j] = 0

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and grid[n_i][n_j] != 0:
                    _sum += dfs(n_i, n_j)
            
            return _sum

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        I_BOUNDARY = len(grid)
        J_BOUNDARY = len(grid[0])

        max_fish = 0
        for i in range(I_BOUNDARY):
            for j in range(J_BOUNDARY):
                if grid[i][j] != 0:
                    max_fish = max(dfs(i, j), max_fish)
        
        return max_fish
    