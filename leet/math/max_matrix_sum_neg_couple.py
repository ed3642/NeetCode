# https://leetcode.com/problems/maximum-matrix-sum
from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        # minimize the num of negatives
        # prio the largest neg nums to turn positive
        # can only cancel out a neg when there are 2 negs
        # no matter where 2 negatives are placed, we can always cancel them out

        _sum = 0
        negative_parity = 0
        least_magnitude = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = matrix[i][j]
                if num < 0:
                    abs_num = -num
                    least_magnitude = min(abs_num, least_magnitude)
                    _sum += abs_num
                    negative_parity ^= 1
                else:
                    least_magnitude = min(num, least_magnitude)
                    _sum += num

        # odd negative one out
        if negative_parity == 1:
            _sum -= least_magnitude * 2

        return _sum
    