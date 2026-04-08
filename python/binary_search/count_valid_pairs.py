# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target

from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # there is a two pointer approach thats better
        
        # [-1,1,1,2,3]
        # 2 - (-1) - 1 = 2
        # 2 - 1 - 1 = 0

        def bisect_right(l, r, x):
            while l < r:
                m = (l + r) // 2
                if nums[m] <= x:
                    l = m + 1
                else:
                    r = m
            return l

        n = len(nums)
        count = 0
        nums.sort()

        for i in range(n):
            max_need = target - nums[i] - 1
            
            j = bisect_right(i, n, max_need)
            pairs = (j - 1) - i
            if pairs > 0:
                count += pairs
        
        return count