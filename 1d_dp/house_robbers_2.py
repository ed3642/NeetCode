class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        def linearRob(nums):
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            
            return dp[n - 1]
        
        return max(linearRob(nums[:-1]), linearRob(nums[1:]))