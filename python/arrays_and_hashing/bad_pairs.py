# https://leetcode.com/problems/count-number-of-bad-pairs

from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        # total - good - N
        # [4,1,3,3]
        # [-4,0,-1,0] 
        #   [0,-1,0]   1
        #     [-1,0]   2
        #        [0]   3

        N = len(nums)
        if N < 2:
            return 0
        total_pairs = (N * (N + 1)) // 2

        num_freq = defaultdict(int)
        for i in range(1, N):
            num = i - nums[i]
            num_freq[num] += 1

        good_pairs = 0
        for i in range(N - 1):
            need = i - nums[i]
            good_pairs += num_freq[need]
            num_freq[i + 1 - nums[i + 1]] -= 1 # remove the next elem from availability

        return total_pairs - good_pairs - N
    