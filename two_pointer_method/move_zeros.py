class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def place_l(l):
            while l < len(nums) and nums[l] != 0:
                l += 1
            return l
        
        def place_r(r):
            while r < len(nums) and nums[r] == 0:
                r += 1
            return r

        if len(nums) == 1:
            return
        
        l = place_l(0)
        r = place_r(l)

        while r < len(nums):
            nums[l], nums[r] = nums[r], nums[l]
            l = place_l(l)
            r = place_r(r)