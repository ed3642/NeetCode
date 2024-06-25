from collections import defaultdict

class Solution:
    # nice solution
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # sliding window, count valid subarrays

        n = len(nums)
        prefix_zeros_count = 0
        total_count = 0
        start = 0
        _sum = 0

        for end in range(n):
            _sum += nums[end]
            while start < end and (_sum > goal or nums[start] == 0):
                if nums[start] == 0:
                    prefix_zeros_count += 1
                else:
                    prefix_zeros_count = 0
                _sum -= nums[start]
                start += 1
            
            if _sum == goal:
                total_count += 1 + prefix_zeros_count
        
        return total_count

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        prefix_sum_freqs = defaultdict(int)
        _sum = 0
        total_count = 0
        prefix_sum_freqs[0] = 1

        for num in nums:
            _sum += num
            total_count += prefix_sum_freqs[_sum - goal]
            prefix_sum_freqs[_sum] += 1
        
        return total_count