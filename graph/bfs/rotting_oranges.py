from collections import deque

class Solution:
    # num of levels in bfs
    def orangesRotting(self, grid: list[list[int]]) -> int:

        def isValidCoord(i, j):
            return (
                i >= 0 and i < ROWS and
                j >= 0 and j < COLS and
                grid[i][j] == 1
            )

        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        max_level = 0
        good_oranges = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j, 0)) # <i, j, level_depth>
                elif grid[i][j] == 1:
                    good_oranges += 1

        while queue:
            for _ in range(len(queue)):
                i, j, depth = queue.popleft()

                max_level = max(depth, max_level)

                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if isValidCoord(n_i, n_j):
                        queue.append((n_i, n_j, depth + 1))
                        grid[n_i][n_j] = 2
                        good_oranges -= 1

        return max_level if good_oranges == 0 else -1
