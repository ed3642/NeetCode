# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # djikstras boundary breaking variation
        # see the cost of an edge based on how long we have to wait to wait
        
        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY
        
        # check theres at least 1 place to oscillate between from 0
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        I_BOUNDARY = len(grid)
        J_BOUNDARY = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0, 0, 0)] # time, i, j
        visited = set()

        while heap:
            time, i, j = heapq.heappop(heap)

            if i == I_BOUNDARY - 1 and j == J_BOUNDARY - 1:
                return time

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and (n_i, n_j) not in visited:
                    visited.add((n_i, n_j))
                    nei_time = time + 1
                    if nei_time >= grid[n_i][n_j]:
                        # can go
                        heapq.heappush(heap, (nei_time, n_i, n_j))
                    else:
                        # have to wait by oscillating back and forth
                        time_diff = grid[n_i][n_j] - time
                        if time_diff % 2 == 0:
                            heapq.heappush(heap, (grid[n_i][n_j] + 1, n_i, n_j))
                        else:
                            heapq.heappush(heap, (grid[n_i][n_j], n_i, n_j))
        
        return -1