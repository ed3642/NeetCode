class Solution:
    # O(m log n), m is the rows and n in the row size
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary_search(arr, target):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = (r + l) // 2
                if target < arr[m]:
                    r = m - 1
                elif target > arr[m]:
                    l = m + 1
                else:
                    return True
            return False
        
        def is_candidate(row):
            return row[0] <= target <= row[-1]
        
        for row in matrix:
            if is_candidate(row) and binary_search(row, target):
                return True
        
        return False
    
    # O(m + n)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # start at bottom left, move up or right accordingly
        # since rows and cols are sorted this never prunes the answer
        M = len(matrix)
        N = len(matrix[0])
        i = M - 1
        j = 0

        while i >= 0 and j < N:
            curr = matrix[i][j]
            if target < curr:
                i -= 1
            elif target > curr:
                j += 1
            else:
                return True
        return False