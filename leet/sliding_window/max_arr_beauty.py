# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/
from typing import List

class Solution:

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # sliding window
        # [1,2,4,6]

        N = len(nums)
        nums.sort()
        max_width = 1
        l = 0
        for r in range(1, N):
            right_end_reach = nums[r] - k
            while l < N and nums[l] + k < right_end_reach:
                l += 1
            max_width = max(r - l + 1, max_width)
        
        return max_width

    # O(n log n)
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        # line sweep, from spans
        # return max intersections

        OPEN = 0
        CLOSE = 1

        events = []

        for num in nums:
            events.append((num - k, OPEN))
            events.append((num + k, CLOSE))
        
        events.sort()
        max_concurrent = 0
        concurrent = 0
        for t, e_type in events:
            if e_type == OPEN:
                concurrent += 1
                max_concurrent = max(concurrent, max_concurrent) # get max after opening
            else:
                max_concurrent = max(concurrent, max_concurrent) # get max before closing
                concurrent -= 1
        
        return max_concurrent
