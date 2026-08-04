# https://leetcode.com/problems/shift-2d-grid

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        # [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
        # [9,1,2,3,4,5,6,7,8]

        N = len(grid)
        M = len(grid[0])
        size = N*M
        flat = [0]*size

        for i in range(N):
            for j in range(M):
                flat[i*M+j] = grid[i][j]
        
        flat = flat+flat
        k = k % size
        flat = flat[size-k:(2*size)-k]

        for i in range(N):
            for j in range(M):
                grid[i][j] = flat[i*M+j]

        return grid
