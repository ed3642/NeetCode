# https://leetcode.com/problems/first-missing-positive

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # [3,1,4,-1]

        # [4,3,1,-1]
        # [0,3,1,4]

        # [3,4,1,-1]
        # [1,4,3,-1]
        
        n = len(nums) # missing num will be in [1, n]

        i = 0
        while i < n:
            if nums[i] == 0:
                i += 1
            elif nums[i] < 0 or n < nums[i]:
                # invalid num
                nums[i] = 0
                i += 1
            elif nums[i] == i + 1:
                # num is in the right place
                i += 1
            else:
                index = nums[i] - 1
                if nums[index] != index + 1:
                    nums[index], nums[i] = nums[i], nums[index]
                else:
                    # index already has correct number in it
                    nums[index] = 0

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
