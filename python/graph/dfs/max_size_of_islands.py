class Solution:
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