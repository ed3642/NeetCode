# https://leetcode.com/problems/longest-increasing-subsequence

import bisect
from typing import List

class Solution:

    # optimal solution O(n log n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        s = []

        for num in nums:
            placer_i = bisect.bisect_left(s, num)
            if placer_i == len(s):
                s.append(num)
            else:
                s[placer_i] = num
        
        return len(s)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        # dp[i] = len of LIS ending at i
        dp = [1] * n

        for r in range(1, n):
            for l in range(r):
                if nums[l] < nums[r]:
                    dp[r] = max(dp[l] + 1, dp[r])

        return max(dp)
    
    # dp O(n ^ 2)
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1] * n

        for end in range(1, n):
            for i in range(end):
                if nums[end] > nums[i]:
                    dp[end] = max(dp[i] + 1, dp[end])
        
        return max(dp)
    
    def lengthOfLIS(self, nums: list[int]) -> int:
        # This builds a LIS
        # but it keeps the relative values in order where the seq generated will have the same length as the actual LIS

        def bisect_left(arr, item):
            l = 0
            r = len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < item:
                    l = m + 1
                else:
                    r = m
            return l

        seq = [nums[0]]

        for num in nums[1:]:
            if seq[-1] < num:
                seq.append(num)
            else:
                insert_index = bisect_left(seq, num)
                seq[insert_index] = num
    
        return len(seq)