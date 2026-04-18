# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        # [1,2,3,4,3,2,5,6,7]
        if k == 1:
            return nums

        N = len(nums)
        M = N - k + 1
        res = [-1] * M

        start = 0
        end = 0
        while start < M:
            failed = False
            while end < start + k - 1:
                end += 1
                if nums[end - 1] >= nums[end] or nums[end - 1] != nums[end] - 1:
                    # saves some work
                    start = end # cant have a proper window with this item in it so skip to it
                    failed = True
                    break
            if not failed:
                # got to the end of this window    
                res[start] = nums[end]
                start += 1

        return res
