# https://leetcode.com/problems/search-a-2d-matrix-ii/
import bisect
from typing import List

class Solution:

    # O(n + m) n=len(matrix) m=len(matrix[0])
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # top right start search
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
        return False

    # O(n log m) n=len(matrix) m=len(matrix[0])
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (l + r) // 2
                if target < arr[m]:
                    r = m - 1
                elif target > arr[m]:
                    l = m + 1
                else:
                    return True
            return False
        
        I_BOUND = len(matrix)

        first_col = [matrix[i][0] for i in range(I_BOUND)]

        last_possible_row = bisect.bisect_right(first_col, target) - 1

        for i in range(last_possible_row, -1, -1):
            if matrix[i][0] <= target <= matrix[i][-1]:
                if binary_search(matrix[i]):
                    return True
        
        return False