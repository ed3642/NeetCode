# https://leetcode.com/problems/number-of-islands
from collections import deque
from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i, j):
            # here you can just use a stack since order of exploration doesnt really matter
            stack = [(i, j)]
            grid[i][j] = VISITED

            while stack:
                for _ in range(len(stack)):
                    i, j = stack.pop()
                    for d_i, d_j in directions:
                        n_i = i + d_i
                        n_j = j + d_j
                        if is_in_bounds(n_i, n_j) and grid[n_i][n_j] != VISITED:
                            grid[n_i][n_j] = VISITED
                            stack.append((n_i, n_j))

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND

        VISITED = '0'
        I_BOUND = len(grid)
        J_BOUND = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0

        for i in range(I_BOUND):
            for j in range(J_BOUND):
                if grid[i][j] != VISITED:
                    islands += 1
                    bfs(i, j)
        
        return islands

    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = VISITED

            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for d_i, d_j in directions:
                        n_i = i + d_i
                        n_j = j + d_j
                        if is_in_bounds(n_i, n_j) and grid[n_i][n_j] != VISITED:
                            grid[n_i][n_j] = VISITED
                            q.append((n_i, n_j))

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND

        VISITED = '0'
        I_BOUND = len(grid)
        J_BOUND = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0

        for i in range(I_BOUND):
            for j in range(J_BOUND):
                if grid[i][j] != VISITED:
                    islands += 1
                    bfs(i, j)
        
        return islands

    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            grid[i][j] = '0'

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_valid(n_i, n_j):
                    dfs(n_i, n_j)

        def is_valid(i, j):
            return (i >= 0 and i < MAX_I and
                    j >= 0 and j < MAX_J and 
                    grid[i][j] == '1')
        
        MAX_I = len(grid)
        MAX_J = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        count = 0
        for i in range(MAX_I):
            for j in range(MAX_J):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count

    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            #visited.add((i, j))
            grid[i][j] = '0'
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if isValidCoord(n_i, n_j):
                    dfs(n_i, n_j)

        def isValidCoord(i, j):
            return (
                #(i, j) not in visited and
                i >= 0 and i < rows and
                j >= 0 and j < cols and
                grid[i][j] == '1'
            )

        #visited = set() # <i, j>
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if isValidCoord(i, j):
                    dfs(i, j) # explores island and marks it as visited
                    islands += 1
        
        return islands
