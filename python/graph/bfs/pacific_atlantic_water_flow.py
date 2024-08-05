from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        # flow in reverse
        def isValidCoord(parent_i, parent_j, i, j, visited: set):
            return (
                i >= 0 and i < rows and
                j >= 0 and j < cols and
                (i, j) not in visited and
                heights[parent_i][parent_j] <= heights[i][j]
            )
        
        def bfs(coast, visited: set):
            for r, c in coast:
                queue.append((r, c))
                visited.add((r, c))
                while queue:
                    i, j = queue.popleft()
                    visited.add((i, j))

                    for d_i, d_j in directions:
                        n_i = i + d_i
                        n_j = j + d_j
                        if isValidCoord(i, j, n_i, n_j, visited):
                            queue.append((n_i, n_j))
                            visited.add((n_i, n_j))

        rows = len(heights)
        cols = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        pacific_coast = [(i, 0) for i in range(rows)] + [(0, j) for j in range(1, cols)]
        atlantic_coast = [(i, cols - 1) for i in range(rows)] + [(rows - 1, j) for j in range(cols - 1)]
        visited_pacific = set()
        visited_atlantic = set()

        bfs(pacific_coast, visited_pacific)
        bfs(atlantic_coast, visited_atlantic)
            
        return visited_pacific & visited_atlantic