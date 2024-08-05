from collections import defaultdict


class Solution:
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