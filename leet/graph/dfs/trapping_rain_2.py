# https://leetcode.com/problems/trapping-rain-water-ii/

import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        I_BOUND = len(heightMap)
        J_BOUND = len(heightMap[0])
        max_height_seen = 0
        volume = 0
        VISITED = -1

        heap = []

        for i in range(I_BOUND):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][J_BOUND - 1], i, J_BOUND - 1))
            heightMap[i][0] = VISITED
            heightMap[i][J_BOUND - 1] = VISITED
        for j in range(1, J_BOUND - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[I_BOUND - 1][j], I_BOUND - 1, j))
            heightMap[0][j] = VISITED
            heightMap[I_BOUND - 1][j] = VISITED

        while heap:
            h, i, j = heapq.heappop(heap)

            max_height_seen = max(h, max_height_seen)

            volume += max_height_seen - h

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and heightMap[n_i][n_j] != VISITED:
                    heapq.heappush(heap, (heightMap[n_i][n_j], n_i, n_j))
                    heightMap[n_i][n_j] = VISITED

        return volume
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        # its like your checking the border and seeing the lowest pool you can climb into
        # then moving onto the next highest pool
        
        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        I_BOUNDARY = len(heightMap)
        J_BOUNDARY = len(heightMap[0])

        if I_BOUNDARY < 3 or J_BOUNDARY < 3:
            return 0

        heap = []
        visited = [[False] * J_BOUNDARY for _ in range(I_BOUNDARY)]

        # append outer layer
        for i in range(I_BOUNDARY):
            for j in [0, J_BOUNDARY - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(J_BOUNDARY):
            for i in [0, I_BOUNDARY - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        total_water = 0

        while heap:
            height, i, j = heapq.heappop(heap)

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and not visited[n_i][n_j]:
                    visited[n_i][n_j] = True
                    total_water += max(height - heightMap[n_i][n_j], 0)
                    heapq.heappush(heap, (max(height, heightMap[n_i][n_j]), n_i, n_j))
        
        return total_water