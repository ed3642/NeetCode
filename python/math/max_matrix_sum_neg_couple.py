# https://leetcode.com/problems/maximum-matrix-sum
from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        # minimize the num of negatives
        # prio the largest neg nums to turn positive
        # can only cancel out a neg when there are 2 negs
        # no matter where 2 negatives are placed, we can always cancel them out

        _sum = 0
        num_negatives = 0
        least_magnitude = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = matrix[i][j]
                mag = abs(num)
                print(mag)
                least_magnitude = min(mag, least_magnitude)
                if num < 0:
                    num_negatives += 1
                _sum += mag

        # odd negative one out
        if num_negatives % 2 != 0:
            _sum -= least_magnitude * 2

        return _sum
    