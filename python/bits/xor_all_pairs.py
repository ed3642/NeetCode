# https://leetcode.com/problems/bitwise-xor-of-all-pairings
from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        all_b_xor = 0
        
        parity_nums1 = len(nums1) % 2
        parity_nums2 = len(nums2) % 2
        if parity_nums1 == 0 and parity_nums2 == 0:
            return 0
        elif parity_nums2 == 0:
            for num in nums2:
                all_b_xor ^= num
            return all_b_xor
        
        xor_total = 0
        if parity_nums1 == 0:
            xor_total = 0
        else:
            for num in nums2:
                all_b_xor ^= num
            xor_total = all_b_xor

        for num in nums1:
            xor_total ^= num
        
        return xor_total

    def xorAllNums2(self, nums1: List[int], nums2: List[int]) -> int:
        
        xor_total = 0

        for num1 in nums1:
            for num2 in nums2:
                xor_total ^= num1 ^ num2
        
        return xor_total
    