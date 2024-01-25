import heapq

class Solution:
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