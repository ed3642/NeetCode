# https://leetcode.com/problems/maximal-square

from functools import lru_cache
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] > 0:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
        
        max_num = 0
        for i in range(n):
            for j in range(m):
                max_num = max(matrix[i][j], max_num)
        
        return max_num * max_num
    
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, j):
            
            if matrix[i][j] == '0':
                return 0
            if i == 0 or j == 0:
                return int(matrix[i][j])

            state_up = dp(i - 1, j)
            state_left = dp(i, j - 1)
            state_left_up = dp(i - 1, j - 1)

            return min(state_up, state_left, state_left_up) + 1
        
        n = len(matrix)
        m = len(matrix[0])

        max_square_side = 0
        for i in range(n):
            for j in range(m):
                max_square_side = max(max_square_side, dp(i, j))
        return max_square_side * max_square_side