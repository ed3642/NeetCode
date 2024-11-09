# https://leetcode.com/problems/max-area-of-island
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def is_valid(i, j):
            return (
                i >= 0 and i < MAX_I and 
                j >= 0 and j < MAX_J and
                grid[i][j] == 1
            )

        def dfs(i, j):
            nonlocal curr_depth
            grid[i][j] = 0
            curr_depth += 1

            for d_i, d_j in directions:
                n_i = i + d_i 
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    dfs(n_i, n_j)

        MAX_I = len(grid)
        MAX_J = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        biggest_island = 0
        curr_depth = 0

        for i in range(MAX_I):
            for j in range(MAX_J):
                if grid[i][j] == 1:
                    curr_depth = 0
                    dfs(i, j)
                    biggest_island = max(curr_depth, biggest_island)

        return biggest_island
    
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0 # mark as visited
            self.size += 1
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if isValidCoord(n_i, n_j):
                    dfs(n_i, n_j)
                    

        def isValidCoord(i, j):
            return (
                i >= 0 and i < rows and
                j >= 0 and j < cols and 
                grid[i][j] == 1
            )
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_size = 0
        self.size = 0

        for i in range(rows):
            for j in range(cols):
                if isValidCoord(i, j):
                    self.size = 0
                    dfs(i, j)
                    max_size = max(self.size, max_size)

        return max_size