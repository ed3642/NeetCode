# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

import bisect
from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # good usage of precompute optimization to go from 6000ms to 100ms
        # since 2 ** n takes O(log n)
        
        n = len(nums)
        MOD = 10 ** 9 + 7
        nums.sort()

        # precompute powers of 2
        pow2 = [1] * n
        num = 1
        for i in range(1, n):
            num = (num << 1) % MOD
            pow2[i] = num

        count = 0


        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                # find first valid r
                need = target - nums[l]
                r = bisect.bisect_right(nums, need, l, r) - 1
            else:
                # take or not take from (l, r]
                count = (count + pow2[r - l]) % MOD
                l += 1
        
        return count % MOD

    def numSubseq(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        MOD = 10 ** 9 + 7
        nums.sort()

        # precompute powers of 2
        pow2 = [1] * n
        num = 1
        for i in range(1, n):
            num = (num << 1) % MOD
            pow2[i] = num

        count = 0

        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                # take or not take from (l, r]
                count = (count + pow2[r - l]) % MOD
                l += 1
        
        return count % MOD
