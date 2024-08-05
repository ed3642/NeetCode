from functools import lru_cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, j):

            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if i == 0:
                return dp(0, j - 1)
            if j == 0:
                return dp(i - 1, 0)
            
            return dp(i - 1, j) + dp(i, j - 1)
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        return dp(n - 1, m - 1)