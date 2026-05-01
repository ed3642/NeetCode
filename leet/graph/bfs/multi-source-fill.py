# https://leetcode.com/problems/multi-source-flood-fill

from collections import deque

class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        # could be more optimal
        
        def is_in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        grid = [[0] * m for _ in range(n)]
        q = deque()

        for i, j, c in sources:
            grid[i][j] = c
            q.append((i, j))

        while q:
            boundary = set()
            for _ in range(len(q)):
                i, j = q.popleft()

                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_in_bounds(n_i, n_j):
                        if grid[n_i][n_j] == 0:
                            q.append((n_i, n_j))
                            grid[n_i][n_j] = grid[i][j]
                            boundary.add((n_i, n_j))
                        if (n_i, n_j) in boundary and grid[n_i][n_j] < grid[i][j]:
                            grid[n_i][n_j] = grid[i][j]

        return grid
