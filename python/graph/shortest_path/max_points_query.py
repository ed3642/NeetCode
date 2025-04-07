# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries

import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        def is_valid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != float('inf')
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        k = len(queries)
        res = [0] * k
        current = 0
        levels = [[0, 0] for _ in range(k)]
        for i, num in enumerate(queries):
            levels[i][0] = num
            levels[i][1] = i
        levels.sort(key=lambda x: x[0])

        level_i = 0
        heap = [(grid[0][0], 0, 0)] # val, i, j
        grid[0][0] = float('inf')

        while heap:
            val, i, j = heapq.heappop(heap)

            while level_i < k and val >= levels[level_i][0]:
                original_i = levels[level_i][1]
                res[original_i] = current # prev record
                level_i += 1
            if level_i == k:
                break # can no longer reach a higher level
            
            current += 1

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    # mark visited
                    heapq.heappush(heap, (grid[n_i][n_j], n_i, n_j))
                    grid[n_i][n_j] = float('inf')

        # queries that reach entire grid
        while level_i < k:
            original_i = levels[level_i][1]
            res[original_i] = current
            level_i += 1

        return res
    