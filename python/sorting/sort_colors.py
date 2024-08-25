# https://leetcode.com/problems/sort-colors
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dutch national flag problem
        # l and r are where you place the 0's and 2's
        # m is the elem were inspecting
        
        l = 0
        r = len(nums) - 1
        m = 0

        while m <= r:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
            else:
                m += 1
