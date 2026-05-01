# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid

from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        def dfs(i, j):
            if i == N - 1 and j == M - 1:
                return True
            
            directions = openings[grid[i][j]]
            grid[i][j] = VISITED
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and grid[n_i][n_j] != VISITED:
                    # check nei can accept from this direction
                    nei_road_type = grid[n_i][n_j]
                    if (d_i, d_j) == (0, -1) and nei_road_type not in has_right: # left nei needs right
                        continue
                    elif (d_i, d_j) == (-1, 0) and nei_road_type not in has_bot: # top nei needs bot
                        continue
                    elif (d_i, d_j) == (0, 1) and nei_road_type not in has_left: # right nei needs left
                        continue
                    elif (d_i, d_j) == (1, 0) and nei_road_type not in has_top: # bot nei needs top
                        continue

                    if dfs(n_i, n_j):
                        return True
            
            return False

        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < M
        
        openings = {
            1: ((0, -1), (0, 1)), 
            2: ((-1, 0), (1, 0)), 
            3: ((0, -1), (1, 0)), 
            4: ((0, 1), (1, 0)),
            5: ((0, -1), (-1, 0)),
            6: ((-1, 0), (0, 1)), 
        }
        has_left = set([1,3,5])
        has_top = set([2,5,6])
        has_right = set([1,4,6])
        has_bot = set([2,3,4])

        VISITED = -1
        N = len(grid)
        M = len(grid[0])

        return dfs(0, 0)