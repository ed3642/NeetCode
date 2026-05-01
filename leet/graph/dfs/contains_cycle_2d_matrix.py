# https://leetcode.com/problems/detect-cycles-in-2d-grid

from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:        
        
        def dfs(i, j, seen):
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and grid[n_i][n_j] == grid[i][j]:
                    if parent[i][j] != (n_i, n_j):
                        if (n_i, n_j) in seen:
                            return True # found loop
                        parent[n_i][n_j] = (i, j)
                        seen.add((n_i, n_j))
                        if dfs(n_i, n_j, seen):
                            return True
            
            return False

        def is_in_bounds(i, j):
            return 0 <= i < N and 0 <= j < M

        NOT_SET = '-1'
        N = len(grid)
        M = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        parent = [[NOT_SET] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if parent[i][j] == NOT_SET:
                    if dfs(i, j, set((i, j))):
                        return True

        return False
