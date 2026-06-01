# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference

from collections import defaultdict
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # space optimized
        n = len(arr)
        seen_prev_len = defaultdict(int)
        max_len = 1

        for i in range(n):
            need = arr[i] - difference
            max_len = max(seen_prev_len[need]+1, max_len)
            seen_prev_len[arr[i]] = seen_prev_len[need]+1
        
        return max_len

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        n = len(arr)
        # dp[i] = longest chain with diff constraint up to i
        dp = [1] * n
        seen_i = defaultdict(int)

        for i in range(n):
            need = arr[i] - difference
            if need in seen_i:
                dp[i] = max(dp[seen_i[need]]+1, dp[i])
            seen_i[arr[i]] = i
        
        return max(dp)
