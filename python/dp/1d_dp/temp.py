class Solution:
    def rob1(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return max(dp[-1], dp[-2])
    
    def rob2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        memo = {}
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i - 1), nums[i] + dp(i - 2))
            return memo[i]

        return dp(n - 1)
    
    def rob3(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        t1 = nums[0]
        t2 = max(nums[0], nums[1])
        temp = t1

        for i in range(2, n):
            temp = max(t2, nums[i] + t1)
            t1 = t2
            t2 = temp
        
        return max(t1, t2)