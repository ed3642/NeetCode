class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        i = 0
        tank = 0
        while tank >= 0 and i < len(nums):
            tank = max(tank, nums[i])
            i += 1
            tank -= 1

        return True if i == len(nums) else False
    
    def canJump2(self, nums: list[int]) -> bool:
        n = len(nums)
        goal = n - 1
        i = n - 2

        for i in range(goal, -1, -1):
            if nums[i] + i >= goal:
                goal = i       

        return goal == 0