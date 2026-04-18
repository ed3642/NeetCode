class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) # size of interval with missing number
        total = sum(nums)
        total_interval = (n * (n + 1)) // 2

        return total_interval - total