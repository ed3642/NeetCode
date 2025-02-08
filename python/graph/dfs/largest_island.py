# https://leetcode.com/problems/making-a-large-island
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        # label the islands and see the connection that one more cell can make

        def dfs(i, j, color):
            grid[i][j] = color
            size = 1
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and grid[n_i][n_j] == 1:
                    size += dfs(n_i, n_j, color)
            return size

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUNDARY and 0 <= j < J_BOUNDARY

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        island_color_to_sizes = {0: 0} # empty space size
        I_BOUNDARY = len(grid)
        J_BOUNDARY = len(grid[0])
        INITIAL_COLOR = 2 # start at 1 since cells are 0 | 1
        curr_color = INITIAL_COLOR # start at 1 since cells are 0 | 1

        # label islands
        for i in range(I_BOUNDARY):
            for j in range(J_BOUNDARY):
                if grid[i][j] == 1:
                    size = dfs(i, j, curr_color)
                    island_color_to_sizes[curr_color] = size
                    curr_color += 1

        # no islands
        if len(island_color_to_sizes) == 1:
            return 1 # we can always have 1 cell
        
        # see biggest connections
        max_connected_size = island_color_to_sizes[INITIAL_COLOR]
        for i in range(I_BOUNDARY):
            for j in range(J_BOUNDARY):
                if grid[i][j] == 0:
                    connected_size = 1 # +1 for the cell itself
                    used_islands = set()
                    for d_i, d_j in directions:
                        n_i = i + d_i
                        n_j = j + d_j
                        if is_in_bounds(n_i, n_j):
                            island_color = grid[n_i][n_j]
                            if island_color not in used_islands:
                                connected_size += island_color_to_sizes[island_color]
                                max_connected_size = max(connected_size, max_connected_size)
                                used_islands.add(island_color)
        
        return max_connected_size
    