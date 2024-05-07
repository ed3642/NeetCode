class Solution:
    
    def jump(self, nums: list[int]) -> int:
        # basically make the best jump

        # worth of a positio n
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