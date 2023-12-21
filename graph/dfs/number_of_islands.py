class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            visited.add((i, j))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if isValidCoord(n_i, n_j):
                    dfs(n_i, n_j)


        def isValidCoord(i, j):
            return (
                (i, j) not in visited and
                i >= 0 and i < rows and
                j >= 0 and j < cols and
                grid[i][j] == '1'
            )

        visited = set() # <i, j>
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if isValidCoord(i, j):
                    dfs(i, j) # explores island and marks it as visited
                    islands += 1
        
        return islands
