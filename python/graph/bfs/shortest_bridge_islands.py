# https://leetcode.com/problems/shortest-bridge
from collections import deque
from typing import List

class Solution:
    # nice use of multi start bfs
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            starting_island_cells.append((i, j))
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and grid[n_i][n_j] == 1:
                    grid[n_i][n_j] = 0
                    dfs(n_i, n_j)

        def bfs():
            q = deque(starting_island_cells)
            depth = 0
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if (i, j) in starting_island_cells:
                        starting_island_cells.remove((i, j))
                    for d_i, d_j in directions:
                        n_i = i + d_i
                        n_j = j + d_j
                        if is_in_bounds(n_i, n_j) and grid[n_i][n_j] != -1:
                            if grid[n_i][n_j] == 0: # not visited yet
                                grid[n_i][n_j] = -1 # mark visited, 1 is reserved for the other island
                                q.append((n_i, n_j))
                            else: # we found the other island
                                return depth
                depth += 1
            return float('inf')

        def is_in_bounds(i, j):
            return (i >= 0 and i < MAX_I and
                    j >= 0 and j < MAX_J)

        MAX_I = len(grid)
        MAX_J = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        starting_island_cells = []
        # find one island
        for i in range(MAX_I):
            if len(starting_island_cells) > 0:
                break
            for j in range(MAX_J):
                if is_in_bounds(i, j) and grid[i][j] == 1:
                    grid[i][j] = 0
                    dfs(i, j)
                    break

        return bfs()