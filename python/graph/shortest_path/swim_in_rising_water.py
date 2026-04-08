# https://leetcode.com/problems/swim-in-rising-water

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND
        
        I_BOUND = len(grid)
        J_BOUND = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        VISITED = -1

        heap = [(grid[0][0], 0, 0)]
        t = 0

        while heap:
            elevation, i, j = heapq.heappop(heap)

            t = max(elevation, t)

            if i == I_BOUND - 1 and j == J_BOUND - 1:
                return t

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and grid[n_i][n_j] != VISITED:
                    heapq.heappush(heap, (grid[n_i][n_j], n_i, n_j))
                    grid[n_i][n_j] = VISITED
        
        return -1 # shouldnt happen
    
    def swimInWater(self, grid: list[list[int]]) -> int:
        # djikstra, distance is how long you have to wait

        def is_valid(i, j):
            return (
                i >= 0 and i < MAX_I and
                j >= 0 and j < MAX_J and
                (i, j) not in visited
            )

        MAX_I = len(grid)
        MAX_J = len(grid[0])
        heap = [(0, 0, 0)] # time_to_wait, i, j, t
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        distances = [[float('inf')] * MAX_J for _ in range(MAX_I)]
        distances[0][0] = 0
        max_dist = grid[0][0] # nodes have to be atleast this


        while heap:
            dist, i, j = heapq.heappop(heap)
            visited.add((i, j))
            max_dist = max(max_dist, dist)

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    candidate_dist = max(grid[n_i][n_j], max_dist)
                    if candidate_dist < distances[n_i][n_j]:
                        distances[n_i][n_j] = candidate_dist
                        heapq.heappush(heap, (candidate_dist, n_i, n_j))

        return distances[MAX_I - 1][MAX_J - 1]
                    