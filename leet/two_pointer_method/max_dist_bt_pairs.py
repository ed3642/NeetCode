# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values

from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        #[55,30,5,4,2] [100,20,10,10,5]
        #[55,30,5,4,2] [5,10,10,20,100]

        l = 0
        r = 0
        max_dist = 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                max_dist = max(r - l, max_dist)
                r += 1
            else:
                l += 1
                if l > r:
                    r += 1
        
        return max_dist

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        def bisect_left(arr, t):
            l = 0
            r = N2

            while l < r:
                m = (l + r) // 2
                if arr[m] < t:
                    l = m + 1
                else:
                    r = m
            return l

        N1 = len(nums1)
        N2 = len(nums2)
        nums2_rev = list(reversed(nums2))

        max_dist = 0
        for i in range(N1):
            j_on_rev = bisect_left(nums2_rev, nums1[i])
            if j_on_rev == N2:
                continue
            j = N2 - 1 - j_on_rev
            max_dist = max(j - i, max_dist)
        
        return max_dist