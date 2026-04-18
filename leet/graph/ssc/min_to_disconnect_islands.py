# tarjans algorithm can be used for better solution
# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/editorial/
# look at foundation material problems
class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        
        def islands_count():
            def dfs(i, j):
                visited.add((i, j))
                surrounding_water = 0
                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_valid(n_i, n_j):
                        if grid[n_i][n_j] == 1 and (n_i, n_j) not in visited:
                            dfs(n_i, n_j)
                        elif grid[n_i][n_j] == 0:
                            surrounding_water += 1

            def is_valid(i, j):
                return (
                    i >= 0 and i < MAX_I and 
                    j >= 0 and j < MAX_J
                )

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            num_islands = 0
            visited = set()

            for i in range(MAX_I):
                for j in range(MAX_J):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j)
                        num_islands += 1
            return num_islands
        
        # exclusive maxes
        MAX_I = len(grid)
        MAX_J = len(grid[0])
        
        num_islands = islands_count()
        if num_islands != 1:
            return 0
        
        for i in range(MAX_I):
            for j in range(MAX_J):
                if grid[i][j] == 1:
                    grid[i][j] = 0 
                    count = islands_count()
                    if 1 < count or count == 0:
                        return 1
                    grid[i][j] = 1 
        return 2