# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii

from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        longest = [[0] * k for _ in range(n)] # longest[end][rem]
        max_len = 0

        for end in range(n):
            for i in range(end):
                rem = (nums[i] + nums[end]) % k
                longest[end][rem] = longest[i][rem] + 1
                max_len = max(longest[end][rem], max_len)

        return max_len + 1