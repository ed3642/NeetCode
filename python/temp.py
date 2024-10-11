from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        l = 0
        inspecting = 0
        r = len(nums) - 1

        while inspecting <= r:
            if nums[inspecting] == 0:
                nums[l], nums[inspecting] = nums[inspecting], nums[l]
                l += 1
                inspecting += 1
            elif nums[inspecting] == 2:
                nums[r], nums[inspecting] = nums[inspecting], nums[r]
                r -= 1
            else:
                inspecting += 1