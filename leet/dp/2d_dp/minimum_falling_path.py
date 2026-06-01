# https://leetcode.com/problems/minimum-falling-path-sum

from functools import lru_cache
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        for i in range(1, n):
            for j in range(n):
                l = j - 1 if j > 0 else 0
                r = j + 1 if j < n - 1 else n - 1
                matrix[i][j] += min(matrix[i - 1][l], matrix[i - 1][j], matrix[i - 1][r])
        
        return min(matrix[n - 1])
    
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