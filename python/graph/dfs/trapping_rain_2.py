# https://leetcode.com/problems/trapping-rain-water-ii
import heapq
from typing import List

class Solution:
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