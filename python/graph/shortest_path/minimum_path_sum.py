# https://leetcode.com/problems/minimum-path-sum
import heapq

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    # this is the first cell, it remains unchaged
                    continue
                if i == 0:
                    grid[0][j] += grid[0][j - 1]
                elif j == 0:
                    grid[i][0] += grid[i - 1][0]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[n - 1][m - 1]

    # NOTE: this problem can more efficiently be solved with DP
    def minPathSum(self, grid: list[list[int]]) -> int:
        # dijkstra

        def isValidCoord(i, j):
            return (
                i >= 0 and i < ROWS and
                j >= 0 and j < COLS and
                not visited[i][j]
            )

        ROWS = len(grid)
        COLS = len(grid[0])
        heap = [(0, 0)] # <i, j>
        visited = [[False] * COLS for _ in range(ROWS)]
        totals = [[float('inf')] * COLS for _ in range(ROWS)]
        totals[0][0] = grid[0][0]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            i, j = heapq.heappop(heap)
            visited[i][j] = True

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if isValidCoord(n_i, n_j):
                    candidate_effort = totals[i][j] + grid[n_i][n_j]
                    if candidate_effort < totals[n_i][n_j]:
                        totals[n_i][n_j] = candidate_effort
                        heapq.heappush(heap, (n_i, n_j))

        return totals[ROWS - 1][COLS - 1]