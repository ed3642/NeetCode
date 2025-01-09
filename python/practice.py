import bisect
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        N1 = len(nums1)
        N2 = len(nums2)

        l1 = 0
        r1 = N1 - 1
        m1 = r1 // 2
        l2 = 0
        r2 = N2 - 1
        m2 = r2 // 2

        nums_to_right = (N1 + N2 + 1) // 2 # right of median

        while True:
            insert_i = bisect.bisect_left(nums2, nums1[m1], l1, r1)
            curr_to_right_1 = N1 - 1 - m1
            curr_to_right_2 = N2 - 1 - m2
            if curr_to_right_1 + curr_to_right_2 == nums_to_right:
                if (N1 + N2) % 2 == 0:

                else:
                    