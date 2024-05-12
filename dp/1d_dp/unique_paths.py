from math import comb
from functools import lru_cache

class Solution:
    
    # math counting way
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        return comb(total, m - 1) * comb(total - (m - 1), n - 1)
    
    # dp bottom up
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # set base cases
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        # dp
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[m - 1][n - 1]
    
    # dp top down
    def uniquePaths3(self, m: int, n: int) -> int:

        @lru_cache(maxsize=None)
        def dp(i, j):

            if i < 1 or j < 1:
                return 1
            
            return dp(i, j - 1) + dp(i - 1, j)

        return dp(m - 1, n - 1)