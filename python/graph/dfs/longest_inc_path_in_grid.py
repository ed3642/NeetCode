# https://leetcode.com/problems/longest-increasing-path-in-a-matrix

from typing import List

class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # since the graph is acyclic we dont need a visited set, we wont visit a lower or equal cell again
        # also store each cells score in a cache for preceeding dfs calls
        
        def dfs(i, j, depth):
            if cache[i][j] != -1:
                return cache[i][j]
            
            depth = 0

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and matrix[n_i][n_j] > matrix[i][j]:
                    depth = max(dfs(n_i, n_j, depth + 1), depth)

            cache[i][j] = depth + 1
            return depth + 1

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND

        I_BOUND = len(matrix)
        J_BOUND = len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_depth = 0
        cache = [[-1] * J_BOUND for _ in range(I_BOUND)]

        for i in range(I_BOUND):
            for j in range(J_BOUND):
                max_depth = max(dfs(i, j, 0), max_depth)
        
        return max_depth

    # TLE
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def dfs(i, j, visited, depth):
            depth = 0

            for d_i, d_j in directions:
                n_i = i + d_i
                n_j = j + d_j
                if is_in_bounds(n_i, n_j) and matrix[n_i][n_j] > matrix[i][j] and not visited[n_i][n_j]:
                    visited[n_i][n_j] = True
                    depth = max(dfs(n_i, n_j, visited, depth + 1), depth)
                    visited[n_i][n_j] = False
            return depth + 1

        def is_in_bounds(i, j):
            return 0 <= i < I_BOUND and 0 <= j < J_BOUND

        I_BOUND = len(matrix)
        J_BOUND = len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_depth = 0

        for i in range(I_BOUND):
            for j in range(J_BOUND):
                visited = [[False] * J_BOUND for _ in range(I_BOUND)]
                max_depth = max(dfs(i, j, visited, 0), max_depth)
        
        return max_depth