# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays
from functools import lru_cache
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        def calc_sum(i):
            left_sum = prefix_sum[i - 1] if i > 0 else 0
            return prefix_sum[i + k - 1] - left_sum

        @lru_cache(maxsize=None)
        def max_sum(i, actions_left):
            if actions_left == 0:
                return (0, '')
            if i >= N - (k - 1):
                # no space to continue
                return (-float('inf'), '')

            take_sum, take_indexes = max_sum(i + k, actions_left - 1)
            take_sum += computed_sums[i]
            take_indexes = str(i) + ',' + take_indexes
            skip_sum, skip_indexes = max_sum(i + 1, actions_left)
            
            # prio sum
            if take_sum > skip_sum:
                return (take_sum, take_indexes)
            if skip_sum > take_sum:
                return (skip_sum, skip_indexes)
            
            # then prio index lexicographically smallest
            if take_indexes < skip_indexes:
                return (take_sum, take_indexes)
            return (skip_sum, skip_indexes)
        
        N = len(nums)
        prefix_sum = nums
        for i in range(1, N):
            prefix_sum[i] += prefix_sum[i - 1]
        computed_sums = [0] * (N - (k - 1))
        for i in range(N - (k - 1)):
            computed_sums[i] = calc_sum(i)

        _sum, indexes = max_sum(0, 3)
        return [int(i_str) for i_str in indexes.split(',')[:-1]]
    