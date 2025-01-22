# https://leetcode.com/problems/first-completely-painted-row-or-column
from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        num_to_coords = {}
        I_BOUNDARY = len(mat)
        J_BOUNDARY = len(mat[0])
        row_filled = [J_BOUNDARY] * I_BOUNDARY
        col_filled = [I_BOUNDARY] * J_BOUNDARY

        for i in range(I_BOUNDARY):
            for j in range(J_BOUNDARY):
                num_to_coords[mat[i][j]] = (i, j)
        
        for index, num in enumerate(arr):
            i, j = num_to_coords[num]
            row_filled[i] -= 1
            if row_filled[i] == 0:
                return index
            col_filled[j] -= 1
            if col_filled[j] == 0:
                return index
        
        return -1 # shouldnt happen
