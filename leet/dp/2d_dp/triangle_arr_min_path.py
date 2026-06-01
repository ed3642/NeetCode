from collections import deque
from functools import lru_cache
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)

        for i in range(1, n):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][i] += triangle[i - 1][i - 1]
        
        for i in range(2, n):
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        
        return min(triangle[n - 1])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        N = len(triangle)

        for level in range(N - 2, -1, -1):
            for i in range(level + 1):
                triangle[level][i] += min(
                    triangle[level + 1][i],
                    triangle[level + 1][i + 1]
                )

        return triangle[0][0]


    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        N = len(triangle)
        prev_level = triangle[N - 1]

        for level in range(N - 2, -1, -1):
            for i in range(level + 1):
                triangle[level][i] += min(
                    prev_level[i],
                    prev_level[i + 1]
                )
            prev_level = triangle[level]

        return triangle[0][0]

    # MLE
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        
        q = deque([(triangle[0][0], 0, 0)]) # val, level, i
        last_level = len(triangle) - 1
        min_path_sum = float('inf')

        while q:
            _sum, level, i = q.popleft()

            if level == last_level:
                min_path_sum = min(_sum, min_path_sum)

            next_level = level + 1
            if next_level <= last_level:
                q.append((_sum + triangle[next_level][i], next_level, i))
                q.append((_sum + triangle[next_level][i + 1], next_level, i + 1))

        return min_path_sum


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