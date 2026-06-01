# https://leetcode.com/problems/longest-arithmetic-subsequence

from collections import defaultdict
from typing import List

class Solution:

    # O(n^2) but slightly more optimized about 1000ms faster than next solution
    def longestArithSeqLength(self, nums: List[int]) -> int:

        n = len(nums)
        # dp[i][diff] = max seq len with this diff
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        longest_seen = 1

        for r in range(n):
            for l in range(r):
                diff = nums[r] - nums[l]
                dp[r][diff] = dp[l][diff]+1
                longest_seen = max(dp[r][diff], longest_seen)
        
        return longest_seen

    # O(n^2)
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        def lasl(arr, diff):
            n = len(arr)
            seen_prev_len = defaultdict(int)
            max_len = 1

            for i in range(n):
                need = arr[i] - diff
                max_len = max(seen_prev_len[need]+1, max_len)
                seen_prev_len[arr[i]] = seen_prev_len[need]+1
            
            return max_len

        n = len(nums)
        cand_diff = set()
        for i in range(n):
            for j in range(i):
                if i != j:
                    cand_diff.add(nums[i]-nums[j])
        
        longest_seq = 1
        for diff in cand_diff:
            longest_seq = max(lasl(nums, diff), longest_seq)

        return longest_seq