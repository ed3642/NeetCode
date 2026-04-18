# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        N = len(grid)
        M = len(grid[0])
        nums = [0] * (N * M)

        i = 0
        for row in grid:
            for num in row:
                nums[i] = num
                i += 1
            
        ops = 0
        nums.sort()
        target = nums[(N * M) // 2]
        for i in range(len(nums)):
            diff = abs(nums[i] - target)
            if diff % x != 0:
                return -1
            ops += abs(nums[i] - target) // x
        
        return ops