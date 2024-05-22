import bisect
from functools import lru_cache

class Solution:

    # nice bisect solution
    def lengthOfLIS(self, nums: list[int]) -> int:
        subseq = [nums[0]]

        for num in nums[1:]:
            if num > subseq[-1]:
                subseq.append(num)
            else:
                insert_at = bisect.bisect_left(subseq, num)
                subseq[insert_at] = num

        return len(subseq)

    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for end in range(n):
            for start in range(end):
                if nums[end] > nums[start]:
                    take = dp[start] + 1
                    leave = dp[end]
                    dp[end] = max(take, leave)
        
        return max(dp)

    def lengthOfLIS2(self, nums: list[int]) -> int:
        # explore paths of taking or not taking each option
        #  this works but uses too much memory
        
        @lru_cache(maxsize=None)
        def dp(i, prev_largest):
            
            if i >= len(nums):
                return 0
            
            if nums[i] > prev_largest:
                take = dp(i + 1, nums[i]) + 1
                leave = dp(i + 1, prev_largest)

                return max(take, leave)
            return dp(i + 1, prev_largest) # leave
        
        return dp(0, -float('inf'))