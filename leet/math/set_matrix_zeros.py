class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for row_i in rows:
            for j in range(len(matrix[0])):
                matrix[row_i][j] = 0
        
        for col_i in cols:
            for i in range(len(matrix)):
                matrix[i][col_i] = 0