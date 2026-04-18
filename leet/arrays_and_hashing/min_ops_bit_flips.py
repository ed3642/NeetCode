# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        N = len(nums)
        count = 0

        for i in range(N - 2):
            if nums[i] != 1:
                count += 1
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
        
        # check last section are all 1s
        if not all(num == 1 for num in nums[N - 3:]):
            return -1
        
        return count
