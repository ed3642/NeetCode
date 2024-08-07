class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums) == 1:
            return

        n = len(nums)
        # place l on the first 0
        l = 0
        while l < n and nums[l] != 0:
            l += 1
        r = l + 1

        # swap when we see a 0 on r
        while r < n:
            if nums[r] == 0:
                r += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1