# https://leetcode.com/problems/map-of-highest-peak
from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        I_BOUNDARY = len(isWater)
        J_BOUNDARY = len(isWater[0])
        
        q = deque()
        visited = [[False] * J_BOUNDARY for _ in range(I_BOUNDARY)]

        for i in range(I_BOUNDARY):
            for j in range(J_BOUNDARY):
                if isWater[i][j] == 1:
                    visited[i][j] = True
                    q.append((0, i, j))

        while q:
            depth, i, j = q.popleft()
            isWater[i][j] = depth

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and not visited[n_i][n_j]:
                    visited[n_i][n_j] = True
                    q.append((depth + 1, n_i, n_j))

        return isWater
