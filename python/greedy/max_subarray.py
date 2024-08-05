class Solution:
    # Kadane's algorithm
    def maxSubArray(self, nums: list[int]) -> int:
        total = 0
        max_total = -float('inf')

        for num in nums:
            total += num
            max_total = max(total, max_total)
            if total < 0:
                total = 0
            
        return max_total