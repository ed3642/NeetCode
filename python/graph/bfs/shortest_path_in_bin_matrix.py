from collections import defaultdict
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        def isValidNode(i, j):
            return ( i >= 0 and i < rows and
                j >= 0 and j < cols and
                grid[i][j] == 0)

        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1: # early termination
            return -1

        queue = deque([((0, 0), 1)]) # ((i, j), length)
        grid[0][0] = 1  # mark start as visited

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                    (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            (i, j), length = queue.popleft()
            if i == rows - 1 and j == cols - 1:
                return length
            
            for dir in directions:
                n_i = i + dir[0]
                n_j = j + dir[1]
                if isValidNode(n_i, n_j):
                    queue.append(((n_i, n_j), length + 1))
                    grid[n_i][n_j] = 1
        
        return -1