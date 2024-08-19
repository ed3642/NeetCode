class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_profit = nums
        max_profit[1] = max(max_profit[0], max_profit[1])

        for i in range(2, len(nums)):
            max_profit[i] = max(
                max_profit[i - 1],
                max_profit[i - 2] + max_profit[i]
            )
        
        return max_profit[-1]

    def robTopDown(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(h_num):
            if h_num == 0:
                return nums[0]
            elif h_num == 1:
                return max(nums[0], nums[1])
            
            if h_num not in memo:
                memo[h_num] = max(dp(h_num - 1), dp(h_num - 2) + nums[h_num])
            return memo[h_num]

        n = len(nums)
        memo = {}
        return dp(n - 1)

    def robBottomUp(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return max(dp[-1], dp[-2])