# https://leetcode.com/problems/01-matrix
from collections import deque
from typing import List

class Solution:
    # NOTE: could also do a DP appoarch

    # saves memory by not creating auxilary res matrix
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def is_in_bounds(i, j):
            return 0 <= i < MAX_I and 0 <= j < MAX_J

        MAX_I = len(mat)
        MAX_J = len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()
        for i in range(MAX_I):
            for j in range(MAX_J):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')

        depth = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_in_bounds(n_i, n_j) and mat[n_i][n_j] > mat[i][j] + 1:
                        mat[n_i][n_j] = depth
                        q.append((n_i, n_j))
            depth += 1
        
        return mat
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # BFS from 0s and record depth when reaching a 1
        
        def is_in_bounds(i, j):
            return 0 <= i < MAX_I and 0 <= j < MAX_J

        MAX_I = len(mat)
        MAX_J = len(mat[0])
        VISITED = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()
        for i in range(MAX_I):
            for j in range(MAX_J):
                if mat[i][j] == 0:
                    mat[i][j] = VISITED
                    q.append((i, j))

        depth = 0
        distances_to_0 = [[0] * MAX_J for _ in range(MAX_I)]
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                distances_to_0[i][j] = depth
                for d_i, d_j in directions:
                    n_i = i + d_i
                    n_j = j + d_j
                    if is_in_bounds(n_i, n_j) and mat[n_i][n_j] != VISITED:
                        mat[n_i][n_j] = VISITED 
                        q.append((n_i, n_j))
            depth += 1
        
        return distances_to_0