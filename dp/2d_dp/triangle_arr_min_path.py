from functools import lru_cache

class Solution:

    # do dp for the top of the triangle elem, better
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(
                    triangle[i + 1][j], 
                    triangle[i + 1][j + 1])
                
        return triangle[0][0]

    # do dp for all of the bottom row
    def minimumTotal2(self, triangle: list[list[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, j):

            if i == 0 and j == 0:
                return triangle[0][0]
            if j == 0:
                return dp(i - 1, j) + triangle[i][j]
            if j == len(triangle[i]) - 1:
                return dp(i - 1, j - 1) + triangle[i][j]
            
            return min(dp(i - 1, j - 1), dp(i - 1, j)) + triangle[i][j]

        n = len(triangle)
        last_row_len = len(triangle[-1])
        return min(dp(n - 1, j) for j in range(last_row_len))