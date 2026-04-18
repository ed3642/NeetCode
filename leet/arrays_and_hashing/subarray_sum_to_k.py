# https://leetcode.com/problems/subarray-sum-equals-k
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # [1,2,3]
        # [1,3,6]

        N = len(nums)
        prefix_sum = nums

        pf_sums = defaultdict(int)
        pf_sums[0] = 1
        count = 0
        for i in range(N):
            if i > 0:
                prefix_sum[i] += prefix_sum[i - 1]
            need = prefix_sum[i] - k
            count += pf_sums[need] 
            pf_sums[prefix_sum[i]] += 1

        return count
    

    def subarraySum(self, nums: list[int], k: int) -> int:
        
        prefix_sum = defaultdict(int)
        count = 0
        total = 0
        for num in nums:
            total += num

            if total == k:
                count += 1
            
            need = total - k
            if need in prefix_sum:
                count += prefix_sum[need]

            prefix_sum[total] += 1
        
        return count