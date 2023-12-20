class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        goal = n - 1
        i = n - 2

        for i in range(goal, -1, -1):
            if nums[i] + i >= goal:
                goal = i       

        return goal == 0