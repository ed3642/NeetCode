class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        def isValid(i, j):
            return (
                i >= 0 and i < ROWS and
                j >= 0 and j < COLS and
                grid[i][j] == "1"
            )
        
        def explore(i, j):
            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if isValid(n_i, n_j):
                    grid[n_i][n_j] = "0" # mark as visited
                    explore(n_i, n_j)
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num_islands = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    num_islands += 1
                    explore(i, j)
        
        return num_islands

