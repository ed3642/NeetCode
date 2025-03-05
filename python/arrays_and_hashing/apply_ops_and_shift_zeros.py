# https://leetcode.com/problems/apply-operations-to-an-array

from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        placer_i = 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nums[placer_i], nums[i] = nums[i], nums[placer_i]
                placer_i += 1
        # place last elem
        if nums[-1] != 0:
            nums[placer_i], nums[-1] = nums[-1], nums[placer_i]
            placer_i += 1
        
        return nums

    def applyOperations(self, nums: List[int]) -> List[int]:
        
        first_zero_i = -1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if first_zero_i == -1 and nums[i] == 0:
                first_zero_i = i
            
        placer_i = first_zero_i
        for i in range(first_zero_i + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[placer_i] = nums[placer_i], nums[i]
                placer_i += 1

        return nums
