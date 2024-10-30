# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        MAX_I = len(matrix)
        MAX_J = len(matrix[0])
        total = 0
        biggest_square_end = [[0] * (MAX_J + 1) for _ in range(MAX_I + 1)]
        for i in range(MAX_I):
            for j in range(MAX_J):
                if matrix[i][j] == 1:
                    biggest_square_end[i + 1][j + 1] = min(
                        biggest_square_end[i + 1][j],
                        biggest_square_end[i][j + 1],
                        biggest_square_end[i][j],
                    ) + 1
                    total += biggest_square_end[i + 1][j + 1]
                
        return total