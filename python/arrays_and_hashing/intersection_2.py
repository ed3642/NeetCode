# https://leetcode.com/problems/intersection-of-two-arrays-ii
from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)

        intersection = set(counts1.keys()) & set(counts2.keys())

        res = []
        for num in intersection:
            min_count = min(counts1[num], counts2[num])
            res += [num] * min_count
        
        return res