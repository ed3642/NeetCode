# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength2(self, nums: List[int], k: int) -> int:
        # can save a bit of processing by not shrinking the window ever since once we find an array of size X we only care about any bigger onces not smaller or eq size. So we just slide the window instead of skrinking it in the below solution.
        # In all other aspects this solution is better though. 

        N = len(nums)
        ms = 0 # Max Size
        l = 0
        hz = defaultdict(int)
        for r in range(N):
            while hz[nums[r]] >= k:
                hz[nums[l]] -= 1
                l += 1
            hz[nums[r]] += 1
            ms = max(ms, r-l+1)

        return ms

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # slide instead of skrink window, saves a bit of O calculations but higher overhead

        N = len(nums)
        ms = 0 # Max Size
        l = 0
        hz = defaultdict(int)
        r = 0
        bad_elems = 0
        while r < N:
            while r < N and bad_elems > 0:
                hz[nums[l]] -= 1
                if hz[nums[l]] == k: # turned not bad
                    bad_elems -= 1
                l += 1
                hz[nums[r]] += 1
                if hz[nums[r]] == k+1: # turned bad
                    bad_elems += 1
                r += 1

            if bad_elems == 0: # check the window [l, r-1] when done sliding, r-1 since r is the elem to be added
                ms = max(ms, r-l)

            if r < N:
                hz[nums[r]] += 1
                if hz[nums[r]] == k+1:
                    bad_elems = 1
                if bad_elems == 0:
                    ms = max(ms, r-l+1)
                r += 1

        return ms

s = Solution()
print(s.maxSubarrayLength([1,1,3,3], 1))
print(s.maxSubarrayLength([1,1,1,2,2,2,2,1,1], 2))
