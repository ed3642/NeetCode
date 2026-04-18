# https://leetcode.com/problems/find-if-array-can-be-sorted
from typing import List

class Solution:
    # NOTE: there is a O(n) solution by splitting the array into segments of the same num_set_bits

    # O(n^2)
    def canSortArray(self, nums: List[int]) -> bool:
        
        N = len(nums)
        num_set_bits = []
        for num in nums:
            num_set_bits.append(bin(num).count('1'))
        
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] > nums[j] and num_set_bits[i] != num_set_bits[j]:
                    return False
        
        return True
    