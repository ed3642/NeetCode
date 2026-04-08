# https://leetcode.com/problems/largest-perimeter-triangle

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        # optimized use of triangle inequality

        N = len(nums)
        nums.sort(reverse=True)

        for i in range(N - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if a < b + c:
                return a + b + c
        
        return 0

    def largestPerimeter(self, nums: List[int]) -> int:
        # check the triangle inqueality
        
        N = len(nums)
        nums.sort(reverse=True)

        for i in range(N):
            a = nums[i]
            for j in range(i + 1, N):
                b = nums[j]
                if a < b * b:
                    for k in range(j + 1, N):
                        c = nums[k]
                        if a >= b + c:
                            break
                        if (b < a + c) and (c < a + b):
                            return a + b + c
        
        return 0