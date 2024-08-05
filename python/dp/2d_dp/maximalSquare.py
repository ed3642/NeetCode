from functools import lru_cache

class Solution:
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