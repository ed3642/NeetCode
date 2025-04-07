# https://leetcode.com/problems/zero-array-transformation-ii

from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        # use a difference array, could also use a fenwich tree but a difference array has O(1) range updates

        def is_valid(last_q_i):
            diff_arr = [0] * (N + 1)
            for l, r, delta in queries[:last_q_i + 1]:
                update(l, r, delta, diff_arr)
            
            # get final processed heights from diff array
            _sum = 0
            for i in range(N):
                _sum += diff_arr[i]
                if _sum < nums[i]:
                    return False
            return True
        
        # update diff array
        def update(l, r, delta, diff_arr):
            diff_arr[l] += delta
            diff_arr[r + 1] -= delta

        # make diff array with prefix
        N = len(nums)
        M = len(queries)
        l = 0
        r = M - 1

        # already all 0s
        if sum(nums) == 0: return 0
        # all queries isnt enough
        if not is_valid(M - 1):
            return -1

        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        
        return l + 1 # + 1 since problem wants 1-indexed