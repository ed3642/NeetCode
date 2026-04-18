# https://leetcode.com/problems/flood-fill

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(i, j):
            image[i][j] = color

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and image[n_i][n_j] == start_color:
                    dfs(n_i, n_j)

        def is_in_bounds(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS

        start_color = image[sr][sc]
        if start_color == color:
            return image
        ROWS = len(image)
        COLS = len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dfs(sr, sc)
        return image