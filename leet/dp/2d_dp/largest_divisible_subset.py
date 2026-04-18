# https://leetcode.com/problems/largest-divisible-subset

from functools import lru_cache
from typing import List

class Solution:
    # works but pretty slow
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        @lru_cache(maxsize=None)
        def largest(i, prev_i):
            if i >= len(nums):
                return []

            leave = largest(i + 1, prev_i)
            take = []
            if prev_i == -1 or nums[prev_i] % nums[i] == 0:
                take = largest(i + 1, i) + [nums[i]]
            
            if len(take) > len(leave):
                return take
            return leave
            
        nums.sort(reverse=True)

        return largest(0, -1)

    # TLE
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        @lru_cache(maxsize=None)
        def largest(start, curr):
            if start >= len(nums):
                return []

            leave = largest(start + 1, curr)
            take = []
            if curr % nums[start] == 0:
                take = largest(start + 1, curr | nums[start]) + [nums[start]]
            
            if len(take) > len(leave):
                return take
            return leave
            
        nums.sort(reverse=True)

        return largest(0, 0)
    
    # TLE
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        # 11110000 240
        # 00001010 10
        # 00001000 8
        # 00000100 4

        def largest(start, builder):
            if start >= len(nums):
                return builder.copy()

            leave = largest(start + 1, builder)
            take = []
            if all(num % nums[start] == 0 for num in builder):
                builder.append(nums[start])
                take = largest(start + 1, builder)
                builder.pop()
            
            if len(take) > len(leave):
                return take
            return leave
            
        nums.sort(reverse=True)

        return largest(0, [])
    
s = Solution()
print(s.largestDivisibleSubset([1,2,3]))
print(s.largestDivisibleSubset([240,4,8,10]))