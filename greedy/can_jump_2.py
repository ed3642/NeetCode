class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            max_i = r
            for i in range(l, r + 1):
                max_i = max(max_i, i + nums[i])
            l = r + 1
            r = max_i
            jumps += 1
        
        return jumps