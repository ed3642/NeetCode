# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
from typing import List
import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
            
        # propagate xor
        heap = []
        MAX_I = len(matrix)
        MAX_J = len(matrix[0])
        xor_matrix = [[0] * MAX_J for _ in range(MAX_I)]
        for i in range(MAX_I):
            for j in range(MAX_J):
                above_val = xor_matrix[i-1][j] if i > 0 else 0
                left_val = xor_matrix[i][j-1] if j > 0 else 0
                diag_val = xor_matrix[i-1][j-1] if i > 0 and j > 0 else 0
                xor_matrix[i][j] = matrix[i][j] ^ above_val ^ left_val ^ diag_val
                if len(heap) < k:
                    heapq.heappush(heap, xor_matrix[i][j])
                elif heap[0] < xor_matrix[i][j]:
                    heapq.heapreplace(heap, xor_matrix[i][j])

        # find kth biggest
        return heap[0]
    
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # quickselect performs poorly with losts of repeating values, hence this TLEs
        def partition(l, r):
            pivot = values[r]
            placer_i = l
            for i in range(l, r):
                if values[i] < pivot:
                    values[i], values[placer_i] = values[placer_i], values[i]
                    placer_i += 1
            values[r], values[placer_i] = values[placer_i], values[r]
            return placer_i

        def quickselect(l, r):
            nonlocal KTH_BIGGEST_INDEX
            if not (l < r):
                return
            
            pivot_i = partition(l, r)

            if KTH_BIGGEST_INDEX < pivot_i:
                quickselect(l, pivot_i - 1)
            elif KTH_BIGGEST_INDEX > pivot_i:
                quickselect(pivot_i + 1, r)
            
        # propagate xor
        values = []
        MAX_I = len(matrix)
        MAX_J = len(matrix[0])
        xor_matrix = [[0] * MAX_J for _ in range(MAX_I)]
        for i in range(MAX_I):
            for j in range(MAX_J):
                above_val = xor_matrix[i-1][j] if i > 0 else 0
                left_val = xor_matrix[i][j-1] if j > 0 else 0
                diag_val = xor_matrix[i-1][j-1] if i > 0 and j > 0 else 0
                xor_matrix[i][j] = matrix[i][j] ^ above_val ^ left_val ^ diag_val
                values.append(xor_matrix[i][j])


        # find kth biggest
        N = MAX_I * MAX_J
        KTH_BIGGEST_INDEX = N - k
        quickselect(0, N - 1)
        return values[KTH_BIGGEST_INDEX]
    