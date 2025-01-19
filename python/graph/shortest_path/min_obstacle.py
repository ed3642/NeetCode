# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
from collections import deque
import heapq
from typing import List

class Solution:
    # we can do a big optimization with BFS instead of DJikstras by prirotizing empty cells over walls
    # O(i * j)
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        # BFS from top left to bot right
        # walls cost 1 and empty cost 0
        # approach referred to as 0-1 BFS or prioritized BFS 
        # NOTE: unlike https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/ this problem doesnt need a costs array since each cell only has 2 states, once we make a decision on a cells state its the optimal one

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY

        EMPTY = 0
        WALL = 1
        VISITED = -1
        I_BOUNDARY = len(grid)
        J_BOUNDARY = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque([(0, 0, 0)]) # <dist, i, j>
        while q:
            dist, i, j = q.popleft()

            if (i, j) == (I_BOUNDARY - 1, J_BOUNDARY - 1):
                return dist

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and grid[n_i][n_j] != VISITED:
                    if grid[n_i][n_j] == WALL:
                        q.append((dist + 1, n_i, n_j))
                    else:
                        q.appendleft((dist, n_i, n_j))
                    grid[n_i][n_j] = VISITED
        return -1 # shouldnt happen

    # O(i * j log(i * j))
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        # BFS from top left to bot right
        # walls cost 1 and empty cost 0

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY

        EMPTY = 0
        WALL = 1
        VISITED = -1
        I_BOUNDARY = len(grid)
        J_BOUNDARY = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        heap = [(0, 0, 0)] # <dist, i, j>
        while heap:
            dist, i, j = heapq.heappop(heap)

            if (i, j) == (I_BOUNDARY - 1, J_BOUNDARY - 1):
                return dist

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and grid[n_i][n_j] != VISITED:
                    nei_dist = 1 if grid[n_i][n_j] == WALL else 0
                    grid[n_i][n_j] = VISITED
                    heapq.heappush(heap, (dist + nei_dist, n_i, n_j))
        return -1 # shouldnt happen
