# https://leetcode.com/problems/jump-game-ii
class Solution:
    
    def jump(self, nums: list[int]) -> int:
        # [2,3,1,1,4]
        # [2,4,3,4,8]
        if len(nums) == 1:
            return 0
        calc_max_pos = lambda i: i + nums[i]


        n = len(nums)
        start = 0
        if calc_max_pos(0) >= n - 1: # can reach the end on the first jump
            return 1
        end = 1
        jumps = 1
        best_pos = -float('inf')
        best_val = -float('inf')
        while end < n - 1:
            max_pos = calc_max_pos(start)
            while end <= max_pos:
                reaches = calc_max_pos(end)
                if best_val < reaches:
                    best_val = reaches
                    best_pos = end
                    if reaches >= n - 1: # First elem that can reach the end
                        return jumps + 1
                end += 1
            start = best_pos
            jumps += 1
        
        return jumps

    def jump(self, nums: list[int]) -> int:
        # basically make the best jump

        # worth of a position
        def heuristic(i):
            return (nums[i] + i)

        tank = 0
        pos = 0
        jumps = 0
        exploring = False
        best = 0

        if len(nums) == 1: # edge case
            return 0

        while tank >= -1 and pos < len(nums):
            if not exploring:
                tank = nums[best] - (pos - best)
                exploring = True
                jumps += 1
            else:
                if heuristic(pos) > heuristic(best):
                    best = pos
                if tank == 0 or pos == len(nums) - 1:
                    exploring = False

                tank -= 1
                pos += 1
        
        return jumps
    
    def jump2(self, nums: list[int]) -> int:
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