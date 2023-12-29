from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        def isPacificCoast(i, j):
            return (i == 0 or j == 0)

        def isAtlanticCoast(i, j):
            return (i == rows - 1 or j == cols - 1)
    
        def isValidCoord(parent_i, parent_j, i, j):
            return (
                i >= 0 and i < rows and
                j >= 0 and j < cols and
                (i, j) not in visited and
                heights[parent_i][parent_j] >= heights[n_i][n_j]
            )

        rows = len(heights)
        cols = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set() # <(i, j)>
        pacific_canal = set()
        atlantic_canal = set()
        res = [] 
        queue = deque()
        reached_pacific = False
        reached_atlantic = False

        for r in range(rows):
            for c in range(cols):
                queue.clear()
                visited.clear()
                reached_pacific = False
                reached_atlantic = False
                queue.append((r, c))
                potential_canal = []
                # run bfs on each cell and see if it can reach both coast
                while queue:
                    i, j = queue.popleft()
                    visited.add((i, j))
                    potential_canal.append((i, j))
                    if isPacificCoast(i, j):
                        reached_pacific = True
                    if isAtlanticCoast(i, j):
                        reached_atlantic = True
                    if reached_atlantic and reached_pacific:
                        res.append([r, c])
                        break

                    for d_i, d_j in directions:
                        n_i = i + d_i
                        n_j = j + d_j
                        if isValidCoord(i, j, n_i, n_j):
                            queue.append((n_i, n_j))
            
        return res