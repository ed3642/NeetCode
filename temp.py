class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # [1,2,3,4]
        # [1,2,6,24]
        # [24,24,12,4]

        # [24,12,8,6]
        n = len(nums)
        pre_cumulative = [1] * (n + 2)
        post_cumulative = [1] * (n + 2)

        for i in range(n):
            pre_cumulative[i + 1] = nums[i] * pre_cumulative[i]
        
        for i in range(n - 1, -1, -1):
            post_cumulative[i + 1] = nums[i] * post_cumulative[i + 2]
        
        for i in range(1, n + 2 - 1):
            nums[i - 1] = pre_cumulative[i - 1] * post_cumulative[i + 1]

        return nums