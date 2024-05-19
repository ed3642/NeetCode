from functools import lru_cache

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, j):
            
            if m - 1 < j or j < 0:
                return float('inf')
            if i == 0:
                print(j)
                return matrix[0][j]

            return min(
                dp(i - 1, j - 1),
                dp(i - 1, j),
                dp(i - 1, j + 1)
            ) + matrix[i][j]
        
        n = len(matrix)
        m = len(matrix[0])
        return min(dp(n - 1, j) for j in range(m))