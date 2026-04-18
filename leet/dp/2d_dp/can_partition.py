# https://leetcode.com/problems/partition-equal-subset-sum
from functools import lru_cache
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # optimal set solution
         
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = _sum // 2
        can_build = set()

        for num in nums:
            for curr in list(can_build):
                candidate = num + curr
                if candidate < target:
                    can_build.add(num + curr)
                elif candidate == target:
                    return True
            can_build.add(num)
        
        return target in can_build

    def canPartition(self, nums: List[int]) -> bool:

        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        
        half = _sum // 2
        can_build = [False] * (half + 1)
        can_build[0] = True

        for num in nums:
            for curr_sum in range(half, num - 1, -1):
                if can_build[half]:
                    return True
                can_build[curr_sum] = can_build[curr_sum] or can_build[curr_sum - num]

        return can_build[half]

    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(maxsize=None)
        def can_split(i, rem):
            if i >= len(nums) or rem < 0:
                return False
            if rem == 0:
                return True

            return can_split(i + 1, rem - nums[i]) or can_split(i + 1, rem)

        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        
        nums.sort(reverse=True)

        return can_split(0, _sum // 2)

    # O(n * half), (n + 1) * (half + 1) states and each states does O(1)
    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(maxsize=None)
        def can_split(i, _sum):
            nonlocal half

            if i >= len(nums):
                if _sum == half:
                    return True
                return False
            if _sum > half:
                return False
            if _sum == half:
                return True

            return can_split(i + 1, _sum + nums[i]) or can_split(i + 1, _sum)

        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2

        return can_split(0, 0)
    
    # first time i see the topdown solution be faster than the bottom up
    def canPartition(self, nums: list[int]) -> bool:
        
        @lru_cache(maxsize=None)
        def can_partition(i, _sum):

            if _sum == 0:
                return True
            if i >= len(nums) or _sum < 0: # prune the search
                return False

            return (
                can_partition(i + 1, _sum - nums[i]) or # take
                can_partition(i + 1, _sum) # leave
            )
            
        total = sum(nums)
        if total % 2 != 0:
            return False
        nums.sort(reverse=True) # using the biggest numbers first gets us a solution faster, not sorting still works but is slower
        half = total // 2 
        return can_partition(0, half)

    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        nums.sort(reverse=True)
        half = total // 2
        n = len(nums)
        # can_par[index][_sum] -> up to index, can we find subseq that sums to _sum
        can_par = [[False for _ in range(half + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            can_par[i][0] = True

        for end in range(1, n + 1):
            num = nums[end - 1]
            for _sum in range(half + 1):
                if num <= _sum:
                    can_par[end][_sum] = (
                        can_par[end - 1][_sum - num] or
                        can_par[end - 1][_sum]
                    )
                else:
                    can_par[end][_sum] = can_par[end - 1][_sum]

        return can_par[n][half]
