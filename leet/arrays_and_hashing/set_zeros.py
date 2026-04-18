# https://leetcode.com/problems/set-matrix-zeroes

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        M = len(matrix[0])
        i_set = set()
        j_set = set()

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    i_set.add(i)
                    j_set.add(j)
        
        for i in i_set:
            for j in range(M):
                matrix[i][j] = 0
        for j in j_set:
            for i in range(N):
                matrix[i][j] = 0