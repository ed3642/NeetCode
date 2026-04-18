# https://leetcode.com/problems/maximum-width-ramp
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        N = len(nums)
        stack = []
        for i in range(N - 1, -1, -1):
            if not stack:
                stack.append(i)
            elif nums[stack[-1]] < nums[i]:
                stack.append(i)
        
        max_diff = 0
        for i in range(N):
            while stack and nums[i] <= nums[stack[-1]]:
                max_diff = max(stack.pop() - i, max_diff)
        
        return max_diff

    def maxWidthRamp(self, nums: List[int]) -> int:

        N = len(nums)
        stack = []
        for i in range(N - 1, -1, -1):
            if not stack:
                stack.append((i, nums[i]))
            elif stack[-1][1] < nums[i]:
                stack.append((i, nums[i]))
        
        max_diff = 0
        last_i = 0
        for i in range(N):
            while stack and nums[i] <= stack[-1][1]:
                last_i, _ = stack.pop()
            max_diff = max(last_i - i, max_diff)
        
        return max_diff