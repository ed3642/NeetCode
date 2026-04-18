# https://leetcode.com/problems/frog-jump-ii/

from typing import List

class Solution:
    
    def maxJump(self, stones: List[int]) -> int:
        # just check odd and even paths, and case when theres only 2 stones
        max_jump = stones[-1] - stones[-2]
        for i in range(0, len(stones), 2):
            max_jump = max(stones[i] - stones[i - 2], max_jump)
        for i in range(1, len(stones), 2):
            max_jump = max(stones[i] - stones[i - 2], max_jump)
        return max_jump

    def maxJump2(self, stones: List[int]) -> int:

        def is_valid(jump_size):
            i = 0
            j = 0
            # go to last
            used = [False] * N
            while i < N:
                while j + 1 < N and stones[j + 1] - stones[i] <= jump_size:
                    j += 1
                if i == j:
                    return False # coulnd find a single stone
                if j == N - 1:
                    break # made it to the end
                i = j # last valid pos
                used[i] = True

            # return to first
            i = N - 1
            j = N - 1
            while i > 0:
                last_open_stone = i
                while j - 1 >= 0 and stones[i] - stones[j - 1] <= jump_size:
                    j -= 1
                    if not used[j]:
                        last_open_stone = j
                if i == last_open_stone:
                    return False
                if last_open_stone == 0:
                    break
                i = last_open_stone
            
            return True
        
        N = len(stones)
        l = 1
        r = stones[-1]

        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        
        return l

s = Solution()
print(s.maxJump([0,3,9]))