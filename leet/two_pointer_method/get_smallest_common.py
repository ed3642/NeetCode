# https://leetcode.com/problems/minimum-common-value

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        a = 0
        b = 0

        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]:
                return nums1[a]
            elif nums1[a] > nums2[b]:
                b += 1
            else:
                a += 1
        
        return -1