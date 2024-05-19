from functools import lru_cache

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, j):
            
            if i == 0 and j == 0:
                return grid[0][0]
            if i == 0:
                return dp(0, j - 1) + grid[i][j]
            if j == 0:
                return dp(i - 1, 0) + grid[i][j]
            
            return min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]

        n = len(grid)
        m = len(grid[0])
        return dp(n - 1, m - 1)